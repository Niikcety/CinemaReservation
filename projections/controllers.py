from .gateway import ProjectionGateway


class ProjectionController:
    def __init__(self):
        self.projection_gateway = ProjectionGateway()

    def create_projection(self, movie_id, type, date, time):
        self.projection_gateway.create(movie_id=movie_id, type=type, date=date, time=time)
        check = self.projection_gateway.check_if_projection_is_created(movie_id, type, date, time)

        if check is None:
            return 0
        else:
            return 1

    def remove_projection(self, movie_id):
        self.projection_gateway.remove_projection(movie_id)
        result = self.projection_gateway.check_if_projections_is_removed(movie_id)

        if result is None:
            return 0
        else:
            return 1

    def list_projection(self, movie_id, date):
        if date == '':
            films = self.projection_gateway.list_projection(movie_id, None)
        else:
            films = self.projection_gateway.list_projection(movie_id, date)
        return films

    def show_room_plan(self, movie_id):
        room = self.projection_gateway.show_room_plan(movie_id)

        return room
