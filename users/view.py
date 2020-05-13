from .controller import UserController


class UserView:
    def __init__(self):
        self.user_controller = UserController()

    def signup(self):
        print('Sign up!')
        email = input('Enter an email address: ')
        username = input('Enter username: ')
        pw = input('Enter a password: ')

        self.user_controller.signup(email, username, pw)

        # NEED TO BE CHECKED

    def login(self):
        print('Log in!')
        email = input('Enter your email address: ')

        supplied_pw = input('Enter your password: ')

        result = self.user_controller.login(email, supplied_pw)

        if result:
            print('You have been logged')
