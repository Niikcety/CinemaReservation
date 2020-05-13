from db.db import Database
from db.db_schema import ADD_MOVIE, LIST_MOVIES
from .models import MovieModel


class MovieGateway:
    def __init__(self):
        self.model = MovieModel()
        self.db = Database()

    def add_movie(self, title, rating):
        with self.db.conn:
            self.db.c.execute(ADD_MOVIE, (title, rating))

    def list_movies(self):
        with self.db.conn:
            self.db.c.execute(LIST_MOVIES)
            cols = [cd[0] for cd in self.db.c.description]
            rows = self.db.c.fetchall()

        return (cols, rows)
