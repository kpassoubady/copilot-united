from pydantic import BaseModel
from typing import Optional


class MovieBase(BaseModel):
    title: str
    year: Optional[int] = None
    genre: Optional[str] = None
    description: Optional[str] = None


class MovieCreate(MovieBase):
    pass


class MovieResponse(MovieBase):
    id: int

    class Config:
        from_attributes = True


class WatchlistBase(BaseModel):
    movie_id: int
    user_notes: Optional[str] = None


class WatchlistCreate(WatchlistBase):
    pass


class WatchlistResponse(WatchlistBase):
    id: int

    class Config:
        from_attributes = True
