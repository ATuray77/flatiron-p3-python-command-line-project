#!/usr/bin/env python3
from models import Artist, Song

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random


if __name__ == '__main__':
    engine = create_engine('sqlite:///data.db')
    Session = sessionmaker(bind=engine)  # enables communication with the db
    session = Session()

    session.query(Artist).delete() # Reset DB
    session.query(Song).delete() # Reset DB

fake = Faker()

names = ["Sinach", "Bassey", "Eben", "Steve", "Grace"]
nationalities = ["Nigerian", "Ghanian", "South African", "American", "Kenyan"]

artists = []
for i in range(5):
    artist = Artist(
       name = random.choice(names),
       nationality = random.choice(nationalities)
    )
    
    session.add(artist)
    session.commit()

categories = ["praise", "worship"]

artists.append(artist)

songs = []
for song in songs:
    song = Song(
        title = fake.unique.name(),
        category = random.choice(categories)
    )

songs.append(song)

