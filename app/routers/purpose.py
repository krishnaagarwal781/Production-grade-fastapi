from fastapi import APIRouter, HTTPException
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


@router.get("/purposes/{purpose_id}")
def get_one(purpose_id: str):
    purpose = crud.get_purpose_by_id(purpose_id)
    if not purpose:
        raise HTTPException(status_code=404, detail="Purpose not found")
    return purpose


@router.put("/purposes/{purpose_id}")
def update(purpose_id: str, purpose: Purpose):
    updated_count = crud.update_purpose(purpose_id, purpose.model_dump())
    if updated_count == 0:
        raise HTTPException(status_code=404, detail="Purpose not found or unchanged")
    return {"message": "Purpose updated successfully"}


@router.delete("/purposes/{purpose_id}")
def delete(purpose_id: str):
    deleted_count = crud.delete_purpose(purpose_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Purpose not found")
    return {"message": "Purpose deleted successfully"}
