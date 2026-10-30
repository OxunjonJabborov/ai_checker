from fastapi import APIRouter

import fake_db
from schemas.teachers import TeacherGet

router = APIRouter(prefix="/teachers")


@router.get("/", response_model=list[TeacherGet])
def get_teachers():
    return list(fake_db.teachers.values())
