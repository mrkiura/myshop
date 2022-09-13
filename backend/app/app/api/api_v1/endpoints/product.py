from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.product import (
    Product,
    ProductCreate,
    ProductSearchResults,
    ProductUpdateRestricted,
)
from app.models.user import User

router = APIRouter()


@router.get("/{product_id}", status_code=200, response_model=Product)
def fetch_product(
    *,
    product_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single product by ID.
    """
    result = crud.product.get(db=db, id=product_id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Product with ID {product_id} not found"
        )

    return result


@router.get("/", status_code=200, response_model=ProductSearchResults)
def fetch_products(
    *,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Fetch all products in the catalog.
    """
    products = crud.product.fetch_many(db=db)
    if not products:
        return {"results": list()}

    return {"results": list(products)}


@router.get("/search/", status_code=200, response_model=ProductSearchResults)
def search_products(
    *,
    keyword: str = Query(None, min_length=3, example="apple"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for products based on label keyword
    """
    products = crud.product.fetch_many(db=db, limit=max_results)
    results = filter(lambda product: keyword.lower() in product.name.lower(), products)

    return {"results": list(results)}


@router.post("/", status_code=201, response_model=Product)
def create_product(
    *,
    product_in: ProductCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> dict:
    """
    Create a new product in the database.
    """
    product = crud.product.create(db=db, obj_in=product_in)

    return product


@router.put("/", status_code=201, response_model=Product)
def update_product(
    *,
    product_in: ProductUpdateRestricted,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> dict:
    """
    Update product in the database.
    """
    product = crud.product.get(db, id=product_in.id)
    if not product:
        raise HTTPException(
            status_code=400, detail=f"Product with ID: {product_in.id} not found."
        )

    if product.submitter_id != current_user.id:
        raise HTTPException(
            status_code=403, detail=f"You can only update your products."
        )

    updated_product = crud.product.update(db=db, db_obj=product, obj_in=product_in)
    return updated_product
