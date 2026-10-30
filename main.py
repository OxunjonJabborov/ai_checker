from fastapi import FastAPI

from api.v1 import exams, groups, students, submissions, teachers

app = FastAPI()

for module in (exams, groups, students, submissions, teachers):
    app.include_router(module.router, prefix="/api/v1")
