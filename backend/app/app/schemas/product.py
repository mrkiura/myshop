from pydantic import BaseModel, HttpUrl

from typing import Sequence, Optional
from pydantic import Field


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    image_url: Optional[HttpUrl] = Field(
        "https://public130922.s3.eu-west-2.amazonaws.com/default-image.jpeg",
        example="htttp://example/com/jpeg",
        description="An image of the product"
    )


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    id: int


class ProductUpdateRestricted(BaseModel):
    id: int
    name: str


class ProductInDBBase(ProductBase):
    id: int

    class Config:
        orm_mode = True


class Product(ProductInDBBase):
    pass


class ProductInDB(ProductInDBBase):
    pass


class ProductSearchResults(BaseModel):
    results: Sequence[Product]
