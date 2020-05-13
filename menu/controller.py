from projections.views import ProjectionsViews
from db.db import Database
from db.db_schema import *
from users.utils import *
import ipdb
from projections.utils import into_list_of_tuples, count_empty_seats, change_floor_panel

CLIENT_MENU = '''
1. Show movies
2. Show movie procjections
3. Make reservation
4. List reservations
5. Cancel reservation
6. Exit
'''

ADMIN_MENU = '''
1. Add movie
2. Show movie
3. Show movie projectionsRemove movie
3. Add projection
4. Remove projection
5. Exit
'''


class MenuController:

    def __init__(self, db=Database()):

        self.db = db
        self.uid = None

        self.client_commands = {
            1: self.show_movies,
            2: self.show_movie_projections,
            3: self.make_reservation,
            4: self.list_reservations,
            5: self.cancel_reservation,
        }

        self.admin_commands = {}

    def signup(self):

        email = input('Enter email: ')
        username = input('Enter username: ')
        pw = pw_prompt(signup=True)

        hash_salt = salt_shaker()
        hashed_pw = pw_hasher(pw + hash_salt)

        with self.db.conn:
            self.db.c.execute(USER_SIGNUP, (email, username, hash_salt, hashed_pw))

        print(f'\nUser {email} added successfully!')
        print('Please, log in.\n')
        return self.login()

    def login(self):

        email = input('Enter email: ')
        supplied_pw = pw_prompt()

        with self.db.conn:
            self.db.c.execute('''
                SELECT *
                FROM USERS WHERE email = (?)
                ''', (email,))

            user_info = self.db.c.fetchone()

            hash_salt = user_info[4]
            correct_pw = user_info[5]

        pw_to_check = pw_hasher(supplied_pw + hash_salt)

        if pw_to_check == correct_pw:

            user_obj = UserModel().from_db_record(user_info)
            self.uid = user_obj.id
            print(f'Welcome, {user_info[1]}!')
            return user_obj

        else:
            print('Incorrect email or password. Pleasse, try again.')
            self.login()

    def show_movies(self):
        with self.db.conn:
            self.db.c.execute(LIST_MOVIES)
            cols = [cd[0] for cd in self.db.c.description]
            rows = self.db.c.fetchall()

        print(to_table(cols, rows, la=['title'], ra=['rating']))

    def show_movie_projections(self):
        mid = input('Choose movie ID: ')
        print(f'\nHere are the projections for your chosen movie:')
        ProjectionsViews().list_projection(mid)

    def make_reservation(self):

        seat_count = int(input('How many seats do you want to book?\n'))

        print('\nHere\'s a list of movies we\'re showing:')
        self.show_movies()

        # mid = input('Choose movie ID: ')
        # print(f'\nHere are the projections for your chosen movie:')
        self.show_movie_projections()

        pid = input('Choose projection ID: ')

        with self.db.conn:
            self.db.c.execute('SELECT * FROM projections WHERE id = (?)', (pid,))
            record = self.db.c.fetchone()

        floor_string = record[5]
        date = record[1]
        time = record[2]
        floor_plan = into_list_of_tuples(floor_string)
        empty_seats = count_empty_seats(floor_plan)
        try:
            assert seat_count <= empty_seats, f'Not enough empty seats. There are only {empty_seats} left.'
        except AssertionError as exc:
            print(exc)
            self.make_reservation()

        cols = (' ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(to_table(cols, floor_plan))
        seat_names = []

        with self.db.conn:
            self.db.c.execute('SELECT movies.title FROM projections JOIN movies ON movies.id = projections.movie_id  WHERE projections.id = (?) ', (pid,))
            movie_title = self.db.c.fetchone()
        for i in range(seat_count):
            seat = input('Enter row letter and seat number: ')

            try:
                assert seat_is_free(seat, floor_string), f'Seat {seat} is taken.'
            except AssertionError as exc:
                print(exc)
                self.make_reservation()
            # TODO: validate seat number
            # TODO: check if seat is avaliable
            with self.db.conn:
                self.db.c.execute(RESERVE, (seat[0], seat[1], self.uid, pid))
            seat_names.append(seat)
            print(f'Seat {seat} reserved successfully!')

            for seat in seat_names:
                floor_string = change_floor_panel(seat, floor_string)

            with self.db.conn:
                self.db.c.execute('UPDATE projections SET floor_plan = (?) WHERE id = (?)', (floor_string, pid))

        print(f'\nYou\'ve reserved seat(s) {seat_names} for {movie_title[0]} on {date} at {time}')

    def list_reservations(self):

        with self.db.conn:

            self.db.c.execute(LIST_RESERVE, (self.uid,))
            cols = [cd[0] for cd in self.db.c.description]
            rows = self.db.c.fetchall()

        print(to_table(cols, rows))

    def cancel_reservation(self):
        self.list_reservations()
        rid = input('Choose reservation ID to cancel: ')

        with self.db.conn:
            self.db.c.execute('SELECT * FROM reservations WHERE id = (?)', (rid,))
            r_info = self.db.c.fetchone()
            self.db.c.execute(CANCEL_RESERVE, (rid,))

        print(f'Reservation No. {r_info[0]} has been cancelled successfully!')
