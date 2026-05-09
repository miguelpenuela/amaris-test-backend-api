from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from app.database.connection import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Movement(Base):
    __tablename__ = "movement"

    id = Column(Integer, primary_key=True)
    registration_id = Column(Integer, ForeignKey("registration.id"))
    type = Column(String)
    amount = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    registration = relationship("Registration", back_populates="movements")