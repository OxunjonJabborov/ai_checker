from pydantic import BaseModel, Field

class GroupBase(BaseModel):
    group_id: int = Field(description="The ID of the group")
    name: str = Field(description="The name of the group")
    count_students: int = Field(ge=1, description="The number of students in the group")


class GroupGet(GroupBase):
    id: int = Field()


class GroupCreate(GroupBase):
    pass