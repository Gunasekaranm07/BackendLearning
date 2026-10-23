from pydantic import BaseModel

class StudentReq(BaseModel):
    name: str
    age: int

class StudentRes(BaseModel):
    id: int
    name: str
    age: int

    model_config = {'from_attributes': True}