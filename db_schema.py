CREATE_USERS = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username VARCHAR(20) NOT NULL,
        usertype VARCHAR(5),
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
    INSERT INTO USERS(email, username, hash_salt, hashed_pw)
    VALUES(?,?,?,?);
'''
