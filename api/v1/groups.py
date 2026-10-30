from fastapi import APIRouter

import fake_db
from schemas.groups import GroupGet

router = APIRouter(prefix="/groups")


@router.get("/", response_model=list[GroupGet])
def get_groups():
    return list(fake_db.groups.values())
