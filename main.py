from fastapi import FastAPI
from api.v1 import exams, groups, students, submissions, teachers

app = FastAPI()

app.include_router(exams.api_router)
app.include_router(groups.api_router)
app.include_router(students.api_router)
app.include_router(submissions.api_router)
app.include_router(teachers.api_router)
