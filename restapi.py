from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()

students = {
    1: {"name": "rock", "age": 200, "year": 2024},
    2: {"name": "jayz", "age": 222, "year": 2023}
}


class Student(BaseModel):
    name: str
    age: int
    year: int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[int] = None

# 1. GET - Read student

@app.get("/students/{student_id}")
def get_student(
    student_id: int = Path(..., description="ID of the student"),
    details: bool = Query(False, description="Set to true for extra details")
):
    student = students.get(student_id)
    if not student:
        return {"error": "Student not found"}
    
    if details:
        student = student.copy()
        student["extra"] = f"{student['name']} is a hardworking student!"
    return student


# 2. POST - Create new student

@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "Student already exists"}
    students[student_id] = student.dict()
    return {"message": "Student created", "student": students[student_id]}


# 3. PUT - Update existing student

@app.put("/students/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "Student not found"}
    if student.name is not None:
        students[student_id]["name"] = student.name
    if student.age is not None:
        students[student_id]["age"] = student.age
    if student.year is not None:
        students[student_id]["year"] = student.year

    return {"message": "Student updated", "student": students[student_id]}


# 4. DELETE - Remove student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    del students[student_id]
    return {"message": "Student deleted successfully"}
