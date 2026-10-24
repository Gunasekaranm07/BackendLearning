from sqlalchemy import select
from sqlalchemy.orm import Session
from app.students.models import Student, Course

def get_students(db: Session) -> list[Student]:
    students = db.scalars(select(Student)).all()
    return students

def get_student(db: Session, student_id: int) -> (Student | None):
    student = db.scalar(select(Student).where(Student.id == student_id))
    return student

def create_student(db: Session, name:str, age:int) -> (Student | None):
    student = Student(name = name, age = age)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def update_student(db: Session, student_id: int, name:str, age:int) -> (Student | None):
    student = get_student(db=db, student_id=student_id)
    if student is None:
        return None
    student.name = name
    student.age = age
    db.commit()
    db.refresh(student)
    return student

def delete_student(db: Session, student_id: int) -> bool:
    student = get_student(db=db, student_id=student_id)
    if student is None:
        return False
    db.delete(student)
    db.commit()
    return True

def create_course(db: Session, student_id: int, title: str) -> Course:
    course = Course(title=title, student_id=student_id)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def find_course(db: Session, student_id: int, title: str) -> (Course | None):
    return db.scalar(
        select(Course).where(student_id == Course.student_id, title == Course.title)
    )