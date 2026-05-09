from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

router = APIRouter(prefix="/v1/api/financial", tags=[
    "financial services", "investment fund", "movements"
])

@router.get("/investment-founds")
def investment_founds():
    return {"access_token": "prueba", "token_type": "bearer"}

@router.post("/registration")
def registration():
    return {"access_token": "prueba", "token_type": "bearer"}

@router.get("/movements")
def movements():
    return {"access_token": "prueba", "token_type": "bearer"}

