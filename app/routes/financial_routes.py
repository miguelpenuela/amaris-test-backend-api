from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.database.connection import get_db

# Services
from app.services.financial_service import get_products

router = APIRouter(prefix="/v1/api/financial", tags=[
    "financial services", "investment fund", "movements"
])

@router.get("/investment-founds")
def investment_founds(db: Session = Depends(get_db)):
    return get_products(db)

@router.post("/registration")
def registration():
    return {"response": "unimplemented"}

@router.get("/movements")
def movements():
    return {"response": "unimplemented"}

