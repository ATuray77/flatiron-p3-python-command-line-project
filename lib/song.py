from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    category = Column(String, nullable = False)
    artist_id = Column(Integer, ForeignKey("artists.id"))



    def __repr__(self):
        return f"\n<Song" \
            + f"id={self.id}, " \
            + f"title={self.title}, " \
            + f"category={self.category}, " \
            + ">"