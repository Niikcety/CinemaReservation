from .controllers import ProjectionController
from .utils import to_table
from .constants import COLS
from .utils import show_projection


class ProjectionsViews:
    def __init__(self):
        self.controller = ProjectionController()

    def add_projection(self):
        date = input('Enter date: ')
        time = input('Enter time: ')
        type = input('Enter type: ')
        movie_id = input('Enter movie_id: ')

        check = self.controller.create_projection(movie_id=movie_id, type=type, date=date, time=time)

        if check == 0:
            print('Couldn\'t add projection')
        else:
            print('Projection added')

    def remove_projection(self):
        id = input('Please enter the ID of the projection to remove: ')

        # CHECK IF RETURNED TRUE SHOW SUCCES MESSAGE
        self.controller.remove_projection(id)

    def list_projection(self):
        movie_id = input('Please enter the ID of the movie you want to watch: ')
        date = input('Please enter the date of the projection:  ')

        films = self.controller.list_projection(movie_id, date)
        show_projection(films)

    def list_projection_seat_plan(self, projection_id):
        room_tuple = self.controller.show_room_plan(projection_id)

        print(to_table(COLS, room_tuple))
