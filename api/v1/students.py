from fastapi import APIRouter

import fake_db
from schemas.students import StudentGet

router = APIRouter(prefix="/students")


@router.get("/", response_model=list[StudentGet])
def get_students():
    return list(fake_db.students.values())
