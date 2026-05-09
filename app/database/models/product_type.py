from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class ProductType(Base):
    __tablename__ = "product_type"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    product = relationship("Product", back_populates="product_type")