from src.server.database import pydantic_models, database_models
from src.server.service import RouterManager


routers = (
    RouterManager(pydantic_model=pydantic_models.Grade, database_model=database_models.Grade, prefix='/grades', tags=['Grades']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Class, database_model=database_models.Class, prefix='/classes', tags=['Classes']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Student, database_model=database_models.Student, prefix='/students', tags=['Students']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Subject, database_model=database_models.Subject, prefix='/subjects', tags=['Subjects']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.User, database_model=database_models.User, prefix='/users', tags=['Users']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Teacher, database_model=database_models.Teacher, prefix='/teacher', tags=['Teacher']).fastapi_router
)
