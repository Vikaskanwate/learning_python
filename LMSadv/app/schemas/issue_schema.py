from pydantic import BaseModel  

class IssueCreate(BaseModel): 
    book_id: str 

class ReturnCreate(BaseModel):
    book_id: str