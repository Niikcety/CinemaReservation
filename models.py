from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import IntegrityError


engine = create_engine('sqlite:///alchemy_cinema.db', echo=True)
# Session is our Data Mapper
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    usertype = Column(String(5))
    email = Column(String(50), nullable=False, unique=True)
    hash_salt = Column(String(10), nullable=False, unique=True)
    hashed_pw = Column(String(32))


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    rating = Column(Float)


class Projection(Base):
    __tablename__ = 'projections'
    id = Column(Integer, primary_key=True)
    date = Column(String(10))
    time = Column(String(5))
    type = Column(String(3))
    movie_id = Column(Integer, ForeignKey(Movie.id))
    movie = relationship(Movie, backref="projections")
    floor_plan = Column(String)


class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True)
    row = Column(String(1))
    seat = Column(Integer)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User, backref='reservations')
    projection_id = Column(Integer, ForeignKey(Projection.id))
    projection = relationship(Projection, backref='projections')


def build_tables():
    Base.metadata.create_all(engine)


Users = [
    User(id=1, username='Georgi', usertype='admin', email='g@c.bg', hash_salt='^+azWpDOU-',
         hashed_pw='096bf77bd573efbed764747706a26f6c'),
    User(id=2, username='Niki', usertype='admin', email='n@c.bg', hash_salt='K_$>g6v&@U',
         hashed_pw='9d7d69533227e943b124f9657e9ff2f7'),
    User(id=3, username='Pesho', usertype=None, email='p@p.com', hash_salt='RnnoI3bt=s',
         hashed_pw='c0bbc9f71095ee8cd50b6969fff8bc99')
]

Movies = [
    Movie(id=1, title='Willow', rating=7.8),
    Movie(id=2, title='Die Hard 2', rating=6.2),
    Movie(id=3, title='O Brother, where art though?', rating=8.5)
]

Projections = [
    Projection(id=1, date='2020-05-06', time='10:00', type='2D', movie_id=3, floor_plan=100 * '.'),
    Projection(id=2, date='2020-05-06', time='16:00', type='4D', movie_id=1, floor_plan=100 * '.'),
    Projection(id=3, date='2020-05-07', time='09:00', type='2D', movie_id=2, floor_plan=100 * '.'),
    Projection(id=4, date='2020-05-07', time='17:00', type='2D', movie_id=3, floor_plan=100 * '.'),
    Projection(id=5, date='2020-05-08', time='11:00', type='2D', movie_id=1, floor_plan=100 * '.'),
    Projection(id=6, date='2020-05-08', time='18:00', type='3D', movie_id=2, floor_plan=100 * '.')
]

INIT_RECORDS = [Users, Movies, Projections]

def fill_tables():

    for records in INIT_RECORDS:
        try:
            session.add_all(records)
            session.commit()

        except IntegrityError:
            session.rollback()
        finally:
            session.close()
