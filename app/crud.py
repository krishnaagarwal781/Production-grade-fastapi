from app.db import purpose_collection


def create_purpose(data: dict):
    inserted_id = purpose_collection.insert_one(data).inserted_id
    return str(inserted_id)


def get_all_purposes():
    purposes = list(purpose_collection.find({}))
    for purpose in purposes:
        purpose["_id"] = str(purpose["_id"])
    return purposes
