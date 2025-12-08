# Movie Watchlist - Architecture Documentation

## Overview

The Movie Watchlist application is a full-stack web application built with FastAPI, SQLAlchemy, and Jinja2 templates. This document describes the system architecture, components, and their interactions.

## High-Level Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        Browser[Web Browser]
    end
    
    subgraph "Presentation Layer"
        Static[Static Files<br/>CSS/JS]
        Templates[Jinja2 Templates]
    end
    
    subgraph "Application Layer"
        FastAPI[FastAPI Application]
        
        subgraph "Routes"
            FrontendRoutes[Frontend Routes]
            MoviesAPI[Movies API]
            WatchlistAPI[Watchlist API]
        end
        
        subgraph "Services"
            MovieService[Movie Service]
            APIService[API Service]
        end
    end
    
    subgraph "Data Layer"
        SQLite[(SQLite Database)]
        ExternalAPI[External Movie API]
    end
    
    Browser --> FastAPI
    FastAPI --> Static
    FastAPI --> Templates
    FastAPI --> FrontendRoutes
    FastAPI --> MoviesAPI
    FastAPI --> WatchlistAPI
    FrontendRoutes --> MovieService
    MoviesAPI --> MovieService
    WatchlistAPI --> MovieService
    MovieService --> SQLite
    APIService --> ExternalAPI
    APIService --> SQLite
```

## Component Architecture

```mermaid
graph LR
    subgraph "app/"
        main[main.py<br/>FastAPI Entry Point]
        models[models.py<br/>SQLAlchemy Models]
        database[database.py<br/>DB Connection]
        schemas[schemas.py<br/>Pydantic Schemas]
        
        subgraph "routes/"
            movies_route[movies.py]
            watchlist_route[watchlist.py]
            frontend_route[frontend.py]
        end
        
        subgraph "services/"
            movie_svc[movie_service.py]
            api_svc[api_service.py]
        end
        
        subgraph "templates/"
            base_html[base.html]
            index_html[index.html]
            detail_html[movie_detail.html]
            watchlist_html[watchlist.html]
            add_html[add_movie.html]
        end
    end
    
    main --> movies_route
    main --> watchlist_route
    main --> frontend_route
    movies_route --> movie_svc
    watchlist_route --> movie_svc
    movie_svc --> models
    movie_svc --> database
    api_svc --> database
    frontend_route --> base_html
```

## Data Flow Diagram

```mermaid
sequenceDiagram
    participant User
    participant Browser
    participant FastAPI
    participant Routes
    participant Services
    participant Database
    participant ExternalAPI
    
    User->>Browser: Request Page
    Browser->>FastAPI: HTTP GET /
    FastAPI->>Routes: Route to Frontend
    Routes->>Services: Get Movies
    Services->>Database: Query Movies
    Database-->>Services: Movie Data
    Services-->>Routes: Movie List
    Routes->>FastAPI: Render Template
    FastAPI-->>Browser: HTML Response
    Browser-->>User: Display Page
    
    User->>Browser: Add Movie (Manual)
    Browser->>FastAPI: HTTP POST /api/movies
    FastAPI->>Routes: Movies API
    Routes->>Services: Add Movie
    Services->>Database: INSERT Movie
    Database-->>Services: Confirmation
    Services-->>Routes: Movie Object
    Routes-->>FastAPI: JSON Response
    FastAPI-->>Browser: Success
    
    User->>Browser: Fetch from API
    Browser->>FastAPI: HTTP GET /api/fetch
    FastAPI->>Routes: API Route
    Routes->>Services: Fetch Movie
    Services->>ExternalAPI: GET Movie Data
    ExternalAPI-->>Services: Movie JSON
    Services->>Database: Cache Data
    Services-->>Routes: Movie Object
    Routes-->>FastAPI: JSON Response
    FastAPI-->>Browser: Movie Data
```

## Database Schema

```mermaid
erDiagram
    MOVIE {
        int id PK
        string title
        text description
        int year
        string genre
    }
    
    WATCHLIST {
        int id PK
        int movie_id FK
        text user_notes
    }
    
    MOVIE ||--o{ WATCHLIST : "added to"
```

## Technology Stack

| Layer               | Technology   | Purpose                              |
| ------------------- | ------------ | ------------------------------------ |
| **Web Framework**   | FastAPI      | High-performance async web framework |
| **Template Engine** | Jinja2       | Server-side HTML rendering           |
| **ORM**             | SQLAlchemy   | Database abstraction and ORM         |
| **Database**        | SQLite       | Lightweight relational database      |
| **Styling**         | Tailwind CSS | Utility-first CSS framework          |
| **Interactivity**   | Alpine.js    | Lightweight JavaScript framework     |
| **HTTP Client**     | Requests     | External API communication           |
| **Server**          | Uvicorn      | ASGI server for FastAPI              |

## Directory Structure

```
movie-watchlist/
├── app/
│   ├── __init__.py           # App package init
│   ├── main.py               # FastAPI application entry point
│   ├── models.py             # SQLAlchemy ORM models
│   ├── database.py           # Database connection & session
│   ├── schemas.py            # Pydantic validation schemas
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── movies.py         # Movie CRUD API endpoints
│   │   ├── watchlist.py      # Watchlist API endpoints
│   │   └── frontend.py       # HTML page routes
│   ├── services/
│   │   ├── __init__.py
│   │   ├── movie_service.py  # Movie business logic
│   │   └── api_service.py    # External API integration
│   ├── templates/            # Jinja2 HTML templates
│   └── tests/                # Unit tests
├── static/
│   ├── css/styles.css        # Custom styles
│   └── js/app.js             # Frontend JavaScript
├── data/                     # SQLite database storage
├── docs/                     # Documentation
├── requirements.txt          # Python dependencies
└── README.md                 # Project readme
```

## API Endpoints

### Movies API (`/api/movies`)

| Method | Endpoint           | Description        |
| ------ | ------------------ | ------------------ |
| GET    | `/api/movies/`     | List all movies    |
| POST   | `/api/movies/`     | Create a new movie |
| DELETE | `/api/movies/{id}` | Delete a movie     |

### Watchlist API (`/api/watchlist`)

| Method | Endpoint          | Description             |
| ------ | ----------------- | ----------------------- |
| GET    | `/api/watchlist/` | Get all watchlist items |
| POST   | `/api/watchlist/` | Add movie to watchlist  |

### Frontend Routes

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | `/`            | Homepage          |
| GET    | `/movies/{id}` | Movie detail page |
| GET    | `/watchlist`   | Watchlist page    |
| GET    | `/add`         | Add movie form    |

## Key Design Decisions

1. **Server-Side Rendering**: Using Jinja2 templates for SEO-friendly pages and simpler state management.

2. **Service Layer Pattern**: Business logic is encapsulated in service classes, keeping routes thin and testable.

3. **SQLite Database**: Lightweight and file-based, perfect for single-user applications without external database setup.

4. **API-First Design**: All data operations go through REST APIs, enabling future frontend flexibility.

5. **Dependency Injection**: FastAPI's `Depends()` is used for database session management.
