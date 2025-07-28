from app.db import purpose_collection
from bson import ObjectId


def create_purpose(data: dict):
    inserted_id = purpose_collection.insert_one(data).inserted_id
    return str(inserted_id)


def get_all_purposes():
    purposes = list(purpose_collection.find({}))
    for purpose in purposes:
        purpose["_id"] = str(purpose["_id"])
    return purposes


def get_purpose_by_id(purpose_id: str):
    purpose = purpose_collection.find_one({"_id": ObjectId(purpose_id)})
    if purpose:
        purpose["_id"] = str(purpose["_id"])
    return purpose


def update_purpose(purpose_id: str, data: dict):
    result = purpose_collection.update_one(
        {"_id": ObjectId(purpose_id)}, {"$set": data}
    )
    return result.modified_count


def delete_purpose(purpose_id: str):
    result = purpose_collection.delete_one({"_id": ObjectId(purpose_id)})
    return result.deleted_count
