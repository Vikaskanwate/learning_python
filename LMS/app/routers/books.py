from fastapi import APIRouter, HTTPException, status, Body
from app.database.collections import get_books_collection
from app.schemas.book import BookCreate, BookResponse, BookUpdate
from bson import ObjectId
from typing import List

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate = Body(...)):
    collection = get_books_collection()
    book_dict = book.model_dump()
    
    # Insert document into MongoDB
    new_book = await collection.insert_one(book_dict)
    
    # Fetch the inserted document
    created_book = await collection.find_one({"_id": new_book.inserted_id})
    return created_book

@router.get("/", response_model=List[BookResponse])
async def get_all_books():
    collection = get_books_collection()
    # Motor returns a cursor; wrap it in to_list
    books = await collection.find().to_list(length=100)
    return books

@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: str):
    collection = get_books_collection()
    if not ObjectId.is_valid(book_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
        
    book = await collection.find_one({"_id": ObjectId(book_id)})
    if book is None:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
    return book

@router.put("/{book_id}", response_model=BookResponse)
async def update_book(book_id: str, book_data: BookUpdate = Body(...)):
    collection = get_books_collection()
    if not ObjectId.is_valid(book_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
        
    # Drop fields passed as None
    update_dict = {k: v for k, v in book_data.model_dump().items() if v is not None}
    
    if len(update_dict) >= 1:
        await collection.update_one({"_id": ObjectId(book_id)}, {"$set": update_dict})
        
    updated_book = await collection.find_one({"_id": ObjectId(book_id)})
    if updated_book is None:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
    return updated_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: str):
    collection = get_books_collection()
    if not ObjectId.is_valid(book_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
        
    delete_result = await collection.delete_one({"_id": ObjectId(book_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
    return None