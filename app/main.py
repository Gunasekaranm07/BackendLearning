from app.core.database import engine, SessionLocal, Base
from app.students.models import Student   
from app.students.schemas import StudentReq, StudentRes
from app.students.repository import *

Base.metadata.create_all(bind=engine)
print("tables created")

with SessionLocal() as session:
    temp = create_student(session, "Throwaway", 30)
    temp_id = temp.id
    print("Delete:", delete_student(session, temp_id))
    print("After delete:", get_student(session, temp_id))

    print("Delete 999:", delete_student(session, 999))
    print("Update 999:", update_student(session, 999, "X", 1))

    updated = update_student(session, 1, "Gunasekaran M", 26)
    print("Updated:", updated.age if updated else "not found")