from pydantic import BaseModel

class RegistrationBase(BaseModel):
    product_id: int
    customer_id: int
    balance: float

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationResponse(RegistrationBase):
    id: int
    class Config:
        from_attributes = True