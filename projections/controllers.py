from .gateway import ProjectionGateway


class ProjectionController:
    def __init__(self):
        self.projection_gateway = ProjectionGateway()

    def create_projection(self, id, movie_id, type, date, time):
        projection = self.projection_gateway.create(id=id, movie_id=movie_id, type=type, date=date, time=time)

        return projection
