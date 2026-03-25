from fastapi import APIRouter

from schemas.submissions import SubmissionGet

api_router = APIRouter(prefix="/submissions")


submissions: dict[int, SubmissionGet] = {
    1: SubmissionGet(id=1, submission_id=1, deadline="2026-03-16T21:00:00", grade=4.5),
    2: SubmissionGet(id=2, submission_id=2, deadline="2026-03-17T21:00:00", grade=3.0)
}

@api_router.get("/", response_model=list[SubmissionGet])
def get_submissions():
    return list(submissions.values())