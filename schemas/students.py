from pydantic import BaseModel, EmailStr, Field


class StudentBase(BaseModel):
    full_name: str = Field(description="The name of the student")
    age: int = Field(ge=17, le=35, description="The age of the student")
    phone_number: str = Field(description="The phone number of the student")
    email: EmailStr = Field(description="The email of the student")


class StudentGet(StudentBase):
    id: int


class StudentCreate(StudentBase):
    pass
