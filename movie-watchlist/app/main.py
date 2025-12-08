from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import movies, watchlist
from app.routes.frontend import router as frontend_router
from app.database import init_db

app = FastAPI(title="Movie Watchlist", description="A movie watchlist application")

# Initialize the database
init_db()

# Serve static files first (before routes)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include API routes with prefix
app.include_router(movies.router, prefix="/api", tags=["Movies API"])
app.include_router(watchlist.router, prefix="/api", tags=["Watchlist API"])

# Include frontend routes (no prefix - serves HTML pages)
app.include_router(frontend_router, tags=["Frontend"])