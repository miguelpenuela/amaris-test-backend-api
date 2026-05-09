from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database.connection import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    product_type_id = Column(Integer, foreign_key="product_type.id")
    name = Column(String)
