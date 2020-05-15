from .controller import ReservationController
from movies.views import MovieView
from projections.views import ProjectionsViews
from projections.utils import to_table, cols, check_if_seat_is_empty


class ReservationView():
    def __init__(self):
        self.controller = ReservationController()
        self.movie_view = MovieView()
        self.projections_view = ProjectionsViews()

    def make_reservation(self):
        seat_count = int(input('How many seats do you want to book?\n'))

        print('\nHere\'s a list of movies we\'re showing:')
        self.movie_view.list_movies()

        self.projections_view.list_projection()

        pid = input('Choose projection ID: ')

        ## NEED TO BE CHANGED
        uid = input('Choose User ID: ')

        # Checks if there are enough seats
        (floor_string, floor_plan) = self.controller.make_reservation(pid, seat_count)

        if floor_string == 0:
            print('Not enough seats. Please re-enter the information again')
            self.make_reservation()
        else:
            print(to_table(cols, floor_plan))
            seats = []
            for i in range(seat_count):
                print('Please enter the seats you want to book(Example: A5, J1, etc): ')
                while True:
                    seat = input('Seat #{} \n'.format(i + 1))
                    if check_if_seat_is_empty(floor_string, seat) and seat not in seats:
                        seats.append(seat)
                        break
                    else:
                        print('This seat is taken. Please enter again: ')

        print('''You are about to reserve these seats : {}. Type "finalize" if you want to reserve them or "cancel"
              if you want to exit the process.\n'''.format(seats))
        command = input('Waiting for command: ')

        if command == 'finalize':
            self.controller.save_reservation(uid, pid, seats, floor_string)
        elif command == 'cancel':
            pass
        else:
            print('Unknown command')


        # with self.db.conn:
        #     self.db.c.execute('SELECT movies.title FROM projections JOIN movies ON movies.id = projections.movie_id  WHERE projections.id = (?) ', (pid,))
        #     movie_title = self.db.c.fetchone()
        # for i in range(seat_count):
        #     seat = input('Enter row letter and seat number: ')

        #     try:
        #         assert seat_is_free(seat, floor_string), f'Seat {seat} is taken.'
        #     except AssertionError as exc:
        #         print(exc)
        #         self.make_reservation()
        #     # TODO: validate seat number
        #     # TODO: check if seat is avaliable
        #     with self.db.conn:
        #         self.db.c.execute(RESERVE, (seat[0], seat[1], self.uid, pid))
        #     seat_names.append(seat)
        #     print(f'Seat {seat} reserved successfully!')

        #     for seat in seat_names:
        #         floor_string = change_floor_panel(seat, floor_string)

        #     with self.db.conn:
        #         self.db.c.execute('UPDATE projections SET floor_plan = (?) WHERE id = (?)', (floor_string, pid))

        # print(f'\nYou\'ve reserved seat(s) {seat_names} for {movie_title[0]} on {date} at {time}')

