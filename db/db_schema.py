CREATE_USERS = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username VARCHAR(20) NOT NULL,
        usertype VARCHAR(5), -- If type is client, leave as NULL, esle manually set to 'admin'
        email VARCHAR(50) UNIQUE NOT NULL,
        hash_salt VARCHAR(10) UNIQUE NOT NULL,
        hashed_pw VARCHAR(32)

    );
'''

CREATE_MOVIES = '''
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY,
        title VARCHAR(50),
        rating REAL
    );
'''

CREATE_PROJECTIONS = '''
    CREATE TABLE IF NOT EXISTS projections(
        id INTEGER PRIMARY KEY,
        date VARCHAR(10),
        time VARCHAR(5),
        type VARCHAR(3),
        movie_id INTEGER,
        floor_plan TEXT,
        FOREIGN KEY (movie_id) REFERENCES movies(id)
        ON DELETE CASCADE
    );
'''

CREATE_RESERVATIONS = '''
    CREATE TABLE IF NOT EXISTS reservations(
        id INTEGER PRIMARY KEY,
        row VARCHAR(1),
        seat INTEGER,
        user_id INTEGER,
        projection_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE,
        FOREIGN KEY (projection_id) REFERENCES projections(id)
        ON DELETE SET NULL
    );
'''

USER_SIGNUP = '''
    INSERT INTO users(email, username, hash_salt, hashed_pw)
    VALUES(?,?,?,?);
'''

ADD_MOVIE = '''
    INSERT INTO movies(title, rating)
    VALUES(?,?)
'''

LIST_MOVIES = '''
    SELECT * from movies
    ORDER BY rating DESC
'''

REMOVE_MOVIE = '''
    DELETE FROM movies WHERE id = (?)
'''

RESERVE = '''
    INSERT INTO reservations(row, seat, user_id, projection_id)
    VALUES(?,?,?,?)
'''

LIST_RESERVE = '''
    SELECT row || seat as seat, movies.title, projections.date, projections.time
    FROM reservations
    JOIN projections ON projections.id = reservations.projection_id
    JOIN movies ON movies.id = projections.movie_id
    WHERE user_id = (?);'''

CANCEL_RESERVE = 'DELETE FROM reservations WHERE id = (?)'

INIT_USERS = [
    (1, 'Georgi', 'admin', 'posta@cinema.bg', '^+azWpDOU-', '096bf77bd573efbed764747706a26f6c'),
    (2, 'Niki', 'admin', 'niki@cinema.bg', 'K_$>g6v&@U', '9d7d69533227e943b124f9657e9ff2f7'),
    (3, 'Pesho', None, 'peter@p.com', 'RnnoI3bt=s', 'c0bbc9f71095ee8cd50b6969fff8bc99')
]

INIT_MOVIES = [
    (1, 'Willow', 7.8),
    (2, 'Die Hard 2', 6.2),
    (3, 'O Brother, where art though?', 8.5)
]

INIT_PROJ = [
    (1, '2020-05-06', '10:00', '2D', 3, 100 * '.'),
    (2, '2020-05-06', '16:00', '4D', 1, 100 * '.'),
    (3, '2020-05-07', '09:00', '2D', 2, 100 * '.'),
    (4, '2020-05-07', '17:00', '2D', 3, 100 * '.'),
    (5, '2020-05-08', '11:00', '2D', 1, 100 * '.'),
    (6, '2020-05-08', '18:00', '3D', 2, 100 * '.')
]
