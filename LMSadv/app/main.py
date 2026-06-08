from fastapi import FastAPI
from app.routes import auth_routes, book_routes, issue_routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(book_routes.router, prefix="/books")
app.include_router(issue_routes.router, prefix="/transactions")

@app.get("/")
def root():
    return {"message": "Library API running"}