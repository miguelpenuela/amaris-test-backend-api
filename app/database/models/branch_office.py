from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.connection import Base

class BrancOffice(Base):
    __tablename__ = "branch_office"

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey("city.id"))
    name = Column(String)
