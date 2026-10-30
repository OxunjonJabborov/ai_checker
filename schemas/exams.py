from datetime import datetime
from typing import Self

from pydantic import BaseModel, Field, model_validator


class ExamBase(BaseModel):
    group_id: int = Field(description="The ID of the group associated with the exam")
    teacher_id: int = Field(description="The ID of the teacher associated with the exam")
    duration: float = Field(ge=1, le=300, description="Exam duration in minutes")
    start_time: datetime = Field(description="Start time of the exam")
    end_time: datetime = Field(description="End time of the exam")

    @model_validator(mode="after")
    def check_time_window(self) -> Self:
        if self.end_time <= self.start_time:
            raise ValueError("end_time must be after start_time")
        window_minutes = (self.end_time - self.start_time).total_seconds() / 60
        if self.duration > window_minutes:
            raise ValueError("duration must fit between start_time and end_time")
        return self


class ExamGet(ExamBase):
    id: int


class ExamCreate(ExamBase):
    pass
