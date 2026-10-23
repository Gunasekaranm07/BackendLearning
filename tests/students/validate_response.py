from app.core.database import SessionLocal
from app.students.repository import get_student
from app.students.schemas import StudentRes
with SessionLocal() as session:
    s = get_student(session, 1)
    print(StudentRes.model_validate(s))