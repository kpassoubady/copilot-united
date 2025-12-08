"""Service for fetching movie artwork from fanart.tv API."""

import urllib.request
import urllib.error
import json
from typing import Optional
from functools import lru_cache

FANART_API_KEY = "b1e0a3eea6137f0fb94776a31c0ec4ea"
FANART_BASE_URL = "https://webservice.fanart.tv/v3"


@lru_cache(maxsize=100)
def get_movie_artwork(tmdb_id: int) -> Optional[dict]:
    """
    Fetch movie artwork from fanart.tv API.
    
    Args:
        tmdb_id: The TMDB ID of the movie
        
    Returns:
        Dict with artwork URLs or None if not found
    """
    if not tmdb_id:
        return None
    
    url = f"{FANART_BASE_URL}/movies/{tmdb_id}?api_key={FANART_API_KEY}"
    
    try:
        request = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(request, timeout=5) as response:
            data = json.loads(response.read().decode())
            return data
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, TimeoutError) as e:
        print(f"Error fetching fanart for TMDB ID {tmdb_id}: {e}")
        return None


def get_movie_poster(tmdb_id: int) -> Optional[str]:
    """
    Get the best available movie poster URL.
    
    Args:
        tmdb_id: The TMDB ID of the movie
        
    Returns:
        URL string of the poster or None
    """
    artwork = get_movie_artwork(tmdb_id)
    if not artwork:
        return None
    
    # Try to get poster in order of preference
    # 1. movieposter (official posters)
    # 2. hdmovielogo (HD logos)
    # 3. moviethumb (thumbnails)
    # 4. moviebackground (backgrounds)
    
    if "movieposter" in artwork and artwork["movieposter"]:
        return artwork["movieposter"][0].get("url")
    
    if "hdmovielogo" in artwork and artwork["hdmovielogo"]:
        return artwork["hdmovielogo"][0].get("url")
    
    if "moviethumb" in artwork and artwork["moviethumb"]:
        return artwork["moviethumb"][0].get("url")
    
    if "moviebackground" in artwork and artwork["moviebackground"]:
        return artwork["moviebackground"][0].get("url")
    
    return None


def get_movie_thumbnail(tmdb_id: int) -> Optional[str]:
    """
    Get a movie thumbnail URL (smaller image for grid view).
    
    Args:
        tmdb_id: The TMDB ID of the movie
        
    Returns:
        URL string of the thumbnail or None
    """
    artwork = get_movie_artwork(tmdb_id)
    if not artwork:
        return None
    
    # Prefer thumbnails for grid view, then posters
    if "moviethumb" in artwork and artwork["moviethumb"]:
        return artwork["moviethumb"][0].get("url")
    
    if "movieposter" in artwork and artwork["movieposter"]:
        return artwork["movieposter"][0].get("url")
    
    return None


def get_movie_background(tmdb_id: int) -> Optional[str]:
    """
    Get a movie background/banner URL.
    
    Args:
        tmdb_id: The TMDB ID of the movie
        
    Returns:
        URL string of the background or None
    """
    artwork = get_movie_artwork(tmdb_id)
    if not artwork:
        return None
    
    if "moviebackground" in artwork and artwork["moviebackground"]:
        return artwork["moviebackground"][0].get("url")
    
    return None
