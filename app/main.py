import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, select
from fastapi import FastAPI
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, sessionmaker
from pydantic import BaseModel

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int]

# class StudentReq(BaseModel):
#     name: str
#     age: int

# class StudentRes(BaseModel):
#     id: int
#     name: str
#     age: int

Base.metadata.create_all(bind=engine)
print("Table created")

with sessionLocal() as session:
    all_student = session.scalars(select(Student))
    for student in all_student:
        print(student.id, student.name, student.age)
    first = session.scalars(select(Student).where(Student.age == 23)).first()
    print(f"first student whose age is 23: {first}")
    older = session.scalars(select(Student).where(Student.age>23)).all()
    print(f"Count of students older than 23: {len(older)}")