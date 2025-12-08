from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import MovieResponse
from app.services.movie_service import MovieService

router = APIRouter()

@router.post("/movies/", response_model=MovieResponse)
def create_movie(title: str, director: str, year: int, genre: str, db: Session = Depends(get_db)):
    service = MovieService(db)
    return service.add_movie(title=title, director=director, year=year, genre=genre)

@router.get("/movies/", response_model=list[MovieResponse])
def read_movies(db: Session = Depends(get_db)):
    service = MovieService(db)
    return service.get_all_movies()

@router.delete("/movies/{movie_id}")
def remove_movie(movie_id: int, db: Session = Depends(get_db)):
    service = MovieService(db)
    success = service.delete_movie(movie_id=movie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted successfully"}