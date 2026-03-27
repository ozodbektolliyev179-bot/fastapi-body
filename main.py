from typing import Annotated, Optional

from fastapi import FastAPI, Path, Query

from schemas import Data, ProductCreate, ProductUpdate
from schemas import BookCreateSchema, BookResponseSchema

app = FastAPI(title='Request Body bilan ishlash')

products: list[dict] = []


@app.post('/api/products')
async def create_product(data: ProductCreate):
    print(data.model_dump())

    products.append(data)
    return {'message': 'ok'}


@app.post('/api/calculate')
async def calculate(data: Data):
    if data.operator == '+':
        return {'result': data.a + data.b}
    elif data.operator == '-':
        return {'result': data.a - data.b}
    elif data.operator == '*':
        return {'result': data.a * data.b}
    elif data.operator == '/':
        return {'result': data.a / data.b}
    else:
        return {'error': 'operator not found'}


@app.put('/api/products/{product_id}')
async def udpate_product(
    product_id: Annotated[int, Path(ge=1)],
    product_data: Optional[ProductUpdate] = None,
    notefy: Annotated[bool, Query()] = False,
):
    print(product_id)
    print(product_data)
    print(notefy)

    return {'message': 'ok'}


# POST /api/books
app = FastAPI()

books = []


@app.post("/api/books", response_model=BookResponseSchema)
def create_book(book: BookCreateSchema):
    new_book = {
        "id": len(books) + 1,
        **book.model_dump()
    }

    books.append(new_book)
    return new_book
{
    "title": '',
    "descrioption": '',
    "isbn": 321412,
    "published_date": 'datetime format',
    "auhor": {
        "first_name": 'str',
        "last_name": 'str',
        "birth_date": 'date',
    },
    "images": [
        {
            "name": "str",
            "url": ''
        }
    ]
}