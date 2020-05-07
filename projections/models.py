class ProjectionModel:
    def __init__(self, **kwargs):
        if len(kwargs) == 4:
            self.movie_id = kwargs[0]
            self.type = kwargs[1]
            self.date = kwargs[2]
            self.time = kwargs[3]

    @staticmethod
    def validate(movie_id, type, date, time):
        pass
