from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .session import session



class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    nationality = Column(String, nullable = False)

    songs = relationship("Song", backref="artist") # relationship


    def __repr__(self):
        return f"\n<Artist" \
            + f"id={self.id}, " \
            + f"name={self.name}, " \
            + f"nationality={self.nationality}, " \
            + ">"