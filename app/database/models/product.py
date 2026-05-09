from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    product_type_id = Column(Integer, ForeignKey("product_type.id"), nullable=False)
    name = Column(String)

    min_amount = Column(Float)

    product_type = relationship("ProductType", back_populates="product")
    registration = relationship("Registration", back_populates="product")