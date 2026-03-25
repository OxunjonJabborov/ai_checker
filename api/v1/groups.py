from fastapi import APIRouter

from schemas.groups import GroupGet

api_router = APIRouter(prefix="/groups")

groups: dict[int, GroupGet] = {
    1: GroupGet(id=1, group_id=1, name="Group 1", count_students=30),
    2: GroupGet(id=2, group_id=2, name="Group 2", count_students=25),
    3: GroupGet(id=3, group_id=3, name="Group 3", count_students=20)
}

@api_router.get("/", response_model=list[GroupGet])
def get_groups():
    return list(groups.values())