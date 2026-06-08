from bson import ObjectId
from datetime import datetime

from fastapi import HTTPException
from app.database import books_collection, issues_collection

def issue_book(data, user_id):

    book_id = ObjectId(data.book_id)

    book = books_collection.find_one({"_id": book_id})

    if not book:
        raise Exception("Book not found")

    if book["available_copies"] <= 0:
        raise Exception("No copies left")

    issues_collection.insert_one({
        "user_id": user_id,      # keep as string OR ObjectId, but consistent
        "book_id": book_id,      # IMPORTANT: store ObjectId
        "issue_date": datetime.utcnow(),
        "status": "ISSUED"
    })

    books_collection.update_one(
        {"_id": book_id},
        {"$inc": {"available_copies": -1}}
    )

    return {"message": "Book issued"}

def return_book(data, user_id):

    book_id = ObjectId(data.book_id)

    result_issue = issues_collection.update_one(
        {
            "book_id": book_id,
            "user_id": user_id,
            "status": "ISSUED"
        },
        {
            "$set": {
                "status": "RETURNED",
                "return_date": datetime.utcnow()
            }
        }
    )

    if result_issue.modified_count == 0:
        raise HTTPException(status_code=400, detail="Already returned or not issued")

    books_collection.update_one(
        {"_id": book_id},
        {"$inc": {"available_copies": 1}}
    )

    return {"message": "Book returned successfully"}