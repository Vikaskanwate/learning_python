from fastapi import APIRouter
from app.schemas.book_schema import BookCreate
from app.services.book_service import add_book, get_books, delete_book
from app.dependencies import admin_required
from fastapi import Depends

router = APIRouter()

@router.post("/")
def create_book(book: BookCreate, user=Depends(admin_required)):
    return add_book(book)

@router.get("/")
def read_books():
    return get_books()

@router.delete("/{title}")
def remove_book(title: str):
    return delete_book(title)