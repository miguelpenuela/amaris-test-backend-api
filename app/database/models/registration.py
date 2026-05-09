from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from app.database.connection import Base
from datetime import datetime

class Registration(Base):
    __tablename__ = "registration"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    customer_id = Column(Integer, ForeignKey("customer.id"))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    status = Column(String, default="ACTIVO")
    balance = Column(Float)
