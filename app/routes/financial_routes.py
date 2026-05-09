from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from app.database.connection import get_db

# Services
from app.services.financial_service import (
    get_products,
    registration_to_found,
    get_movements,
    get_financial_products
)

#Schemas
from app.schemas.registration_schema import (RegistrationCreate, RegistrationResponse)

router = APIRouter(prefix="/v1/api/financial", tags=[
    "financial services", "investment fund", "movements"
])

@router.get("/investment-founds")
def investment_founds(db: Session = Depends(get_db)):
    return get_products(db)

@router.post("/registration", response_model=RegistrationResponse)
def registration(body: RegistrationCreate, db: Session = Depends(get_db)):
    return registration_to_found(db, body)

@router.get("/products/{customer_id}")
def products(customer_id: int, db: Session = Depends(get_db)):
    return get_financial_products(customer_id, db)

@router.get("/movements/{registration_id}")
def movements(registration_id: int, db: Session = Depends(get_db)):
    return get_movements(registration_id, db)

