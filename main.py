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

fake_bd = []