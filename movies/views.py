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

    def remove_movie(self):
        mid = input('Enter movie id: ')

        data = self.controller.remove_movie(mid)
        if data is not 0:
            movie_title = data[0]

            if data[1] == 0:
                print(f'\"{movie_title}\" wasn\'t removed from schedule.')
            else:
                print(f'\"{movie_title}\" removed from schedule.')
        else:
            print(f'There is no movie related to this id - {mid}')
