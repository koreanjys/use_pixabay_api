# models/api_models.py

from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, timedelta


class ResponseData(SQLModel, table=True):
    image_id: int = Field(primary_key=True)
    type: Optional[str] = None
    tags: Optional[str] = None
    user: Optional[str] = None
    keyword: Optional[str] = None
    imageURL: str
    created_at: datetime = datetime.utcnow() + timedelta(hours=9)