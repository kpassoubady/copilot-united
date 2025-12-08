# Movie Watchlist Project

## Overview
The Movie Watchlist project is a single-user application designed to help users manage their movie watchlist. It allows for manual data entry when an API key is not available and caches API responses in an SQLite database. The application is built using FastAPI for the backend and utilizes Jinja2 for server-side rendering of templates. The frontend is styled with Tailwind CSS and includes interactivity powered by Alpine.js.

## Documentation
- 📐 [Architecture Diagram](docs/architecture.md) - System architecture, components, and data flow diagrams

## Features
- **Manual Data Entry**: Users can manually add movies to their watchlist when the API key is not present.
- **API Integration**: Fetch movie data from external APIs when an API key is available.
- **SQLite Caching**: Cache API responses in an SQLite database for efficient data retrieval.
- **Server-Side Rendering**: All pages are rendered on the server using Jinja2 templates.
- **Responsive Design**: The application is styled with Tailwind CSS for a modern and responsive user interface.

## Project Structure
```
movie-watchlist
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── movies.py
│   │   └── watchlist.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── movie_service.py
│   │   └── api_service.py
│   └── templates
│       ├── base.html
│       ├── index.html
│       ├── movie_detail.html
│       ├── watchlist.html
│       └── add_movie.html
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── app.js
├── data
│   └── .gitkeep
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd movie-watchlist
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the Application**:
   Open your browser and navigate to `http://localhost:8000`.

## Usage
- Navigate to the homepage to view the main features.
- Use the "Add Movie" page to manually enter movie details if the API key is not available.
- View your watchlist to see all added movies.
- Access detailed information about each movie from the watchlist.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.