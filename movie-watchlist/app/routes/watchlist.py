from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.schemas import WatchlistResponse
from app.services.movie_service import MovieService

router = APIRouter()
@router.post("/watchlist/", response_model=WatchlistResponse)
async def create_watchlist_item(movie_id: int, user_notes: Optional[str] = None, db: Session = Depends(get_db)):
    try:
        service = MovieService(db)
        return service.add_movie_to_watchlist(movie_id, user_notes)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/watchlist/", response_model=list[WatchlistResponse])
async def read_watchlist(db: Session = Depends(get_db)):
    try:
        service = MovieService(db)
        return service.get_watchlist_items()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))