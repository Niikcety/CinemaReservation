import sqlite3
from settings import DB_NAME


class Database():
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()
