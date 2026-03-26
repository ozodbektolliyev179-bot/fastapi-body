from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Request Body bilan ishlash')


@app.post('/api/products')
async def create_product(
    data: dict
):
    return data

# POST /api/calculate {"a": 3, "b": 4, "operator": "+"} -> {"result": 7}

class CalculateRequest(BaseModel):
    a: float
    b: float
    operator: str


@app.post("/api/calculate")
def calculate(data: CalculateRequest):
    if data.operator == "+":
        result = data.a + data.b
    elif data.operator == "-":
        result = data.a - data.b
    elif data.operator == "*":
        result = data.a * data.b
    elif data.operator == "/":
        if data.b == 0:
            return {"error": "0 ga bo‘lish mumkin emas"}
        result = data.a / data.b
    else:
        return {"error": "Noto‘g‘ri operator"}

    return {"result": result}



app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    pages: int

@app.post("/api/books")
def create_book(book: Book):
    return {
        "message": "Book created successfully",
        "data": book
    }