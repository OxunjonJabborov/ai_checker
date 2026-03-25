from pydantic import BaseModel, Field


class StudentBase(BaseModel):
    student_id: int = Field(description="The ID of the student")
    full_name: str = Field(description="The name of the student")
    age: int = Field(ge=17, le=35, description="The age of the student")
    phone_number: str = Field(description="The phone number of the student")
    email: str = Field(description="The email of the student")


class StudentGet(StudentBase):
    id: int = Field()


class StudentCreate(StudentBase):
    pass

