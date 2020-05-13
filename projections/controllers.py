from .gateway import ProjectionGateway
from .utils import show_projection


class ProjectionController:
    def __init__(self):
        self.projection_gateway = ProjectionGateway()

    def create_projection(self, movie_id, type, date, time):
        self.projection_gateway.create(movie_id=movie_id, type=type, date=date, time=time)
        check = self.projection_gateway.check_if_projection_is_created(movie_id, type, date, time)

        if check is ():
            return 0
        else:
            return 1

    def remove_projection(self, id):
        projection = self.projection_gateway.remove_projection(id)

        return projection

    def list_projection(self, id, date):
        if date == '':
            films = self.projection_gateway.list_projection(id, None)
        else:
            films = self.projection_gateway.list_projection(id, date)
        return films

    def show_room_plan(self, id):
        room = self.projection_gateway.show_room_plan(id)

        return room
