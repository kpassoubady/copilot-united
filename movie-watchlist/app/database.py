from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base

DATABASE_URL = "sqlite:///./data/movies.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency for getting database sessions."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def save_movie_data(movie_data: dict):
    """Save movie data to the database."""
    from app.models import Movie
    db = SessionLocal()
    try:
        movie = Movie(
            title=movie_data.get("title"),
            description=movie_data.get("description"),
            year=movie_data.get("year"),
            genre=movie_data.get("genre")
        )
        db.add(movie)
        db.commit()
        db.refresh(movie)
        return movie
    finally:
        db.close()