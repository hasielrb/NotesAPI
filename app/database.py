from pymongo import MongoClient
from core.config import settings

client = MongoClient(settings.DATABASE_URL)
db_name = client.api_notes

users_collection = db_name.users
notes_collection = db_name.notes