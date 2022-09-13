from typing import Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.product import Product
from app.models.user import User
from app.schemas.product import ProductCreate, ProductUpdateRestricted, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: User,
        obj_in: Union[ProductUpdate, ProductUpdateRestricted]
    ) -> Product:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj

product = CRUDProduct(Product)
