from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_comment():
    response = client.post("/comments/", json={"task": "Test Task", "text": "Test comment"})
    assert response.status_code == 200
    assert response.json()["task"] == "Test Task"

def test_get_comments():
    response = client.get("/comments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
