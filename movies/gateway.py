from db.db import Database
from db.db_schema import ADD_MOVIE, LIST_MOVIES, REMOVE_MOVIE
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

    def remove_movie(self, mid):
        with self.db.conn:
            self.db.c.execute('SELECT title FROM movies WHERE id = (?)', (mid,))
            movie_title = self.db.c.fetchone()

            self.db.c.execute(REMOVE_MOVIE, (mid,))

        if movie_title != None:
            return movie_title[0]
        else:
            return 0

    def check_if_movie_is_deleted(self, mid):
        with self.db.conn:
            self.db.c.execute('SELECT * FROM movies WHERE id = (?)', (mid,))
            movie = self.db.c.fetchone()

        return movie
