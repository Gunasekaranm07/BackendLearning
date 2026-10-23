from sqlalchemy.orm import Session
from sqlalchemy import select
from app.students.models import Student

def create_student(db: Session, name:str, age:int)->Student:
    student = Student(name = name, age = age)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_student(db: Session, student_id: int) -> Student|None:
    student = db.scalar(select(Student).where(Student.id==student_id))
    return student

def get_students(db: Session) -> list[Student]:
    students = db.scalars(select(Student)).all()
    return students

def update_student(db: Session, student_id: int, name: str, age: int) -> Student | None:
    student = get_student(db=db, student_id=student_id)
    if student is not None:
        student.name, student.age = name, age
        db.commit()
        db.refresh(student)
        return student
    return None

def delete_student(db: Session, student_id: int) -> bool:
    student = get_student(db=db, student_id=student_id)
    if student is not None:
        db.delete(student)
        db.commit()
        return True
    return False