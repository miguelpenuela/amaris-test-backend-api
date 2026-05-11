from fastapi import APIRouter

router = APIRouter(tags=["healthy"])

@router.get("/health")
def investment_founds():
    return {"status": "OK"}
