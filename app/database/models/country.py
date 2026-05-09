from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    name = Column(String)
