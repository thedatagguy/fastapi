from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()

students = {
    1: {
        "name": "Undertaker",
        "age": 69,
        "class": "third class"
    }
}

@app.get("/")
def index(): 
    return "Hi beech welcome to my page"

@app.get("/get_student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view",gt=0,lt=10)):
    return students[student_id]

@app.get('/get_by_name')
def get_student(*, name: Optional[str] = None,test : int):
    for student_id in students:
         if students[student_id]["name"]==name:
             return students[student_id]
    return {"Data":"Not found"}
    