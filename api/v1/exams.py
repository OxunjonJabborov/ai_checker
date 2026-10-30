from fastapi import APIRouter

import fake_db
from schemas.exams import ExamGet

router = APIRouter(prefix="/exams")


@router.get("/", response_model=list[ExamGet])
def get_exams():
    return list(fake_db.exams.values())
