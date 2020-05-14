from db.db import Database
from models import User
from db.db_schema import USER_SIGNUP


class UserGateway:
    def __init__(self):
        self.db = Database()
        self.model = User()

    def signup(self, email, username, hash_salt, hashed_pw):
        with self.db.conn:
            self.db.c.execute(USER_SIGNUP, (email, username, hash_salt, hashed_pw))

    def login(self, email):
        with self.db.conn:
            self.db.c.execute('SELECT hash_salt, hashed_pw FROM users WHERE email = (?)', (email,))
            result = self.db.c.fetchone()

        return result
