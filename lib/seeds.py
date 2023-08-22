#!/usr/bin/env python3
from models import Artist, Song

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker

fake = Faker()

names = ["Sinach", "Bassey", "Eben", "Steve", ]


if __name__ == '__main__':
    engine = create_engine('sqlite:///data.db')
    Session = sessionmaker(bind=engine)  # enables communication with the db
    session = Session()

    session.query(Artist).delete() # Reset DB
    session.query(Song).delete() # Reset DB