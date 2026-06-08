from app.database import books_collection

def add_book(book):
    book_dict = book.dict()
    book_dict["available_copies"] = book.total_copies
    books_collection.insert_one(book_dict)
    return {"message": "Book added"}

def get_books():
    books = []
    for b in books_collection.find():
        b["_id"] = str(b["_id"])
        books.append(b)
    return books

def delete_book(title):
    books_collection.delete_one({"title": title})
    return {"message": "Book deleted"}