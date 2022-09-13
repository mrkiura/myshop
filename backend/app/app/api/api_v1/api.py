from fastapi import APIRouter

from app.api.api_v1.endpoints import product, auth, cart


api_router = APIRouter()
api_router.include_router(product.router, prefix="/products", tags=["products"])
api_router.include_router(cart.router, prefix="/cart", tags=["cart"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
