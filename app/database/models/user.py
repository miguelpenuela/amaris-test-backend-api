from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database.connection import Base
from datetime import datetime

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    username = Column(String)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    status = Column(String, default="ACTIVO")
