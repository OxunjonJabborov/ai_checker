from pydantic import BaseModel, Field
from datetime import datetime


class ExamBase(BaseModel):
    group_id: int = Field(description="The ID of the group associated with the exam")
    teacher_id: int = Field(description="The ID of the teacher associated with the exam")
    duration: float = Field(ge=1, le=300, description="Exam duration in minutes")
    start_time: datetime = Field(description="Start time of the exam")
    end_time: datetime = Field(description="End time of the exam")


class ExamGet(ExamBase):
    id: int = Field()


class ExamCreate(ExamBase):
    pass



