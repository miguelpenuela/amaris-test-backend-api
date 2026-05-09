from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import select

from app.database.models.product import Product
from app.database.models.product_type import ProductType

def get_products(db: Session):
    sql = select(Product).options(joinedload(Product.product_type))
    products = db.execute(sql).scalars().all()
    return products

