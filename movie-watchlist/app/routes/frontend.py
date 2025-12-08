from fastapi import APIRouter, Request, Depends, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime

from app.database import get_db
from app.models import Movie, Watchlist
from app.services.movie_service import MovieService
from app.services.fanart_service import get_movie_poster, get_movie_thumbnail

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def get_context(request: Request, **kwargs):
    """Helper to create template context with common variables."""
    return {"request": request, "current_year": datetime.now().year, **kwargs}


def enrich_movie_with_poster(movie):
    """Add poster_url to a movie object."""
    poster_url = None
    if movie.tmdb_id:
        poster_url = get_movie_thumbnail(movie.tmdb_id) or get_movie_poster(movie.tmdb_id)
    return {
        "id": movie.id,
        "title": movie.title,
        "year": movie.year,
        "genre": movie.genre,
        "description": movie.description,
        "tmdb_id": movie.tmdb_id,
        "poster_url": poster_url
    }


@router.get("/", response_class=HTMLResponse, name="index")
async def home(
    request: Request,
    db: Session = Depends(get_db),
    search: Optional[str] = Query(None),
    genre: Optional[str] = Query(None),
    sort: Optional[str] = Query(None)
):
    """Home page showing all movies with search/filter/sort."""
    service = MovieService(db)
    movies = service.get_all_movies()
    
    # Get unique genres for filter dropdown
    genres = list(set(m.genre for m in movies if m.genre))
    genres.sort()
    
    # Apply search filter
    if search:
        movies = [m for m in movies if search.lower() in m.title.lower()]
    
    # Apply genre filter
    if genre:
        movies = [m for m in movies if m.genre and m.genre.lower() == genre.lower()]
    
    # Apply sorting
    if sort == "title":
        movies = sorted(movies, key=lambda m: m.title.lower())
    elif sort == "title_desc":
        movies = sorted(movies, key=lambda m: m.title.lower(), reverse=True)
    elif sort == "year":
        movies = sorted(movies, key=lambda m: m.year or 0)
    elif sort == "year_desc":
        movies = sorted(movies, key=lambda m: m.year or 0, reverse=True)
    
    # Enrich movies with poster URLs
    movies_with_posters = [enrich_movie_with_poster(m) for m in movies]
    
    return templates.TemplateResponse(
        "index.html",
        get_context(request, movies=movies_with_posters, genres=genres, search=search, selected_genre=genre, sort=sort)
    )


@router.get("/add", response_class=HTMLResponse, name="add_movie")
async def add_movie_page(request: Request):
    """Page to add a new movie."""
    return templates.TemplateResponse("add_movie.html", get_context(request))


@router.post("/add", response_class=HTMLResponse, name="add_movie_post")
async def add_movie_submit(
    request: Request,
    db: Session = Depends(get_db),
    title: str = Form(...),
    year: Optional[int] = Form(None),
    genre: Optional[str] = Form(None),
    description: Optional[str] = Form(None)
):
    """Handle add movie form submission."""
    service = MovieService(db)
    service.add_movie_simple(title=title, year=year, genre=genre, description=description)
    return RedirectResponse(url="/", status_code=303)


@router.get("/movie/{movie_id}", response_class=HTMLResponse, name="movie_detail")
async def movie_detail(request: Request, movie_id: int, db: Session = Depends(get_db)):
    """Movie details page."""
    service = MovieService(db)
    movie = service.get_movie_by_id(movie_id)
    if not movie:
        return templates.TemplateResponse(
            "error.html",
            get_context(request, message="Movie not found"),
            status_code=404
        )
    
    # Enrich movie with poster URL
    movie_data = enrich_movie_with_poster(movie)
    # Get full poster for detail page
    if movie.tmdb_id:
        movie_data["poster_url"] = get_movie_poster(movie.tmdb_id) or movie_data["poster_url"]
    
    # Check if movie is in watchlist
    watchlist_item = db.query(Watchlist).filter(Watchlist.movie_id == movie_id).first()
    in_watchlist = watchlist_item is not None
    
    return templates.TemplateResponse(
        "movie_detail.html",
        get_context(request, movie=movie_data, in_watchlist=in_watchlist, watchlist_item=watchlist_item)
    )


@router.post("/movie/{movie_id}/delete", name="delete_movie")
async def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    """Delete a movie."""
    service = MovieService(db)
    # Also remove from watchlist if present
    watchlist_item = db.query(Watchlist).filter(Watchlist.movie_id == movie_id).first()
    if watchlist_item:
        db.delete(watchlist_item)
        db.commit()
    service.delete_movie(movie_id)
    return RedirectResponse(url="/", status_code=303)


@router.get("/watchlist", response_class=HTMLResponse, name="watchlist")
async def watchlist_page(request: Request, db: Session = Depends(get_db)):
    """Watchlist page showing all saved movies."""
    watchlist_items = db.query(Watchlist).all()
    
    # Get movie details for each watchlist item
    service = MovieService(db)
    watchlist_with_movies = []
    for item in watchlist_items:
        movie = service.get_movie_by_id(item.movie_id)
        if movie:
            movie_data = enrich_movie_with_poster(movie)
            watchlist_with_movies.append({
                "id": item.id,
                "movie": movie_data,
                "user_notes": item.user_notes,
                "watched": item.watched if hasattr(item, 'watched') else False
            })
    
    return templates.TemplateResponse(
        "watchlist.html",
        get_context(request, watchlist=watchlist_with_movies)
    )


@router.post("/watchlist/add/{movie_id}", name="add_to_watchlist")
async def add_to_watchlist(
    movie_id: int,
    db: Session = Depends(get_db),
    user_notes: Optional[str] = Form(None)
):
    """Add a movie to the watchlist."""
    # Check if already in watchlist
    existing = db.query(Watchlist).filter(Watchlist.movie_id == movie_id).first()
    if not existing:
        new_item = Watchlist(movie_id=movie_id, user_notes=user_notes)
        db.add(new_item)
        db.commit()
    return RedirectResponse(url=f"/movie/{movie_id}", status_code=303)


@router.post("/watchlist/remove/{item_id}", name="remove_from_watchlist")
async def remove_from_watchlist(item_id: int, db: Session = Depends(get_db)):
    """Remove a movie from the watchlist."""
    item = db.query(Watchlist).filter(Watchlist.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return RedirectResponse(url="/watchlist", status_code=303)


@router.post("/watchlist/toggle-watched/{item_id}", name="toggle_watched")
async def toggle_watched(item_id: int, db: Session = Depends(get_db)):
    """Toggle watched status for a watchlist item."""
    item = db.query(Watchlist).filter(Watchlist.id == item_id).first()
    if item:
        item.watched = 0 if item.watched else 1
        db.commit()
    return RedirectResponse(url="/watchlist", status_code=303)


@router.post("/watchlist/update-notes/{item_id}", name="update_notes")
async def update_notes(
    item_id: int,
    db: Session = Depends(get_db),
    user_notes: str = Form("")
):
    """Update user notes for a watchlist item."""
    item = db.query(Watchlist).filter(Watchlist.id == item_id).first()
    if item:
        item.user_notes = user_notes
        db.commit()
    return RedirectResponse(url="/watchlist", status_code=303)
