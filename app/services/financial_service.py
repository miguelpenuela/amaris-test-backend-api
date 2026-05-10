from fastapi import HTTPException

from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import select

#Models
from app.database.models.product import Product
from app.database.models.registration import Registration
from app.database.models.movement import Movement

#Schemas
from app.schemas.registration_schema import (RegistrationCreate, RegistrationResponse)

def get_products(db: Session):
    sql = select(Product).options(joinedload(Product.product_type))
    products = db.execute(sql).scalars().all()
    return products

def registration_to_found(db: Session, body: RegistrationCreate) -> RegistrationResponse:
    try:
        with db.begin():
            if (not validate_min_amount(db, body)):
                raise HTTPException(status_code=409, detail="The amount is not valid according to the product rules")
        
            new_registration = Registration(
                product_id = body.product_id,
                customer_id = body.customer_id,
                balance = body.balance
            )
            db.add(new_registration)
            db.flush()

            new_movement = Movement(
                registration_id = new_registration.id,
                type = "SUBSCRIBE",
                amount = new_registration.balance
            )
            db.add(new_movement)
        
            return new_registration
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def validate_min_amount(db: Session, body: RegistrationCreate):
    product =  db.query(Product).filter(Product.id == body.product_id).first()
    return body.balance >= product.min_amount

def get_financial_products(customer_id: int, db: Session):
    sql = select(Registration).options(joinedload(Registration.product)).filter(Registration.customer_id == customer_id)
    result = db.execute(sql).scalars().all()
    return result

def get_movements(registration_id: int, db: Session):
    sql = select(Registration).options(joinedload(Registration.product),joinedload(Registration.movements)).filter(Registration.id == registration_id)
    result = db.execute(sql).unique().scalars().first()
    return result
