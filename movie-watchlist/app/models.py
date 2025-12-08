from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    year = Column(Integer, nullable=True)
    genre = Column(String(100), nullable=True)
    tmdb_id = Column(Integer, nullable=True)  # For fetching artwork from fanart.tv

class Watchlist(Base):
    __tablename__ = 'watchlist'

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, nullable=False)
    user_notes = Column(Text, nullable=True)
    watched = Column(Integer, default=0)  # 0 = not watched, 1 = watched