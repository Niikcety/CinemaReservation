import ipdb
from menu.model import MenuModel

menu = MenuModel()
menu.controller.db.create_tables()
menu.controller.db.fill_tables()
menu.start()
menu.main_menu()
