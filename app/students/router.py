from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.students.schemas import StudentReq, StudentRes
from app.students.repository import (
    get_student, get_students, create_student, update_student, delete_student
)

router = APIRouter(prefix="/api/v1/students", tags=["Students"])

@router.get("/", status_code=200, response_model=list[StudentRes])
def read_students(db:Session = Depends(get_db)):
    return get_students(db)

@router.post("/", status_code=201, response_model=StudentRes)
def insert_student(req: StudentReq, db:Session = Depends(get_db)):
    return create_student(db = db, name = req.name, age = req.age)

@router.get("/{student_id}", status_code=200, response_model=StudentRes)
def read_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = get_student(db=db, student_id=student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not Found")
    return student

@router.put("/{student_id}", status_code=200, response_model=StudentRes)
def update_student_by_id(student_id:int, req: StudentReq, db: Session = Depends(get_db)):
    student = update_student(db, student_id, req.name, req.age)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not Found")
    return student

@router.delete("/{student_id}", status_code=204)
def delete_student_by_id(student_id: int, db: Session = Depends(get_db)):
    if delete_student(db, student_id):
        return "Deleted Successfully" 
    raise HTTPException(status_code=404, detail="Student not Found")