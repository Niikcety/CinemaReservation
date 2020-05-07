''' add proj
remove proj
list proj
list projection floor plan '''

import sqlite3

connection = sqlite3.connect('../cinema.db')
cursor = connection.cursor()

ADD_PROJECTION = '''
    INSERT INTO projections(movie_id, type, date, time) VALUES(?, ?, ?, ?)
'''

DELETE_PROJECTION = '''
    DELETE FROM projections WHERE id = (?)
'''

SHOW_ALL_PROJECTIONS = '''
    SELECT * FROM projections
'''

SHOW_PROJECTIONS_BY_FILM_ID = '''
    SELECT * FROM projections WHERE movie_id = (?)
'''

SHOW_PROJECTIONS_BY_FILM_ID_AND_DATE = '''
    SELECT * FROM projections WHERE movie_id = (?) AND date = (?)
'''


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


def print_the_room():
    for i in range(0, 11):
        if i == 0:
            print(''.join(cols))
        else:
            print(rows[i - 1], ''.join(room[i - 1]))


def count_empty_seats(room):
    free_space = 0
    for i in range(0, 10):
        free_space += room[i].count('. ')
    return free_space


def check_if_seat_is_empty(room, x, y):
    return room[x - 1][y - 1] == '. '


def make_seat_taken(room, x, y):
    room[x - 1][y - 1] = 'X '


def add_projection():
    movie_id = input('Please enter movie ID to add: ')
    type = input('Please enter type of the projection: ')
    date = input('Please enter date of the projection(yy-mm-dd): ')
    time = input('Please enter time of the projection(hh:mm): ')

    #VALIDATE 

    with connection:
        cursor.execute(ADD_PROJECTION, (movie_id, type, date, time))


def remove_projection():
    id = input('Please enter the ID of the projection to remove: ')
    with connection:
        cursor.execute(DELETE_PROJECTION, (id,))


def list_projection(*argv):
    if len(argv) == 0:
        with connection:
            cursor.execute(SHOW_ALL_PROJECTIONS)
        films = cursor.fetchall()
        # list all projections
    elif len(argv) == 1:
        with connection:
            cursor.execute(SHOW_PROJECTIONS_BY_FILM_ID, (argv[0],))
        films = cursor.fetchall()
        # list projections by film ID
    elif len(argv) == 2:
        # list projections by film ID
        with connection:
            cursor.execute(SHOW_PROJECTIONS_BY_FILM_ID_AND_DATE, (argv[0], argv[1]))
        films = cursor.fetchall()

    return films


# printing
def show_projection(films):
    if films == []:
        print('We are sorry, but there aren\'t any projections avaliable')
    else:
        print('ID    DATE       TIME  TYPE')
        for film in films:
            print('[{}] - {} {} ({})'.format(film[0], film[1], film[2], film[3]))


def show_floor_panel():
    pass


show_projection(list_projection())
