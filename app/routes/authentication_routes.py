from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.customer_schema import (CustomerCreate, CustomerResponse)
from app.services.authentication_service import create_customer

router = APIRouter(prefix="/v1/api/authentication", tags=["authentication"])

@router.post("/register", response_model=CustomerResponse)
def register(
    customer: CustomerCreate,
    db: Session = Depends(get_db),
):
    return create_customer(db, customer)

@router.post("/login")
def login():
    return {"access_token": "prueba", "token_type": "bearer"}

