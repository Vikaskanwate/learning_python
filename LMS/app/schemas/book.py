from pydantic import BaseModel, Field, BeforeValidator
from typing import Annotated, Optional

# Custom type to safely map MongoDB's ObjectId to a string
PyObjectId = Annotated[str, BeforeValidator(str)]

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1)
    isbn: str = Field(..., pattern=r"^[0-9\-]{10,13}$")
    copies: int = Field(default=1, ge=0)

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    copies: Optional[int] = None

class BookResponse(BookBase):
    id: PyObjectId = Field(alias="_id")

    class Config:
        populate_by_name = True  # Allows alias mapping from _id to id