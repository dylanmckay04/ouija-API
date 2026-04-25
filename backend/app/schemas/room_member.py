from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.models.room_member import MemberRole
from app.schemas.user import UserSummary


class RoomMemberResponse(BaseModel):
    user: UserSummary
    role: MemberRole
    joined_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
