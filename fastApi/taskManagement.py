from fastapi import FastAPI,HTTPException

app = FastAPI()

tasks = {
   1:{"title":"learn FastAPI","status":"pending"},
   2:{"title":"write crud endpoints","status":"in-progress"}
}


@app.post("/tasks/")
def create_task(task:dict):
    new_id = max(tasks.keys()) + 1 if task else 1
    tasks[new_id] = task
    return {"task_id":new_id,"task":task}


@app.get("/tasks/")
def read_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def read_task(task_id:int):
    if task_id in tasks:
        return {task_id:tasks[task_id]}
    raise HTTPException(status_code=404,detail="task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id:int,updated_task:dict):
    if task_id in tasks:
        tasks[task_id].update(updated_task)
        return {task_id:tasks[task_id]}
    raise HTTPException(status_code=404,detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    if task_id in tasks:
        deleted = tasks.pop(task_id)
        return {"deleted":{task_id:deleted}}
    raise HTTPException(status_code=404,detail="Task not found")