from fastapi import APIRouter

import fake_db
from schemas.submissions import SubmissionGet

router = APIRouter(prefix="/submissions")


@router.get("/", response_model=list[SubmissionGet])
def get_submissions():
    return list(fake_db.submissions.values())
