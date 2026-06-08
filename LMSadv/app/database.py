from pymongo import MongoClient
from app.config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["library_db"]

users_collection = db["users"]
books_collection = db["books"]
issues_collection = db["issues"]