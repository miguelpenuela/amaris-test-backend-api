from pydantic import BaseModel,EmailStr,Field
from typing import Optional
from datetime import datetime

class CustomerBase(BaseModel):
    name: str
    surname: str
    city_id: int
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    status: str = "ACTIVO"
    general_balance: float = 500000
    email: EmailStr

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int
    class Config:
        from_attributes = True