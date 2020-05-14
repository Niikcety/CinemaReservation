from db.db_alchemy import Base, engine
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    usertype = Column(String(5))
    email = Column(String(50), nullable=False, unique=True)
    hash_salt = Column(String(10), nullable=False, unique=True)
    hashed_pw = Column(String(32))

    def build_table(self):
        Base.metadata.create_all(engine)
