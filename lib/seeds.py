from models import Artist, Song

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('sqlite:///data.db')
    Session = sessionmaker(bind=engine)  # enables communication with the db
    session = Session()

    session.query(Artist).delete() # Reset DB
    session.query(Song).delete() # Reset DB