from fastapi import HTTPException

from sqlalchemy.orm import Session

#Models
from app.database.models.customer import Customer
from app.database.models.user import User

#Schemas
from app.schemas.create_customer_schema import (CreateCustomerRequest)

from .crypto_service import (hash_password, verify_password)

def create_customer(db: Session, body: CreateCustomerRequest) -> Customer:
    try:
        customer = body.customer
        with db.begin():
            new_customer = Customer(
                name = customer.name,
                surname = customer.surname,
                city_id = customer.city_id,
                email = customer.email,
                status = 'ACTIVO',
                general_balance = 500000
            )
            db.add(new_customer)
            db.flush()

            hashed_password = hash_password(body.password)

            new_user = User(
                customer_id = new_customer.id,
                username = new_customer.email,
                password_hash = hashed_password
            )
            db.add(new_user)
            return new_customer
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def login_user(db: Session, username: str, password: str):
    try:
        finded_user = db.query(User).filter(User.username == username).first()
        if not finded_user:
            raise HTTPException(status_code=400, detail="Incorrect email or password")

        if not verify_password(password, finded_user.password_hash):
            raise HTTPException(status_code=400, detail="Incorrect email or password")

        customer_info = db.query(Customer).filter(Customer.email == finded_user.username).first()

        return {"user": finded_user, "customer_info": customer_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))