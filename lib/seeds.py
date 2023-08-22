from models import Artist, Song

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data.db')

Session = sessionmaker(bind=engine)  # enables communication with the db
session = Session()