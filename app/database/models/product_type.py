from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class ProductType(Base):
    __tablename__ = "product_type"

    id = Column(Integer, primary_key=True)
    name = Column(String)
