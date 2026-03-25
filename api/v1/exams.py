from fastapi import APIRouter
from datetime import datetime
from schemas.exams import ExamGet

api_router = APIRouter(prefix="/exams")

exams: dict[int, ExamGet] = {1: ExamGet(id=1,
                                        group_id=1,
                                        teacher_id=1,
                                        duration=10,
                                        start_time=datetime(2026, 3, 30, 19, 30),
                                        end_time=datetime(2026, 3, 30, 21, 30))} 

@api_router.get("/", response_model=list[ExamGet])
def get_exams():
    return list(exams.values())


