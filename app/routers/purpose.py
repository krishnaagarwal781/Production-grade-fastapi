from fastapi import APIRouter
from app.models import Purpose
from app import crud

router = APIRouter()


@router.post("/purposes")
def create(purpose: Purpose):

    purpose_data = purpose.model_dump()

    inserted_id = crud.create_purpose(purpose_data)
    return {"inserted_id": inserted_id}


@router.get("/purposes")
def get_all():
    return crud.get_all_purposes()
