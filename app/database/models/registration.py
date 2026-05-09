from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from app.database.connection import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Registration(Base):
    __tablename__ = "registration"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    status = Column(String, default="ACTIVO")
    balance = Column(Float)

    movements = relationship("Movement", back_populates="registration")
    product = relationship("Product", back_populates="registration")
