# Project 2: Python Task Manager (FastAPI) — macOS Install

This guide sets up a minimal FastAPI app with Jinja2 templates and SQLite on macOS.

## 1. Prerequisites

- Python 3.11+ (3.12 recommended)
- Homebrew installed (https://brew.sh)

Install and verify Python:

```bash
brew install python
python3 --version
pip3 --version
```

## 2. Create and activate a virtual environment

```bash
mkdir -p ~/copilot/project2 && cd ~/copilot/project2
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

Create `requirements.txt`:

```text
fastapi
uvicorn[standard]
sqlalchemy
alembic
jinja2
pydantic
python-multipart
passlib[bcrypt]
```

Install:

```bash
pip3 install -r requirements.txt
```

## 4. Scaffold a minimal app

Create folders:

```bash
mkdir -p app/templates app/static/css app/static/js
```

Create `app/main.py`:

```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to Python Task Manager!"})
```

Create `app/templates/index.html`:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Python Task Manager</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  </head>
  <body class="container py-5">
    <h1 class="mb-3">Python Task Manager</h1>
    <p class="lead">{{ message }}</p>
  </body>
  </html>
```

## 5. Run the dev server

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`

API docs:

```text
Swagger UI: http://127.0.0.1:8000/docs
ReDoc:      http://127.0.0.1:8000/redoc
```

## 6. VS Code extensions

- Python, Pylance, Jinja
- GitHub Copilot, GitHub Copilot Chat

## 7. Database URLs (SQLAlchemy)

```text
SQLite:      sqlite:///./task_manager.db
PostgreSQL:  postgresql+psycopg2://user:password@localhost:5432/task_manager
```
