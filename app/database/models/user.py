from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database.connection import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    username = Column(String)
    password = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    status = Column(String)
