from typing import Annotated, Optional, List
from enum import Enum
from datetime import date, datetime
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
    # date: datetime

    # @field_validator('date')
    # @staticmethod
    # def validate_date(cls, value: datetime):
    #     if value < datetime(2024, 1, 1):
    #         raise ValueError("datetime must be >= 2024-01-01")
    #     return value


class ProductUpdate(BaseModel):
    name: Annotated[str | None, Field(min_length=5, max_length=128)] = None
    descriptioin: Optional[str] = None
    price: Annotated[float | None, Field(ge=0, lt=100_000_000)] = None
    stock: Annotated[int | None, Field(ge=1)] = None
    status: Optional[ProductStatus] = None




class AuthorSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: date


class ImageSchema(BaseModel):
    name: str
    url: HttpUrl


class BookCreateSchema(BaseModel):
    title: str
    description: str
    isbn: int
    published_date: datetime
    author: AuthorSchema
    images: List[ImageSchema]


class BookResponseSchema(BookCreateSchema):
    id: int

    class Config:
        from_attributes = True