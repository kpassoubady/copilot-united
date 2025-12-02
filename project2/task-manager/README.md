# Python Task Manager (FastAPI) — Starter

Minimal FastAPI starter with Jinja2 templates and SQLite-ready structure.

## Quick start

```bash
# macOS/zsh
cd project2/task-manager
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
uvicorn app.main:app --reload
```

```cmd
:: Windows (cmd)
cd project2\task-manager
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000` and try `http://127.0.0.1:8000/health`.

## Project layout

- `app/main.py`: FastAPI app with health and home routes
- `app/templates/index.html`: Bootstrap-backed minimal page
- `requirements.txt`: Dependencies matching course install guides
- `.gitignore`: Python caches, venv, and local DB files

## Running Tests (Optional)

```bash
# Run all tests
PYTHONPATH=. pytest -q

# Run a specific test file
PYTHONPATH=. pytest -q tests/test_main.py

# Verbose output
PYTHONPATH=. pytest -vv

# Stop on first failure
PYTHONPATH=. pytest -x

# With coverage report (requires pytest-cov)
pip install pytest-cov
PYTHONPATH=. pytest --cov=app --cov-report=term-missing
```

## Notes

- Default DB is SQLite (no setup needed). Example URL: `sqlite:///./task_manager.db`.
- For PostgreSQL, use `postgresql+psycopg2://user:password@localhost:5432/task_manager`.
  **Note:** If you switch to PostgreSQL, install the driver with `pip install psycopg2-binary`.
