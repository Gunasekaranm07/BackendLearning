from fastapi import APIRouter, HTTPException, Depends
from app.students.repository import *
from app.students.schemas import StudentRes, StudentReq
from app.core.database import get_db
from sqlalchemy.orm import Session
router = APIRouter(prefix="/api/v1/students", tags=["Students Routes"])

@router.get("/", status_code=200, response_model=list[StudentRes])
def read_all_students(
    db: Session = Depends(get_db)
):
    return get_students(db=db)

@router.get("/{student_id}", status_code=200, response_model=StudentRes)
def read_student_by_id(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = get_student(db=db, student_id=student_id)
    if student is not None:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

@router.post("/", status_code=201, response_model=StudentRes)
def create_student_by_id(
    req: StudentReq,
    db: Session = Depends(get_db)
):
    return create_student(db, req.name, req.age)

@router.put("/{student_id}", status_code=200, response_model=StudentRes)
def update_student_by_id(
    student_id: int,
    req: StudentReq,
    db: Session = Depends(get_db)
):
    student = update_student(db, student_id, req.name, req.age)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.delete("/{student_id}", status_code=204)
def delete_student_by_id(
    student_id: int,
    db: Session = Depends(get_db)
):
    if not delete_student(db, student_id):
        raise HTTPException(status_code=404, detail="Student not found")