from fastapi import HTTPException
import requests
from app.database import get_db, save_movie_data

class APIService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def fetch_movie_data(self, movie_title: str):
        if not self.api_key:
            raise HTTPException(status_code=400, detail="API key is not provided.")
        
        url = f"https://api.example.com/movies?title={movie_title}&api_key={self.api_key}"
        response = requests.get(url)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching movie data.")

        movie_data = response.json()
        save_movie_data(movie_data)
        return movie_data

    def get_movie_details(self, movie_id: str):
        # This method can be used to fetch details of a specific movie if needed
        pass

    def cache_movie_data(self, movie_data):
        db = get_db()
        # Logic to cache movie data in SQLite
        pass