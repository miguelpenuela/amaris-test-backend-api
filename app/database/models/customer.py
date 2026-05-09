from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database.connection import Base

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    city_id = Column(Integer, ForeignKey("city.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    status = Column(String)
    general_balance = Column(Integer)
    email = Column(String)
