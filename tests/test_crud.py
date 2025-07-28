import pytest
from unittest.mock import MagicMock
from app.crud import create_purpose, get_all_purposes
from app.models import Purpose
from bson import ObjectId


# Mock the database collection globally for these unit tests
@pytest.fixture
def mock_purpose_collection(mocker):
    # This will replace the actual purpose_collection with a mock object
    # located where it's used in app.crud.
    # We are patching 'app.crud.purpose_collection' because that's the
    # reference that functions in app.crud use.
    mock_collection = mocker.patch(
        "app.crud.purpose_collection"
    )  # <--- FIX: Patch where it's used
    yield mock_collection
    # You might want to reset the mock after each test if needed,
    # though mocker.patch usually handles cleanup automatically per test.


def test_create_purpose_unit(mock_purpose_collection):
    test_data = {"name": "Test Unit", "description": "Unit test purpose"}
    # Configure the mock to return a specific InsertOneResult
    # PyMongo's insert_one returns an object with an 'inserted_id' attribute
    mock_purpose_collection.insert_one.return_value = MagicMock()
    mock_purpose_collection.insert_one.return_value.inserted_id = "mock_id_123"

    # Call the crud function. It expects a dictionary.
    # So, convert the Pydantic model to a dictionary using .model_dump()
    purpose_model = Purpose(**test_data)
    result_id = create_purpose(purpose_model.model_dump())

    # Assert that insert_one was called with the correct dictionary
    mock_purpose_collection.insert_one.assert_called_once_with(test_data)
    assert result_id == "mock_id_123"


def test_get_all_purposes_unit(mock_purpose_collection):
    # Mock data as it would come directly from MongoDB, including ObjectId
    mock_data_from_db = [
        {
            "name": "P1",
            "description": "Desc1",
            "_id": ObjectId("60c72b2f9b1e8b001c8e4d1a"),
        },
        {
            "name": "P2",
            "description": "Desc2",
            "_id": ObjectId("60c72b2f9b1e8b001c8e4d1b"),
        },
    ]
    # Configure the mock for .find() to return a mock object that can be iterated over.
    # The list() call in crud.py will iterate over this mock.
    mock_cursor = MagicMock()
    mock_cursor.__iter__.return_value = iter(mock_data_from_db)
    mock_purpose_collection.find.return_value = mock_cursor

    purposes = get_all_purposes()

    # Assert that find was called with only the query argument, as per your crud.py
    mock_purpose_collection.find.assert_called_once_with(
        {}
    )  # <--- FIX: Removed projection argument

    # The get_all_purposes function converts "_id" to string, so assert against that format
    expected_purposes = [
        {"name": "P1", "description": "Desc1", "_id": "60c72b2f9b1e8b001c8e4d1a"},
        {"name": "P2", "description": "Desc2", "_id": "60c72b2f9b1e8b001c8e4d1b"},
    ]
    assert purposes == expected_purposes
