from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hello, World"}

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    stock: bool = True 

fake_bd = {}


@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in fake_bd:
        return {"error": "this already exists"}
    fake_bd[item_id] = item
    return {"item_id": item_id, "item": item}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    
    if item_id not in fake_bd:
        return {"error": "item not found"}
    return {"item_id": item_id, "item": fake_bd[item_id]}


#cambio de prueba