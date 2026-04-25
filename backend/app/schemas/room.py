from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from app.schemas.user import UserSummary


class RoomCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=300)
    is_private: bool = False


class RoomResponse(BaseModel):
    id: int
    name: str
    description: str | None
    is_private: bool
    created_at: datetime
    creator: UserSummary | None
    
    model_config = ConfigDict(from_attributes=True)

class RoomDetail(RoomResponse):
    member_count: int