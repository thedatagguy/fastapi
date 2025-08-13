from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Undertaker",
        "age": 69,
        "year":2020
    },
    2:{
        "name": "manoj",
        "age": 169,
        "year":2010

    }
}


class Student(BaseModel):
    name:str
    age:int
    year:str

class updatestudent(BaseModel):
    name : Optional[str]=None
    age : Optional[int] = None
    year : Optional[str]=None
@app.get("/")
def index():
    return "Hi beech welcome to my page"

# Path parameter example
@app.get("/get_student/{student_id}")
def get_student(
    student_id: int = Path(
        ..., 
        description="The ID of the student you want to view", 
        gt=0, lt=10
    )
):
    student = students.get(student_id)
    if student:
        return student
    return {"error": "Student not found"}

# Query parameter example
@app.get("/get_by_name")
def get_student_by_name(
    student_id: int = Query(..., description="The ID of the student"),
    name: Optional[str] = Query(None, description="The name of the student"),
    test: Optional[int] = Query(None, description="Test value to filter students")
):
    student = students.get(student_id)
    if student and student["name"] == name and test == 1:
        return student
    return {"Data": "Not found"}


@app.post("/create_student/{student_id}")
def create_student(student_id:int,student : Student):
    if student_id in students:
        return {"Error":"Student Exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update_student/{student_id}")

def update_student(student_id: int, student:updatestudent):
    if student_id not in students:
        return{"Error":"student does not exits"}
    
    if student.name is not None:
        students[student_id]["name"] = student.name
    if student.age is not None:
        students[student_id]["age"] = student.age
    if student.year is not None:
        students[student_id]["year"] = student.year

    return students[student_id]

@app.delete("/delete_student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error : Student does not exist"}
    del students[student_id]
    return {"Message : Student data deleted successfully"}