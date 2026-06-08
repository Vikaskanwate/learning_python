from app.core.config import database

def get_books_collection():
    return database["books"]