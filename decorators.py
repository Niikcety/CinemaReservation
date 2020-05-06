from utils import *
from settings import *
from contextlib import ContextDecorator

class IsLoggedIn(ContextDecorator):

    def __enter__(self):
        if not LOGGED_IN:
            print('You need to be logged in to complete this action.')
            login()
            print("EXITING ENTER")

        return self

    def __exit__(self, exc_type, exc, exc_tb):
        print("EXITING EXIT")