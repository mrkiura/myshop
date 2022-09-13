from pydantic import BaseModel
from .product import Product
from typing import List, Dict


class CartItem(BaseModel):
    quantity: int =  1
    price: float
    name: str
    product_id: str


class CartBase(BaseModel):
    items: Dict[str: dict]

