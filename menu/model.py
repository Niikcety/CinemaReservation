
from menu.controller import *
# from users.utils import *


class MenuModel():
    def __init__(self):
        self.user = None
        self.controller = MenuController()

    def start(self):
        print('''
Choose an option:
1. Sign up, if you don\'t have an account.
2. Log in, if you already do.''')
        choice = input()
        if choice == '1':
            self.user = self.controller.signup()
        elif choice == '2':
            self.user = self.controller.login()
        else:
            print('Enter a 1 or a 2.')
            self.start()

    def main_menu(self):

        while True:
            if self.user is None:
                self.start()

            elif self.user.tp == 'admin':
                pass
                # print(ADMIN_MENU)

            else:
                print('Choose an option.\n')
                print(CLIENT_MENU)
                choice = int(input())

                if choice == 6:
                    break

                elif choice in self.controller.client_commands:
                    self.controller.client_commands[choice]()
                else:
                    print(f'{choice} is not a recognized command. Please try again.')
