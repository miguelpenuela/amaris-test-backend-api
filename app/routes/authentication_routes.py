from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.database.connection import get_db

# Schemas
from app.schemas.customer_schema import (CustomerResponse)
from app.schemas.login_schema import (LoginRequest)
from app.schemas.create_customer_schema import (CreateCustomerRequest)

# Services
from app.services.authentication_service import (create_customer, login_user)

router = APIRouter(prefix="/v1/api/authentication", tags=["authentication"])

@router.post("/register", response_model=CustomerResponse)
def register(
    body: CreateCustomerRequest,
    db: Session = Depends(get_db),
):
    return create_customer(db, body)

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return login_user(db, data.username, data.password)

