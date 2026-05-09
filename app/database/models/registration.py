from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database.connection import Base

class Registration(Base):
    __tablename__ = "registration"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    customer_id = Column(Integer, ForeignKey("customer.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    status = Column(String)
    balance = Column(Integer)
