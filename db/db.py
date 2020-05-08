import sqlite3
from db.db_schema import *


class Database():
    def __init__(self):
        self.conn = sqlite3.connect('cinema.db')
        self.c = self.conn.cursor()

    def create_tables(self):
        with self.conn:
            self.c.execute(CREATE_USERS)
            self.c.execute(CREATE_MOVIES)
            self.c.execute(CREATE_PROJECTIONS)
            self.c.execute(CREATE_RESERVATIONS)

    def fill_tables(self):
        with self.conn:
            try:
                self.c.executemany('''
                    INSERT INTO users(id, username, usertype, email, hash_salt, hashed_pw)
                    VALUES(?,?,?,?,?,?)''', INIT_USERS)
            except Exception:
                pass

            try:
                self.c.executemany('''
                    INSERT INTO movies(id, title, rating)
                    VALUES(?,?,?)''', INIT_MOVIES)
            except Exception:
                pass

            try:
                self.c.executemany('''
                    INSERT INTO projections(id, date, time, type, movie_id, floor_plan)
                    VALUES(?,?,?,?,?,?)''', INIT_PROJ)
            except Exception:
                pass
