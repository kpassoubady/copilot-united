from fastapi import FastAPI
from .database import init_db

app = FastAPI()

# Initialize the database
init_db()