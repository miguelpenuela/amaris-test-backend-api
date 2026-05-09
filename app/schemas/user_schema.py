from pydantic import BaseModel,EmailStr,Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    customer_id: int
    username: EmailStr
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    status: str = "ACTIVO"

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True