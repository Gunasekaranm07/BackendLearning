from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.students.schemas import (
    StudentReq, StudentRes, CourseRes, CourseReq, StudentWithCourse
)
from app.students.repository import (
    get_student, get_students, create_student, update_student, delete_student, create_course
)
from app.students.exceptions import StudentNotFound, DuplicateCourse
from app.students.service import add_course

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
    if not delete_student(db, student_id):
        raise HTTPException(status_code=404, detail="Student not Found")

@router.post("/{student_id}/course", status_code=201, response_model=CourseRes)
def add_course_to_student(student_id: int, req: CourseReq, db: Session = Depends(get_db)):
    try:
        return add_course(db, student_id, req.title)
    except StudentNotFound:
        raise HTTPException(status_code=404, detail="Student not Found")
    except DuplicateCourse:
        raise HTTPException(status_code=409, detail="Course already existed")


@router.get("/{student_id}/full", status_code=200, response_model=StudentWithCourse)
def get_student_with_course(student_id: int, db: Session = Depends(get_db)):
    student = get_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not Found")
    return student