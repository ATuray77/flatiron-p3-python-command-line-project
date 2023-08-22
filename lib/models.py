from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship



Base = declarative_base()

class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    nationality = Column(String)

    songs = relationship("Song", backref="artist") # relationship


    def __repr__(self):
        return f"\n<Artist" \
            + f"id={self.id}, " \
            + f"name={self.name}, " \
            + f"nationality={self.nationality}, " \
            + ">"


class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    category = Column(String)
    artist_id = Column(Integer, ForeignKey("artists.id"))

    #artists = relationship("Artist", backref="song") # Relationship


    def __repr__(self):
        return f"\n<Song" \
            + f"id={self.id}, " \
            + f"title={self.title}, " \
            + f"category={self.category}, " \
            + ">"