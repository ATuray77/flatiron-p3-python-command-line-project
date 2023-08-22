from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///songLibrary.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, Primary_key = True)
    name = Column(String)
    nationality = Column(String)
    songs = relationship("song", backref="artist")


    def __repr__(self):
        return f"\n<Owner" \
            + f"id={self.id}, " \
            + f"name={self.name}, " \
            + f"nationality={self.nationality}, " \
            + ">"


class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, Prinary_key = True)
    title = Column(String)
    category = Column(String)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    artists = relationship("artist", backref="song")


    def __repr__(self):
        return f"\n<Song" \
            + f"id={self.id}, " \
            + f"title={self.title}, " \
            + f"category={self.category}, " \
            + ">"