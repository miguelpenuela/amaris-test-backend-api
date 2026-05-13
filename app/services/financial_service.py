from fastapi import HTTPException

from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import select
from sqlalchemy import func

#Models
from app.database.models.product import Product
from app.database.models.registration import Registration
from app.database.models.movement import Movement
from app.database.models.customer import Customer

#Schemas
from app.schemas.registration_schema import (SubscribeRequestBody, RegistrationResponse, CancelRegistrationBody)

def get_products(db: Session):
    sql = select(Product).options(joinedload(Product.product_type))
    products = db.execute(sql).scalars().all()
    return products

def subscribe_fund(db: Session, body: SubscribeRequestBody) -> RegistrationResponse:
    try:
        
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
            type = "SUBSCRIBED",
            amount = new_registration.balance
        )
        db.add(new_movement)

        customer = db.query(Customer).filter(Customer.id == body.customer_id).first()
        new_general_balance = customer.general_balance - new_registration.balance

        setattr(customer, 'general_balance', new_general_balance)

        db.commit()

        db.refresh(customer)
    
        return customer
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def validate_min_amount(db: Session, body: SubscribeRequestBody):
    product =  db.query(Product).filter(Product.id == body.product_id).first()
    return body.balance >= product.min_amount

def get_financial_products(customer_id: int, db: Session):
    sql = select(Registration).options(joinedload(Registration.product)).filter(Registration.customer_id == customer_id).order_by(Registration.id.desc())
    result = db.execute(sql).scalars().all()
    return result

def get_movements(registration_id: int, db: Session):
    sql = select(Registration)\
        .options(joinedload(Registration.product),joinedload(Registration.movements))\
        .filter(Registration.id == registration_id)
    result = db.execute(sql).unique().scalars().first()
    return result

def cancel_subscription(body: CancelRegistrationBody, db: Session):
    try:
        registration = db.query(Registration).filter(Registration.id == body.id).first()

        if not registration:
            raise HTTPException(404, "Subscription not found")
        
        customer = db.query(Customer).filter(Customer.id == registration.customer_id).first()

        totalBalance = db.query(func.sum(Movement.amount)).filter(Movement.registration_id == registration.id).scalar()

        setattr(registration, 'status', 'UNSUBSCRIBED')
        setattr(registration, 'balance', totalBalance)

        new_general_balance = customer.general_balance + totalBalance

        setattr(customer, 'general_balance', new_general_balance)

        new_movement = Movement(
            registration_id = registration.id,
            type = "UNSUBSCRIBED",
            amount = 0
        )
        db.add(new_movement)

        db.commit()

        db.refresh(registration)
        db.refresh(customer)
        
        return customer
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))