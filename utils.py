from getpass import getpass
from prettytable import PrettyTable
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from hashlib import md5
from random import choice
from db import Database
from db_schema import *

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


def signup():

    email = input('Enter email: ')
    username = input('Enter username: ')
    pw = pw_prompt(signup=True)

    hash_salt = salt_shaker()
    hashed_pw = pw_hasher(pw + hash_salt)

    with db.conn:
        db.c.execute(USER_SIGNUP, (email, username, hash_salt, hashed_pw))

    print(f'\nUser {email} added successfully!')


def login():
    email = input('Enter email: ')
    supplied_pw = pw_prompt()

    with db.conn:
        db.c.execute('''
            SELECT *
            FROM USERS WHERE email = (?)
            ''', (email,))

        user_info = db.c.fetchone()
        uid = user_info[0]
        username = user_info[1]
        usertype = user_info[2]
        hash_salt = user_info[4]
        correct_pw = user_info[5]

    pw_to_check = pw_hasher(supplied_pw + hash_salt)

    if pw_to_check == correct_pw:

        global LOGGED_IN, USER_ID, USER_TYPE
        LOGGED_IN = True
        USER_ID = uid
        USER_TYPE = usertype
        print(f'\nWelcome, {username}!')

    else:
        print('Incorrect email or password. Pleasse, try again.')
        login()


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
