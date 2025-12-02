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

## 2. Recommended: use the included starter

The repo includes a ready-to-run starter at `project2/task-manager`.

```bash
cd project2/task-manager
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000` (docs at `/docs`).

## 3. Alternatively: scaffold manually

Create a project folder and venv:

```bash
mkdir -p ~/copilot/project2 && cd ~/copilot/project2
python3 -m venv .venv
source .venv/bin/activate
```

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

Create folders:

```bash
mkdir -p app/templates app/static/css app/static/js
```

Create `app/main.py` (uses file-relative paths and ensures folders exist):

```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import pathlib

app = FastAPI(title="Python Task Manager")

BASE_DIR = pathlib.Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

STATIC_DIR.mkdir(parents=True, exist_ok=True)
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

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

Run the dev server:

```bash
uvicorn app.main:app --reload
```

API docs:

```text
Swagger UI: http://127.0.0.1:8000/docs
ReDoc:      http://127.0.0.1:8000/redoc
```

## 4. VS Code extensions

- Python, Pylance, Jinja
- GitHub Copilot, GitHub Copilot Chat

## 5. Running Tests (Optional)

The starter includes a basic test suite using pytest.

```bash
# Install pytest (already in requirements.txt)
pip3 install pytest

# Run all tests
PYTHONPATH=. pytest -q

# Verbose output
PYTHONPATH=. pytest -vv

# Stop on first failure
PYTHONPATH=. pytest -x

# With coverage report (requires pytest-cov)
pip3 install pytest-cov
PYTHONPATH=. pytest --cov=app --cov-report=term-missing
```

## 6. Database URLs (SQLAlchemy)

- Default is SQLite (no setup needed):
  ```text
  sqlite:///./task_manager.db
  ```

- **Optional:** For PostgreSQL, install the driver and use:
  ```bash
  pip3 install psycopg2-binary
  ```
  ```text
  postgresql+psycopg2://user:password@localhost:5432/task_manager
  ```
