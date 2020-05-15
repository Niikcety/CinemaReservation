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
            print('You have successfully made a reservation')
        elif command == 'cancel':
            pass
        else:
            print('Unknown command')

    def list_reservations(self):
        uid = input('Please enter your User ID: ')
        print('Your reservations: \n')

        data = self.controller.list_reservations(uid)
        print(to_table(data[0], data[1]))

    def cancel_reservation(self):
        self.list_reservations()
        rid = input('Choose reservation ID to cancel: ')

        with self.db.conn:
            self.db.c.execute('SELECT * FROM reservations WHERE id = (?)', (rid,))
            r_info = self.db.c.fetchone()
            self.db.c.execute(CANCEL_RESERVE, (rid,))

        print(f'Reservation No. {r_info[0]} has been cancelled successfully!')
