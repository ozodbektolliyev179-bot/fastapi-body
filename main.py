from typing import Annotated, Optional

from fastapi import FastAPI, Path, Query

from schemas import Data, ProductCreate, ProductUpdate, BookCreate


app = FastAPI(title='Request Body bilan ishlash')

products: list[dict] = []
books: list[dict] = []


@app.post('/api/products')
async def create_product(data: ProductCreate):
    print(data.model_dump())

# POST /api/calculate {"a": 3, "b": 4, "operator": "+"} -> {"result": 7}


@app.post('/api/calculate')
async def calculate(
    data: dict
):
    a = data['a']
    b = data['b']
    op = data['operator']

    if op == '+':
        result = a + b
        return {"result": result}
    elif op == '-':
        result = a - b
        return {"result": result}
    elif op == '/':
        result = a / b
        return {"result": result}
    elif op == '*':
        result = a * b
        return {"result": result}
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


@app.post('/api/books')
async def create_book(data: BookCreate):
    book = data.model_dump()
    books.append(book)

    return {'message': 'ok'}