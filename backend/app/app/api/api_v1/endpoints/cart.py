from app.schemas import Product
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.product import Product
from app.models.user import User



router = APIRouter()


@router.post("/add", status_code=201)
def add_to_cart(
    *,
    product_id: str,
    db: Session = Depends(deps.get_db),
    cart: crud.crud_cart.Cart = Depends(deps.get_cart),
    current_user: User = Depends(deps.get_current_user),
) -> dict:
    """
    Add an item to the cart.
    """
    product = crud.product.fetch_one(db, product_id)
    cart.add(product=product, user_id=current_user.id)
    return cart._cart[current_user.id]


@router.post("/remove", status_code=201)
def remove_from_cart(
    *,
    product_id: str,
    db: Session = Depends(deps.get_db),
    cart: crud.crud_cart.Cart = Depends(deps.get_cart),
    current_user: User = Depends(deps.get_current_user),
) -> dict:
    """
    Add an item to the cart.
    """
    cart.remove(product_id, current_user.id)
    return cart[current_user.id]


@router.post("/clear", status_code=201)
def remove_from_cart(
    *,
    db: Session = Depends(deps.get_db),
    cart: crud.crud_cart.Cart = Depends(deps.get_cart),
    current_user: User = Depends(deps.get_current_user),
) -> dict:
    """
    Add an item to the cart.
    """
    cart.clear(current_user.id)
    return cart.summary(current_user.id)


@router.get("/summary", status_code=200)
def cart_summary(
    *,
    cart: crud.crud_cart.Cart = Depends(deps.get_cart),
    current_user: User = Depends(deps.get_current_user),
) -> dict:
    return cart.summary(current_user.id)
