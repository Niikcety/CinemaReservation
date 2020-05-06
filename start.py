from getpass import getpass
from db import Database
from utils import *
from db_schema import USER_SIGNUP


db = Database()


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
            SELECT hash_salt, hashed_pw, username
            FROM USERS WHERE email = (?)
            ''', (email,))

        result = db.c.fetchone()
        hash_salt = result[0]
        correct_pw = result[1]
        username = result[2]

    pw_to_check = pw_hasher(supplied_pw + hash_salt)

    if pw_to_check == correct_pw:
        print(f'Welcome, {username}!')
    else:
        print('Incorrect email or password. Pleasse, try again.')
        login()
