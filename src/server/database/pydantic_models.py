from pydantic import BaseModel
from typing import Optional


class ModifyBaseModel(BaseModel):
    id: Optional[int] = 0


class ChangePassword(ModifyBaseModel):
    password: str


class LoginData(ModifyBaseModel):
    login: str
    password: str


class User(ModifyBaseModel):
    position: str
    login: str
    password: str
    power_level: int 


class Student(ModifyBaseModel):
    student_id: int
    first_name: str
    last_name: str
    grade: str


class Teacher(ModifyBaseModel):
    teacher_id: int
    first_name: str
    last_name: str
    subject: str


class Class(ModifyBaseModel):
    class_name: str
    teacher_id: int


class Subject(ModifyBaseModel):
    subject_name: str


class Grade(ModifyBaseModel):
    student_id: int
    subject_id: int
    grade_value: float