from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Product(BaseModel):
    id: int
    name: str

products = [
{"id":101, "name":"Laptop"},
{"id":102, "name":"Phone"}
]

@app.get("/")
def root():
    return {"message":"Product service is running"}

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def create_products():
    products.append(product.dict())
    return {"product_created": product}

