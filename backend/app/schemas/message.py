from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from app.schemas.user import UserSummary


class MessageCreate(BaseModel):
    content: str = Field(..., min_length=1, max_length=4000)


class MessageResponse(BaseModel):
    id: int
    content: str
    room_id: int
    author: UserSummary | None
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class MessagePage(BaseModel):
    items: list[MessageResponse]
    total: int
    limit: int
    offset: int
