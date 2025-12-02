# Project 2: Python Task Manager (FastAPI) — Windows Install

This guide sets up a minimal FastAPI app with Jinja2 templates and SQLite on Windows 11.

## 1. Install Python and verify

Download from <https://www.python.org/downloads/> and during setup:

- Check “Add Python to PATH”
- Choose “Customize installation” and keep pip enabled

Verify:

```cmd
python --version
pip --version
```

Optional (upgrade pip):

```cmd
python -m pip install --upgrade pip
```

## 2. Recommended: use the included starter

The repo includes a ready-to-run starter at `project2\task-manager`.

```cmd
cd project2\task-manager
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000` (docs at `/docs`).

## 3. Alternatively: scaffold manually

Create a project directory and venv:

```cmd
mkdir %USERPROFILE%\copilot\project2
cd %USERPROFILE%\copilot\project2
python -m venv .venv
.venv\Scripts\activate
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

```cmd
pip install -r requirements.txt
```

Create folders:

```cmd
mkdir app\templates app\static\css app\static\js
```

Create `app\main.py` (PowerShell example; uses file-relative paths and ensures folders exist):

```powershell
@"
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
"@ | Out-File -Encoding utf8 app\main.py
```

Create `app\templates\index.html`:

```powershell
@"
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
"@ | Out-File -Encoding utf8 app\templates\index.html
```

## 4. Run the dev server

```cmd
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`

API docs:

```text
Swagger UI: http://127.0.0.1:8000/docs
ReDoc:      http://127.0.0.1:8000/redoc
```

## 5. VS Code extensions

- Python (Microsoft) — Python language support
- Pylance — Fast Python language server
- Jinja — Syntax highlighting for Jinja2 templates
- GitHub Copilot — AI-powered code suggestions
- GitHub Copilot Chat — Interactive AI assistance

## 6. Running Tests (Optional)

The starter includes a basic test suite using pytest.

```cmd
:: Install pytest (already in requirements.txt)
pip install pytest

:: Run all tests
set PYTHONPATH=. && pytest -q

:: Verbose output
set PYTHONPATH=. && pytest -vv

:: Stop on first failure
set PYTHONPATH=. && pytest -x

:: With coverage report (requires pytest-cov)
pip install pytest-cov
set PYTHONPATH=. && pytest --cov=app --cov-report=term-missing
```

## 7. Database URLs (SQLAlchemy)

- Default is SQLite (no setup needed):

  ```text
  sqlite:///./task_manager.db
  ```

- **Optional:** For PostgreSQL, install the driver and use:

  ```cmd
  pip install psycopg2-binary
  ```

  ```text
  postgresql+psycopg2://user:password@localhost:5432/task_manager
  ```
