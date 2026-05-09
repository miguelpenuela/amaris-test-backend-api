from pydantic import BaseModel

from .customer_schema import CustomerCreate

class CreateCustomerRequest(BaseModel):
    customer: CustomerCreate
    password: str
