from fastapi.testclient import TestClient
from meetings.main import app

client = TestClient(app)


def test_extracts_known_skills():
    payload = client.post("/extract", json={"text": 'Owner will rollback if the error budget is spent.'}).json()
    assert "rollback" in payload["skills"]


def test_empty_is_refused():
    assert client.post("/extract", json={"text": ""}).status_code == 422
