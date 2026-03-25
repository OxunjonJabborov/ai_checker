from fastapi import APIRouter

from schemas.teachers import TeacherGet

api_router = APIRouter(prefix="/teachers")

teachers: dict[int, TeacherGet] = {
    1: TeacherGet(id=1, teacher_id=1, full_name="Abdullayev Askar", phone_number="+998911111111", email="abdullayevaskar@example.com"),
}

@api_router.get("/", response_model=list[TeacherGet])
def teacher_get():
    return list(teachers.values())