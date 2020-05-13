from . gateway import UserGateway
from .utils import salt_shaker, pw_hasher


class UserController:
    def __init__(self):
        self.user_gateway = UserGateway()

    def signup(self, email, username, pw):
        hash_salt = salt_shaker()
        hashed_pw = pw_hasher(pw + hash_salt)

        self.user_gateway.signup(email, username, hash_salt, hashed_pw)

    def login(self, email, pw):
        result = self.user_gateway.login(email)
        salt = result[0]
        hashed_pw = result[1]

        pw_to_check = pw_hasher(pw + salt)

        return pw_to_check == hashed_pw
