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
    student = session.scalars(select(Student).where(Student.name=="Santhosh M")).first()
    print(f"Before update: {student.age}")
    student.age = 22
    print(f"After update: {student.age}")
