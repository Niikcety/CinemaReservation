from .gateway import MovieGateway


class MovieController():
    def __init__(self):
        self.movie_gateway = MovieGateway()

    def add_movie(self, title, rating):
        self.movie_gateway.add_movie(title, rating)

        # CHECK IF IT WAS SAVED
        return True

    def list_movies(self):
        data = self.movie_gateway.list_movies()
        if len(data[1]) == 0:
            return 0
        else:
            return data

    def remove_movie(self, mid):
        title = self.movie_gateway.remove_movie(mid)
        if title is 0:
            return 0

        check_if_deleted = self.movie_gateway.check_if_movie_is_deleted(mid)

        return (title, check_if_deleted)
