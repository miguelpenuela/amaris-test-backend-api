from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.connection import Base

class Region(Base):
    __tablename__ = "region"

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey("country.id"))
    name = Column(String)
