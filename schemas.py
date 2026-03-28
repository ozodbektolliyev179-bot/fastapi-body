from datetime import datetime

from typing import Annotated, Optional, List
from enum import Enum

from pydantic import BaseModel, Field, HttpUrl


class Data(BaseModel):
    a: float
    b: float
    operator: str


class ProductStatus(str, Enum):
    new: str = 'yangi'
    old: str = 'eski'


class ProductImage(BaseModel):
    id: int
    url: HttpUrl


class ProductCreate(BaseModel):
    name: Annotated[str, Field(min_length=5, max_length=128)]
    descriptioin: Optional[str] = None
    price: Annotated[float, Field(ge=0, lt=100_000_000)]
    stock: Annotated[int, Field(ge=1)]
    status: ProductStatus
    images: List[ProductImage]


class ProductUpdate(BaseModel):
    name: Annotated[str | None, Field(min_length=5, max_length=128)] = None
    descriptioin: Optional[str] = None
    price: Annotated[float | None, Field(ge=0, lt=100_000_000)] = None
    stock: Annotated[int | None, Field(ge=1)] = None
    status: Optional[ProductStatus] = None


class BookAuthor(BaseModel):
    first_name: Annotated[str, Field(min_length=3)]
    last_name: Annotated[str | None, Field(min_length=3)] = None
    birth_date: datetime | None = None


class BookImages(BaseModel):
    name: Annotated[str, Field(min_length=3)]
    url: HttpUrl


class BookCreate(BaseModel):
    title: Annotated[str, Field(min_length=3)]
    description: Optional[str] = None
    isbn: Annotated[int, Field(gt=0)]
    published_date: datetime
    author: BookAuthor
    images: List[BookImages]