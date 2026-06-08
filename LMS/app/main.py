from fastapi import FastAPI
# 1. Grab the cleaned router export path from your package init
from app.routers import books_router 

app = FastAPI(
    title="Library Management System",
    description="A standard layered architecture using FastAPI and MongoDB",
    version="1.0.0"
)

# 2. Register it using the exact imported variable name
app.include_router(books_router) 

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Library Management API"}