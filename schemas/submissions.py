from pydantic import BaseModel, Field

class SubmissionBase(BaseModel):
    submission_id: int = Field(description="The ID of the submission")
    deadline: str = Field(description="The end time of the submission")
    grade: float = Field(ge=0, le=5, description="The grade of the student's submission")


class SubmissionGet(SubmissionBase):
    id: int = Field()


class SubmissionCreate(SubmissionBase):
    pass