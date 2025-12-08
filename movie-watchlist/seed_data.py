"""Seed script to populate the database with sample movies and watchlist items."""

from app.database import SessionLocal, init_db
from app.models import Movie, Watchlist

# Sample movies data with TMDB IDs for fanart.tv integration
MOVIES = [
    {
        "title": "The Shawshank Redemption",
        "year": 1994,
        "genre": "Drama",
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "tmdb_id": 278
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "genre": "Action",
        "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        "tmdb_id": 155
    },
    {
        "title": "Inception",
        "year": 2010,
        "genre": "Sci-Fi",
        "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "tmdb_id": 27205
    },
    {
        "title": "Pulp Fiction",
        "year": 1994,
        "genre": "Crime",
        "description": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "tmdb_id": 680
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "genre": "Sci-Fi",
        "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "tmdb_id": 603
    },
    {
        "title": "Forrest Gump",
        "year": 1994,
        "genre": "Drama",
        "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75.",
        "tmdb_id": 13
    },
    {
        "title": "The Godfather",
        "year": 1972,
        "genre": "Crime",
        "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "tmdb_id": 238
    },
    {
        "title": "Interstellar",
        "year": 2014,
        "genre": "Sci-Fi",
        "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "tmdb_id": 157336
    },
    {
        "title": "Parasite",
        "year": 2019,
        "genre": "Thriller",
        "description": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
        "tmdb_id": 496243
    },
    {
        "title": "The Avengers",
        "year": 2012,
        "genre": "Action",
        "description": "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
        "tmdb_id": 24428
    },
    {
        "title": "Spirited Away",
        "year": 2001,
        "genre": "Animation",
        "description": "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.",
        "tmdb_id": 129
    },
    {
        "title": "The Silence of the Lambs",
        "year": 1991,
        "genre": "Thriller",
        "description": "A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer.",
        "tmdb_id": 274
    },
]

# Watchlist items (movie indices and notes)
WATCHLIST_ITEMS = [
    {"movie_index": 2, "user_notes": "Must watch this weekend!", "watched": 0},
    {"movie_index": 4, "user_notes": "Classic sci-fi - rewatch", "watched": 1},
    {"movie_index": 7, "user_notes": "Recommended by Sarah", "watched": 0},
    {"movie_index": 10, "user_notes": "Studio Ghibli marathon", "watched": 0},
]


def seed_database():
    """Seed the database with sample data."""
    # Initialize database tables
    init_db()
    
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing_movies = db.query(Movie).count()
        if existing_movies > 0:
            print(f"Database already has {existing_movies} movies. Skipping seed.")
            return
        
        # Add movies
        print("Adding movies...")
        movie_objects = []
        for movie_data in MOVIES:
            movie = Movie(**movie_data)
            db.add(movie)
            movie_objects.append(movie)
        
        db.commit()
        
        # Refresh to get IDs
        for movie in movie_objects:
            db.refresh(movie)
        
        print(f"Added {len(movie_objects)} movies.")
        
        # Add watchlist items
        print("Adding watchlist items...")
        for item_data in WATCHLIST_ITEMS:
            movie = movie_objects[item_data["movie_index"]]
            watchlist_item = Watchlist(
                movie_id=movie.id,
                user_notes=item_data["user_notes"],
                watched=item_data["watched"]
            )
            db.add(watchlist_item)
        
        db.commit()
        print(f"Added {len(WATCHLIST_ITEMS)} watchlist items.")
        
        print("\nSeed completed successfully!")
        print("\nMovies added:")
        for i, movie in enumerate(movie_objects, 1):
            print(f"  {i}. {movie.title} ({movie.year}) - {movie.genre}")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
