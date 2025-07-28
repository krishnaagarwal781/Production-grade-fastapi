import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import purpose_collection

client = TestClient(app)

@pytest.fixture(autouse=True)
def clean_purpose_collection():
    # Clean up before each test
    purpose_collection.delete_many({})
    yield
    # Clean up after each test
    purpose_collection.delete_many({})

def test_create_and_get_purpose():
    data = {"name": "Analytics", "description": "Used for site analysis"}

    # Create purpose
    res = client.post("/purposes", json=data)
    assert res.status_code == 200
    res_json = res.json()
    assert "inserted_id" in res_json
    assert isinstance(res_json["inserted_id"], str)

    # Get purposes
    res = client.get("/purposes")
    assert res.status_code == 200
    all_purposes = res.json()
    assert any(p["name"] == "Analytics" and p["description"] == "Used for site analysis" for p in all_purposes)
