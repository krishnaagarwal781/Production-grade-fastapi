from pymongo import MongoClient
from app.config import settings

client = MongoClient(settings.MONGO_URI)

# Choose DB based on ENV
db_name = {
    "development": "cmp_dev",
    "testing": "cmp_test",
    "production": "cmp"
}.get(settings.ENV, "cmp_dev")

db = client[db_name]
purpose_collection = db["purposes"]
