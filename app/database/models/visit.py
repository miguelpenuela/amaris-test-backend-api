from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.database.connection import Base

class Visit(Base):
    __tablename__ = "visit"

    id = Column(Integer, primary_key=True)
    branch_office_id = Column(Integer, ForeignKey("branch_office.id"))
    customer_id = Column(Integer, ForeignKey("customer.id"))
    visit_date = Column(DateTime)
