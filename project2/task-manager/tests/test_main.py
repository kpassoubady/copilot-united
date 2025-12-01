# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "Python Task Manager" in response.text