from fastapi import FastAPI
from api.v1 import exams, groups, students, submissions, teachers

app = FastAPI()

app.include_router(exams.router)
app.include_router(groups.router)
app.include_router(students.router)
app.include_router(submissions.router)
app.include_router(teachers.router)
