from .models import ProjectionModel
from .queries import *
from .utils import into_list_of_tuples
from db import Database
from .constants import ROWS


class ProjectionGateway:
    def __init__(self):
        self.model = ProjectionModel()
        self.db = Database()

    def create(self, movie_id, type, date, time):
        self.model.validate(movie_id, type, date, time)

        with self.db.conn:
            self.db.c.execute(ADD_PROJECTION, (date, time, type, movie_id))

    def remove_projection(self, id):
        with self.db.conn:
            self.db.c.execute(DELETE_PROJECTION, (id,))

    def list_projection(self, movie_id, date=None):
        with self.db.conn:
            if date is None:
                self.db.c.execute(SHOW_PROJECTIONS_BY_FILM_ID, (movie_id,))
            else:
                self.db.c.execute(SHOW_PROJECTIONS_BY_FILM_ID_AND_DATE, (movie_id, date))
            films = self.db.c.fetchall()

        return films

    def show_room_plan(self, projection_id):
        with self.db.conn:
            self.db.c.execute(SHOW_ROOM_PLAN, (projection_id,))
            room = self.db.c.fetchall()
        return into_list_of_tuples(room, ROWS)
