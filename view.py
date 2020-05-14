from os import system
from utils import MAIN_MENU
from users.controller import UserController
from movies.controller import MovieController
from projections.controller import ProjectionController
from reservations.controller import ReservationController


class View():

    def __init__(self):
        self.ucon = UserController()
        self.mcon = MovieController()
        self.pcon = ProjectionController()
        self.rcon = ReservationController()
        self.options = {
            '1': self.mcon.list_movies(),
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }

    def start(self, err=None):
        system('clear')
        print(MAIN_MENU)
        if err is not None:
            print(err)
        choice = input()

        try:
            assert choice.isnumeric(), f'{choice} is not a valid option. Enter a number between 1 and 6.\n'
            assert 1 <= int(choice) <= 6, f'{choice} is not a valid option. Enter a number between 1 and 6.\n'
        except AssertionError as err:
            View.start(err)

        while choice != '6':
            print(self.options[choice]())
        print('Goodbye!')
