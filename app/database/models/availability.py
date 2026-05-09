from sqlalchemy import Column, Integer, ForeignKey

from app.database.connection import Base

class Availability(Base):
    __tablename__ = "availability"

    branch_office_id = Column(Integer, ForeignKey("branch_office.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
