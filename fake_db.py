"""In-memory data used until a real database is added."""

from datetime import datetime

from schemas.exams import ExamGet
from schemas.groups import GroupGet
from schemas.students import StudentGet
from schemas.submissions import SubmissionGet
from schemas.teachers import TeacherGet

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

groups: dict[int, GroupGet] = {
    1: GroupGet(id=1, group_id=1, name="Group 1", count_students=30),
    2: GroupGet(id=2, group_id=2, name="Group 2", count_students=25),
    3: GroupGet(id=3, group_id=3, name="Group 3", count_students=20),
}

students: dict[int, StudentGet] = {
    1: StudentGet(
        id=1,
        student_id=1,
        full_name="Abdusalimova Sarvinoz",
        age=18,
        phone_number="+998777777777",
        email="abdusalimova@example.com",
    ),
    2: StudentGet(
        id=2,
        student_id=2,
        full_name="Rahmonaliyev Izzatbek ",
        age=20,
        phone_number="+998770000000",
        email="rahmonaliyev@example.com",
    ),
}

submissions: dict[int, SubmissionGet] = {
    1: SubmissionGet(id=1, submission_id=1, deadline=datetime(2026, 3, 16, 21, 0), grade=4.5),
    2: SubmissionGet(id=2, submission_id=2, deadline=datetime(2026, 3, 17, 21, 0), grade=3.0),
}

teachers: dict[int, TeacherGet] = {
    1: TeacherGet(
        id=1,
        teacher_id=1,
        full_name="Abdullayev Askar",
        phone_number="+998911111111",
        email="abdullayevaskar@example.com",
    ),
}
