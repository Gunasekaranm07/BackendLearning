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
    #insert
    student1 = Student(name="Ranjith R", age=24)
    session.add(student1)
    session.commit()
    new_id = student1.id
    print("saved at id: ", student1.id)

    student2 = session.scalar(select(Student).where(Student.id == new_id))
    if student2 is None:
        print("student not found")
    else:
        #read
        print(f'Read: {student2.name} {student2.age}')
        #update
        student2.age = 21
        session.commit()
        print(f"Updated age to {student2.age}")
        #delete
        name = student2.name
        session.delete(student2)
        session.commit()
        print(f'Deleted: {name}')
with sessionLocal() as session:
    check = session.scalar(select(Student).where(Student.id==new_id))
    print("deleted") if check is None else print("still there")