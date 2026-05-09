from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database.connection import Base

class Movement(Base):
    __tablename__ = "movement"

    id = Column(Integer, primary_key=True)
    registration_id = Column(Integer, ForeignKey("registration.id"))
    type = Column(String)
    amount = Column(Integer)
    created_at = Column(DateTime)
