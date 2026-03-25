from pydantic import BaseModel, Field

class TeacherBase(BaseModel):
    teacher_id: int = Field(description="The ID of the teacher")
    full_name: str = Field(description="The name of the teacher")
    phone_number: str = Field(description="The phone number of the teacher")
    email: str = Field(description="The email of the teacher")


class TeacherGet(TeacherBase):
    id: int = Field()


class TeacherCreate(TeacherBase):
    pass