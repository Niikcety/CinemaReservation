class ProjectionModel:
    def __init__(self, id, movie_id, type, date, time):
        self.id = id
        self.movie_id = movie_id
        self.type = type
        self.date = date
        self.time = time

    @staticmethod
    def validate():
        pass
