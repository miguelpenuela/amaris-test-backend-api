from pydantic import BaseModel

class RegistrationBase(BaseModel):
    product_id: int
    customer_id: int
    balance: float

class SubscribeRequestBody(RegistrationBase):
    notification_type: str
    pass

class RegistrationResponse(RegistrationBase):
    id: int
    class Config:
        from_attributes = True

class CancelRegistrationBody(BaseModel):
    id: int