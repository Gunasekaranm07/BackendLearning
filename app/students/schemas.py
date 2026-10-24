from pydantic import BaseModel

class StudentReq(BaseModel):
    name: str
    age: int

class StudentRes(BaseModel):
    id: int
    name: str
    age: int

    model_config = {'from_attributes': True}

class CourseReq(BaseModel):
    title: str

class CourseRes(BaseModel):
    id: int
    title: str
    student_id: int

    model_config = {"from_attributes": True}

class StudentWithCourse(BaseModel):
    id: int
    name: str
    age: int
    courses: list[CourseRes]

    model_config={'from_attributes': True}