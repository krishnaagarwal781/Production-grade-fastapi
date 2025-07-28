# app/models.py
from pydantic import BaseModel


class Purpose(BaseModel):
    name: str
    description: str
