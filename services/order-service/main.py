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


class Order(BaseModel):
    id: int
    product_id: int
    user_id : int

orders = [
{"id":1001, "product_id": 101, "user_id": 1},
{"id":1002, "product_id": 102, "user_id": 2}
]

@app.get("/")
def root():
    return {"message":"Order service is running"}

@app.get("/")
def get_orders():
    return orders

@app.post("/orders")
def create_order(order: Order):
    orders.append(order.dict())
    return {"order_create": order}

