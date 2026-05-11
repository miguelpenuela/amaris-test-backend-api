from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from app.database.connection import get_db

# Services
from app.services.financial_service import (
    get_products,
    subscribe_fund,
    get_movements,
    get_financial_products,
    cancel_subscription
)

#Schemas
from app.schemas.registration_schema import (
    SubscribeRequestBody,
    CancelRegistrationBody
)

router = APIRouter(prefix="/v1/api/financial", tags=["financial services", "investment fund", "movements"])

@router.get("/investment-founds")
def investment_founds(db: Session = Depends(get_db)):
    return get_products(db)

@router.post("/subscribe")
def subscribe(body: SubscribeRequestBody, db: Session = Depends(get_db)):
    return subscribe_fund(db, body)

@router.get("/products/{customer_id}")
def products(customer_id: int, db: Session = Depends(get_db)):
    return get_financial_products(customer_id, db)

@router.get("/movements/{registration_id}")
def movements(registration_id: int, db: Session = Depends(get_db)):
    return get_movements(registration_id, db)

@router.post("/cancel-subscription")
def unsubscribe(body: CancelRegistrationBody, db: Session = Depends(get_db)):
    return cancel_subscription(body, db)
