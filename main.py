from menu.model import MenuModel
from reservations.view import ReservationView


menu = MenuModel()
menu.controller.db.create_tables()
menu.controller.db.fill_tables()
# menu.start()
# menu.main_menu()

res = ReservationView()
res.list_reservations()
