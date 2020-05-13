from .models import ProjectionModel
from .queries import *
from .utils import into_list_of_tuples
from db.db import Database
from .constants import ROWS, FLOOR


class ProjectionGateway:
    def __init__(self):
        self.model = ProjectionModel()
        self.db = Database()

    def create(self, movie_id, type, date, time):
        self.model.validate(movie_id, type, date, time)

        with self.db.conn:
            self.db.c.execute(ADD_PROJECTION, (date, time, type, movie_id, FLOOR))

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

    def check_if_projection_is_created(self, movie_id, type, date, time):
        with self.db.conn:
            self.db.c.execute(CHECK_IF_ADDED, (movie_id, type, date, time))
            data = self.db.c.fetchone()

        return data

    def check_if_projections_is_removed(self, movie_id):
        with self.db.conn:
            self.db.c.execute(SHOW_PROJECTIONS_BY_FILM_ID, (movie_id,))
            data = self.db.c.fetchone()

        return data

