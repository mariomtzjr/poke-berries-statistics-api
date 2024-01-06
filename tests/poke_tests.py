import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_berries_data():
    response = client.get("/berries/allBerryStats")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    
    expected_result = {"name": "cheri", "flavor": "spicy"}
    assert response.json() == expected_result