from peewee import Model, CharField, IntegerField, ForeignKeyField
from peewee import *  
import settings


db = SqliteDatabase(database=f'{settings.DATABASE_PATH}/{settings.DATABASE_NAME}')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    position = CharField(default='')
    login = CharField(default='')
    password = CharField(default='')
    power_level = IntegerField(default=0)

class Student(BaseModel):
    first_name = CharField(default='')
    last_name = CharField(default='')
    grade = CharField(default='')

class Teacher(BaseModel):
    first_name = CharField(default='')
    last_name = CharField(default='')
    subject = CharField(default='')

class Class(BaseModel):
    class_name = CharField(default='')
    teacher_id = ForeignKeyField(Teacher, backref='classes', default=0)

class Subject(BaseModel):
    subject_name = CharField(default='')

class Grade(BaseModel):
    student_id = ForeignKeyField(Student, backref='grades', default=0)
    subject_id = ForeignKeyField(Subject, backref='grades', default=0)
    grade_value = DecimalField(default=0)

db.create_tables([
    User,
    Student,
    Teacher,
    Class,
    Subject,
    Grade
])