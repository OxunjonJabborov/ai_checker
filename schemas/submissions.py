from datetime import datetime

from pydantic import BaseModel, Field


class SubmissionBase(BaseModel):
    deadline: datetime = Field(description="The end time of the submission")
    grade: float = Field(ge=0, le=5, description="The grade of the student's submission")


class SubmissionGet(SubmissionBase):
    id: int


class SubmissionCreate(SubmissionBase):
    pass
