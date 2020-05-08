from getpass import getpass
from prettytable import PrettyTable
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from hashlib import md5
from random import choice
from db import Database

from users.model import UserModel

db = Database()

chars = ascii_lowercase + ascii_uppercase + digits + punctuation

def salt_shaker():

    hash_salt = ''.join(choice(chars) for i in range(10))

    return hash_salt


def pw_hasher(salted_pw):

    return md5(salted_pw.encode()).hexdigest()


def pw_prompt(signup=False):

    pw = getpass(prompt='Enter password: ')

    if signup:
        reentered_pw = getpass(prompt='Reenter the password: ')

        if pw == reentered_pw:
            return pw
        else:
            print('Reentered password didn\'t match. Please try again.')
            pw = pw_prompt(signup=True)

    return pw





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


def count_empty_seats(room):
    free_space = 0
    for i in range(0, 10):
        free_space += room[i].count('. ')
    return free_space



def seat_is_free(seat, fstring):
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    letter = 10 * rows.index(seat[0])
    num = int(seat[1:])
    chair = fstring[letter + num - 1]

    if chair != 'X':
        return True
    else:
        return False

