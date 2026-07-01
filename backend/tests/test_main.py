from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "service" in response.json()


def test_analyze_image():
    response = client.post("/analyze-image", json={"image": "test"})
    assert response.status_code == 200
    data = response.json()
    assert "objects" in data
    assert "text" in data
    assert "description" in data
