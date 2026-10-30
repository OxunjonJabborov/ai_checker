from datetime import datetime

import pytest
from pydantic import ValidationError

from schemas.exams import ExamCreate
from schemas.students import StudentCreate
from schemas.submissions import SubmissionCreate


def make_exam(**overrides):
    data = {
        "group_id": 1,
        "teacher_id": 1,
        "duration": 60,
        "start_time": datetime(2026, 3, 30, 19, 30),
        "end_time": datetime(2026, 3, 30, 21, 30),
    }
    return ExamCreate(**(data | overrides))


def test_exam_accepts_valid_time_window():
    assert make_exam().duration == 60


def test_exam_rejects_end_time_before_start_time():
    with pytest.raises(ValidationError, match="end_time must be after start_time"):
        make_exam(end_time=datetime(2026, 3, 30, 18, 0))


def test_exam_rejects_duration_longer_than_window():
    with pytest.raises(ValidationError, match="duration must fit"):
        make_exam(duration=180)


def test_submission_rejects_invalid_deadline():
    with pytest.raises(ValidationError):
        SubmissionCreate(deadline="tomorrow", grade=4)


def test_student_rejects_invalid_email():
    with pytest.raises(ValidationError):
        StudentCreate(
            full_name="Test Student",
            age=18,
            phone_number="+998900000000",
            email="not-an-email",
        )
