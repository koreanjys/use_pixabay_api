# models/api_models.py

from typing import Optional
from sqlmodel import SQLModel, Field


class ResponseData(SQLModel, table=True):
    image_id: int = Field(primary_key=True)
    type: Optional[str] = None
    tags: Optional[str] = None
    user: Optional[str] = None
    imageURL: str