from pydantic import BaseModel, EmailStr, Field


class TeacherBase(BaseModel):
    teacher_id: int = Field(description="The ID of the teacher")
    full_name: str = Field(description="The name of the teacher")
    phone_number: str = Field(description="The phone number of the teacher")
    email: EmailStr = Field(description="The email of the teacher")


class TeacherGet(TeacherBase):
    id: int


class TeacherCreate(TeacherBase):
    pass
