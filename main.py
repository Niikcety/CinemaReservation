# import ipdb
# from menu.model import MenuModel

# menu = MenuModel()
# menu.controller.db.create_tables()
# menu.controller.db.fill_tables()
# menu.start()
# menu.main_menu()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys
# from db.db_alchemy import User, Movie, Projection, Reservation

engine = create_engine('sqlite:///alchemy_cinema.db', echo=True)


class Menu():
    # def __init__(self):
    #     self.user_mocel = User()
    @classmethod
    def build(self):
        Base = declarative_base()
        Base.metadata.create_all(engine)


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Menu.build()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
