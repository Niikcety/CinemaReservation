from utils import salt_shaker, pw_hasher
from db import Database
from db_schema import (
    CREATE_USERS,
    CREATE_MOVIES,
    CREATE_PROJECTIONS,
    CREATE_RESERVATIONS,
    USER_SIGNUP)


db = Database()

with db.conn:
    db.c.execute(CREATE_USERS)
    db.c.execute(CREATE_MOVIES)
    db.c.execute(CREATE_PROJECTIONS)
    db.c.execute(CREATE_RESERVATIONS)
