from .views import ProjectionModel
from .queries import CREATE_PROJECTION
import db
import sys
sys.path.append('..')


class ProjectionGateway:
    def __init__(self):
        self.model = ProjectionModel()
        self.db = Database()

    def create(self, id, movie_id, type, date, time):
        self.model.validate(id, movie_id, type, date, time)

        self.db.cursor.execute(CREATE_PROJECTION, (id, movie_id, type, date, time))

    def remove_projection():
        pass

    def list_projection():
        pass
