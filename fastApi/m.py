from fastapi import FastAPI ,HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

client = AsyncIOMotorClient('mongodb://localhost:27017/')
db = client['taskdb']
task_collection = db['task']


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    title:str
    status:str
    due_date:str | None = None
    priority:int | None = None

def task_helper(task) -> dict:
    return {
        "id":str(task["_id"]),
        "title":task["title"],
        "status":task["status"],
        "due_date":task.get("due_date"),
        "priority":task.get("priority")
    }


@app.post("/tasks/")
async def create_task(task:Task):
    result = await task_collection.insert_one(task.model_dump())
    return {"id":str(result.inserted_id),"task":task.model_dump()}

@app.get("/tasks/")
async def read_tasks():
    tasks = []
    async for task in task_collection.find():
        tasks.append(task_helper(task))
    return tasks

@app.get("/tasks/{task_id}")
async def read_task(task_id:str):
    task = await task_collection.find_one({"_id":ObjectId(task_id)})
    if task:
        return task_helper(task)
    raise HTTPException(status_code=404,detail="Task not found")

@app.put("/tasks/{task_id}")
async def update_task(task_id:str,updated_task:Task):
    result  = await task_collection.update_one(
        {"_id":ObjectId(task_id)},{"$set":updated_task.model_dump()}
    )
    if result.modified_count:
        return {"id":task_id,"updated":updated_task.model_dump()}
    raise HTTPException(status_code=404,detail="Task not found")

@app.delete("/tasks/{task_id}")
async def delete_task(task_id:str):
    try:
        oid = ObjectId(task_id)
    except:
        raise HTTPException(status_code=400,detail="Invalid ID format")
    result = await task_collection.delete_one({"_id":oid})
    if result.deleted_count:
        return {"deleted":task_id}
    raise HTTPException(status_code=404,detail="Task not found")