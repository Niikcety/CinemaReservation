from .controllers import ProjectionController


class ProjectionsViews:
    def __init__(self):
        self.controller = ProjectionController()

    def add_projection(self):
        id = input('Enter id: ')
        movie_id = input('Enter movie_id: ')
        type = input('Enter type: ')
        date = input('Enter date: ')
        time = input('Enter time: ')

        self.controller.create_projection(id=id, movie_id=movie_id, type=type, date=date, time=time)

    def remove_projection(self):
        pass

    def list_projection(self):
        pass

    def list_projection_seat_plan(self):
        pass
