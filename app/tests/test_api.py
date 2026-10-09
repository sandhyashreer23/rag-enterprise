from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_ask():
    response = client.post("/ask", json={"question": "hi"})

    assert response.status_code == 200
    assert response.json()["answer"] == "You asked: hi"    