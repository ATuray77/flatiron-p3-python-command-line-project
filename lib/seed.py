from models import Artist, Song

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random


#if __name__ == '__main__':
engine = create_engine('sqlite:///songLibrary.db')
Session = sessionmaker(bind=engine)  # enables communication with the db
session = Session()

session.query(Artist).delete() # Reset DB
session.query(Song).delete() # Reset DB
session.commit()

fake = Faker()

names = ["Sinach", "Bassey", "Eben", "Steve", "Grace"]
nationalities = ["Nigerian", "Ghanian", "South African", "American", "Kenyan"]

artists = []
for i in range(5):
    artist = Artist(
        name = random.choice(names),
        nationality = random.choice(nationalities)
        )
    artists.append(artist)
session.add_all(artists)
session.commit()
print(artists)
print(artists[1].id)

titles = ["Way Maker", "Kadosh", "You are Powerful", "Goodness", "Happily!"]
categories = ["praise", "worship"]

music = []
for n in range(5):
    print(artists[n].id)
    song = Song(
        artist_id = artists[n].id,
        title = random.choice(titles),
        category = random.choice(categories)
        )

#session.bulk_save_objects(songs, artist)
    music.append(song)
session.add_all(music)
session.commit()
session.close()

