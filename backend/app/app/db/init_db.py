import logging
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db import base  # noqa: F401
from app.core.config import settings

logger = logging.getLogger(__name__)


PRODUCTS = [
    {
        "id": 1,
        "name": "Apple",
        "description": "Edible fruit produced by an apple tree",
        "price": 1.99,
    },
    {
        "id": 2,
        "name": "Book",
        "description": "Reference book",
        "price": 100,
    },
    {
        "id": 3,
        "name": "Car",
        "description": "Second hand in pristine condtion",
        "price": 20000,
    },
]


def init_db(db: Session) -> None:
    if settings.FIRST_SUPERUSER:
        user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
        if not user:
            user_in = schemas.UserCreate(
                full_name="Initial Super User",
                email=settings.FIRST_SUPERUSER,
                is_superuser=True,
                password=settings.FIRST_SUPERUSER_PW,
            )
            user = crud.user.create(db, obj_in=user_in)  # noqa: F841
        else:
            logger.warning(
                "Skipping creating superuser. User with email "
                f"{settings.FIRST_SUPERUSER} already exists. "
            )

        for product in PRODUCTS:
            product_in = schemas.ProductCreate(
                name=product.get("name"),
                description=product.get("description"),
                price=product.get("price"),
            )
            crud.product.create(db, obj_in=product_in)
    else:
        logger.warning(
            "Skipping creating superuser.  FIRST_SUPERUSER needs to be "
            "provided as an env variable. "
            "e.g.  FIRST_SUPERUSER=admin@api.coursemaker.io"
        )
