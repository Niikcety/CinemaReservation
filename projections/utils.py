import sqlite3
from db import Database
from .queries import *
from prettytable import PrettyTable


cols = ['     1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10 ']
rows = ['A   ', 'B   ', 'C   ', 'D   ', 'E   ', 'F   ', 'G   ', 'H   ', 'I   ', 'J   ']
room = [['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ']]


# def print_the_room():
#     for i in range(0, 11):
#         if i == 0:
#             print(''.join(cols))
#         else:
#             print(rows[i - 1], ''.join(room[i - 1]))

db = Database()


def count_empty_seats(room):
    free_space = 0
    for i in range(0, 10):
        free_space += room[i].count('. ')
    return free_space


def check_if_seat_is_empty(room, x, y):
    return room[x - 1][y - 1] == '. '


def make_seat_taken(room, x, y):
    room[x - 1][y - 1] = 'X '


# def add_projection():
#     movie_id = input('Please enter movie ID to add: ')
#     type = input('Please enter type of the projection: ')
#     date = input('Please enter date of the projection(yy-mm-dd): ')
#     time = input('Please enter time of the projection(hh:mm): ')

#     #VALIDATE 

#     with db.conn:
#         db.c.execute(ADD_PROJECTION, (movie_id, type, date, time))


# def remove_projection():
#     id = input('Please enter the ID of the projection to remove: ')
#     with db.conn:
#         db.c.execute(DELETE_PROJECTION, (id,))


# def list_projection(*argv):
#     if len(argv) == 0:
#         with db.conn:
#             db.c.execute(SHOW_ALL_PROJECTIONS)
#         films = db.c.fetchall()
#         # list all projections
#     elif len(argv) == 1:
#         with db.conn:
#             db.c.execute(SHOW_PROJECTIONS_BY_FILM_ID, (argv[0],))
#         films = db.c.fetchall()
#         # list projections by film ID
#     elif len(argv) == 2:
#         # list projections by film ID
#         with db.conn:
#             db.c.execute(SHOW_PROJECTIONS_BY_FILM_ID_AND_DATE, (argv[0], argv[1]))
#         films = db.c.fetchall()

#     return films


# printing
def show_projection(films):
    if films == []:
        print('We are sorry, but there aren\'t any projections avaliable')
    else:
        print('ID    DATE       TIME  TYPE')
        for film in films:
            print('[{}] - {} {} ({})'.format(film[0], film[1], film[2], film[3]))


# def show_floor_panel():
#     pass


row_line = 100 * '.'
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


def into_list_of_tuples(str, rows):
    rows = []
    row = []
    for i in range(10):
        row.append(alphabets[i])
        row += list(row_line[i * 10: (i + 1) * 10])
        rows.append(tuple(row))
        row = []
    return rows


def change_floor_panel(place, row_line, seat='X'):
    # example str: B6 = row_line[]
    index = alphabets.index(place[0]) * 10 + int(place[1]) - 1
    new_str = row_line[:index]
    new_str += seat
    new_str += row_line[index + 1:]

    return new_str


def to_table(cols, rows, la=[], ra=[]):
    table = PrettyTable(cols)

    if la != []:
        for col in la:
            table.align[col] = 'l'

    if ra != []:
        for col in ra:
            table.align[col] = 'r'

    for row in rows:
        table.add_row(row)

    return table
