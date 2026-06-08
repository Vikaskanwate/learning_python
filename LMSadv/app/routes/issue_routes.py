from fastapi import APIRouter, Depends
from app.utils.security import get_current_user
from app.schemas.issue_schema import IssueCreate, ReturnCreate
from app.services.issue_service import issue_book, return_book

router = APIRouter()

@router.post("/issue")
def issue(data: IssueCreate, user_id: str = Depends(get_current_user)):
    return issue_book(data, user_id)


@router.post("/return")
def return_route(data: IssueCreate, user_id: str = Depends(get_current_user)):
    return return_book(data, user_id)