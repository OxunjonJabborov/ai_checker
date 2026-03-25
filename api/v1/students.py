from fastapi import APIRouter

from schemas.students import StudentGet

api_router = APIRouter(prefix="/students")

students: dict[int, StudentGet] = {
    1: StudentGet(id=1, student_id=1, full_name="Abdusalimova Sarvinoz", age=18, phone_number='+998777777777', email="abdusalimova@example.com"),
    2: StudentGet(id=2, student_id=2, full_name="Rahmonaliyev Izzatbek ", age=20, phone_number='+998770000000', email="rahmonaliyev@example.com")
}

@api_router.get("/", response_model=list[StudentGet])
def get_students():
    return list(students.values())
