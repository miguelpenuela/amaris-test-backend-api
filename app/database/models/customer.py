from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from app.database.connection import Base
from datetime import datetime

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    city_id = Column(Integer, ForeignKey("city.id"))

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    status = Column(String, default="ACTIVO")
    general_balance = Column(Float, default=500000.0)

    email = Column(String, unique=True, nullable=False)
