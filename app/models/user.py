from datetime import datetime
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: str | None = None
    username: str
    email: EmailStr
    hashed_password: str
    created_at: datetime = datetime.utcnow()
