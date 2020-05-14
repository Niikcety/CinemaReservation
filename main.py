# import ipdb
import sys
from models import build_tables, fill_tables
from view import View


if __name__ == '__main__':
    # ipdb.set_trace()
    try:
        command = sys.argv[1]
    except IndexError:
        print('Enter a command. ("build" or "start")')
        command = input()

    if command.lower() == 'build':
        build_tables()
        fill_tables()

    elif command.lower() == 'start':
        view = View()
        view.start()
    else:
        print(f'{command} is not a supported command. Try "build" or "start".')
