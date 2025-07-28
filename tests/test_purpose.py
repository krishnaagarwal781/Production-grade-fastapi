import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import purpose_collection

client = TestClient(app)

@pytest.fixture(autouse=True)
def clean_purpose_collection():
    # Clean up before and after each test
    purpose_collection.delete_many({})
    yield
    purpose_collection.delete_many({})

def test_create_and_get_purpose():
    data = {"name": "Analytics", "description": "Used for site analysis"}

    res = client.post("/purposes", json=data)
    assert res.status_code == 200
    inserted_id = res.json()["inserted_id"]

    res = client.get("/purposes")
    assert res.status_code == 200
    purposes = res.json()
    assert any(p["name"] == "Analytics" and p["description"] == "Used for site analysis" for p in purposes)

def test_get_purpose_by_id():
    data = {"name": "Marketing", "description": "Used for ads"}
    res = client.post("/purposes", json=data)
    inserted_id = res.json()["inserted_id"]

    res = client.get(f"/purposes/{inserted_id}")
    assert res.status_code == 200
    purpose = res.json()
    assert purpose["name"] == "Marketing"
    assert purpose["description"] == "Used for ads"

def test_update_purpose():
    data = {"name": "Research", "description": "Old desc"}
    res = client.post("/purposes", json=data)
    inserted_id = res.json()["inserted_id"]

    update_data = {"name": "Research Updated", "description": "New desc"}
    res = client.put(f"/purposes/{inserted_id}", json=update_data)
    assert res.status_code == 200
    assert res.json()["message"] == "Purpose updated successfully"

    res = client.get(f"/purposes/{inserted_id}")
    assert res.status_code == 200
    updated = res.json()
    assert updated["name"] == "Research Updated"
    assert updated["description"] == "New desc"

def test_delete_purpose():
    data = {"name": "Temp", "description": "To be deleted"}
    res = client.post("/purposes", json=data)
    inserted_id = res.json()["inserted_id"]

    res = client.delete(f"/purposes/{inserted_id}")
    assert res.status_code == 200
    assert res.json()["message"] == "Purpose deleted successfully"

    res = client.get(f"/purposes/{inserted_id}")
    assert res.status_code == 404
