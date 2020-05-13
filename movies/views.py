from .controllers import MovieController
from projections.utils import to_table


class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def add_movie(self):
        title = input('Enter title: ')
        rating = float(input('Enter rating: '))

        result = self.controller.add_movie(title, rating)

        if result:
            print(f'{title} added successfully!')
        else:
            print(f'{title} not added. Error occured')

    def list_movies(self):
        data = self.controller.list_movies()
        if data == 0:
            print('There are no movies to show')
        else:
            print(to_table(data[0], data[1], la=['title'], ra=['rating']))


    # def remove_movie():

    # mid = input('Enter movie id: ')

    # with db.conn:
    #     db.c.execute('SELECT title FROM movies WHERE id = (?)', (mid,))
    #     movie_title = db.c.fetchone()[0]

    #     db.c.execute(REMOVE_MOVIE, (mid,))

    # print(f'\"{movie_title}\" removed from schedule.')

