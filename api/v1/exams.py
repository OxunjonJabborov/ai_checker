from datetime import datetime

from fastapi import APIRouter

from schemas.exams import ExamGet

router = APIRouter(prefix="/exams")

exams: dict[int, ExamGet] = {
    1: ExamGet(
        id=1,
        group_id=1,
        teacher_id=1,
        duration=10,
        start_time=datetime(2026, 3, 30, 19, 30),
        end_time=datetime(2026, 3, 30, 21, 30),
    ),
}


@router.get("/", response_model=list[ExamGet])
def get_exams():
    return list(exams.values())
