from app.database import get_db
from app.models import Movie, Watchlist
from sqlalchemy.orm import Session

class MovieService:
    def __init__(self, db: Session):
        self.db = db

    def add_movie(self, title: str, director: str, year: int, genre: str):
        # Note: director is ignored as it's not in the model
        new_movie = Movie(title=title, year=year, genre=genre)
        self.db.add(new_movie)
        self.db.commit()
        self.db.refresh(new_movie)
        return new_movie

    def add_movie_simple(self, title: str, year: int = None, genre: str = None, description: str = None):
        """Add a movie with all model fields."""
        new_movie = Movie(title=title, year=year, genre=genre, description=description)
        self.db.add(new_movie)
        self.db.commit()
        self.db.refresh(new_movie)
        return new_movie

    def get_all_movies(self):
        return self.db.query(Movie).all()

    def get_movie_by_id(self, movie_id: int):
        return self.db.query(Movie).filter(Movie.id == movie_id).first()

    def delete_movie(self, movie_id: int):
        movie_to_delete = self.db.query(Movie).filter(Movie.id == movie_id).first()
        if movie_to_delete:
            self.db.delete(movie_to_delete)
            self.db.commit()
            return True
        return False

    def cache_api_response(self, movie_data):
        for movie in movie_data:
            self.add_movie(movie['title'], movie['director'], movie['year'], movie['genre'])

    def add_movie_to_watchlist(self, movie_id: int, user_notes: str = None):
        # Check if movie exists
        movie = self.get_movie_by_id(movie_id)
        if not movie:
            raise ValueError(f"Movie with id {movie_id} not found")
        
        # Check if already in watchlist
        existing = self.db.query(Watchlist).filter(Watchlist.movie_id == movie_id).first()
        if existing:
            raise ValueError(f"Movie already in watchlist")
        
        new_item = Watchlist(movie_id=movie_id, user_notes=user_notes)
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)
        return new_item

    def get_watchlist_items(self):
        return self.db.query(Watchlist).all()