import ipdb
from db import Database
from utils import *
from db_schema import *
from settings import *
from decorators import IsLoggedIn

db = Database()


def add_movie():
    title = input('Enter title: ')
    rating = float(input('Enter rating: '))

    with db.conn:
        db.c.execute(ADD_MOVIE, (title, rating))

    print(f'{title} added successfully!')

def list_movies():

    with db.conn:
        db.c.execute(LIST_MOVIES)
        cols = [cd[0] for cd in db.c.description]
        rows = db.c.fetchall()

    print(to_table(cols, rows, la=['title'], ra=['rating']))


def remove_movie():

    mid = input('Enter movie id: ')

    with db.conn:
        db.c.execute('SELECT title FROM movies WHERE id = (?)', (mid,))
        movie_title = db.c.fetchone()[0]

        db.c.execute(REMOVE_MOVIE, (mid,))

    print(f'\"{movie_title}\" removed from schedule.')


def mock_list_projections(mid):
    print('''id, title, date, time, type
2, Die Hard, 2020-05-06, 18:00, 2D\n''')


def mock_proj_floor_plan(pid):
    cols = (' ', 1, 2, 3)
    rows = [
        ('A', '.', '.', '.'),
        ('B', '.', '.', '.'),
        ('C', '.', '.', '.'),
    ]

    print(to_table(cols, rows))


@IsLoggedIn()
def make_reservation():
    # ipdb.set_trace()
    seat_count = int(input('How many seats do you want to book?\n'))

    print('\nHere\'s a list of movies we\'re showing:')
    list_movies()
    mid = input('\nEnter ID of the movie you want to see:\n')

    print(f'\nHere are the projections for your chosen movie:')
    mock_list_projections(mid)
    pid = input('Choose projection ID: ')
    # TODO: Check if seat_count is <= number of avaliable seats in the projection

    mock_proj_floor_plan(pid)

    seat_names = []
    for i in range(seat_count):
        seat = input('Enter row letter and seat number: ')
        # TODO: validate seat number
        # TODO: check if seat is avaliable
        with db.conn:
            db.c.execute(RESERVE, (seat[0], seat[1], USER_ID, pid))
        seat_names.append(seat)

    print(f'\nYou\'ve reserved seat(s) {seat_names} for movietitle on date at time')


def list_reservations():
    pass


make_reservation()
