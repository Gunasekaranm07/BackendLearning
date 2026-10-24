from sqlalchemy.orm import Session
from app.students.exceptions import StudentNotFound, DuplicateCourse
from app.students.repository import create_course, get_student, find_course

def add_course(db: Session, student_id: int, title: str):
    if get_student(db, student_id) is None:
        raise StudentNotFound()
    if find_course(db, student_id, title) is not None:
        raise DuplicateCourse()
    return create_course(db, student_id, title)