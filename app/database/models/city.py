from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.connection import Base

class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    region_id = Column(Integer, ForeignKey("region.id"))
    name = Column(String)
