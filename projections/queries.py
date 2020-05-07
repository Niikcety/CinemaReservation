ADD_PROJECTION = '''
    INSERT INTO projections(date, time, type, movie_id) VALUES(?, ?, ?, ?)
'''

DELETE_PROJECTION = '''
    DELETE FROM projections WHERE id = (?)
'''

SHOW_ALL_PROJECTIONS = '''
    SELECT * FROM projections
'''

SHOW_PROJECTIONS_BY_FILM_ID = '''
    SELECT * FROM projections WHERE movie_id = (?)
'''

SHOW_PROJECTIONS_BY_FILM_ID_AND_DATE = '''
    SELECT * FROM projections WHERE movie_id = (?) AND date = (?)
'''

SHOW_ROOM_PLAN = '''
    SELECT floor_plan FROM projections WHERE id = (?)
'''