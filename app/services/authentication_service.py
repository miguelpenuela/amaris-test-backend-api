from fastapi import HTTPException

from sqlalchemy.orm import Session
import datetime
from app.database.models.customer import Customer
from app.schemas.customer_schema import CustomerCreate

from app.database.models.user import User
from app.schemas.user_schema import UserCreate

now = datetime.datetime.now()

def create_customer(db: Session, customer: Customer):
    try:
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

            new_user = User(
                customer_id = new_customer.id,
                username = new_customer.email,
                password_hash = "miclavetemporal"
            )
            db.add(new_user)
            return new_customer
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
