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

LIST_RESERvE = '''
    SELECT row || seat as seat, movies.title, projections.date, projections.time
    FROM reservations
    JOIN projections ON projections.id = reservations.projection_id
    JOIN movies ON movies.id = projections.movie_id;
    '''
