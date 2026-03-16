from fastapi import APIRouter

from schemas.exams import ExamGet

api_router = APIRouter(prefix="/exams")

exams: dict[int, ExamGet] = {1: ExamGet(id=1,
                                        group_id=1,
                                        teacher_id=1,
                                        duration=10,
                                        start_time="2026-03-16T19:00:00",
                                        end_time="2026-03-16T21:00:00")} 

@api_router.get("/", response_model=list[ExamGet])
def get_exams():
    return list(exams.values())


