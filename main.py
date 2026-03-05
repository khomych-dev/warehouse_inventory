from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SparePart(BaseModel):
    name: str
    price: float
    quantity: int
    category: str

@app.get("/")
def read_root():
    return {"message": "Warehouse System Online, Bratishka"}

@app.get("/status")
def get_status():
    return {"status": "Operational", "fuel_level": "100%"}

@app.get('/tools')
def get_tools():
    tools_list = ["Wrench", "Hammer", "Screwdriver", "Multimeter"]
    return {'tools': tools_list}

@app.post("/add-part")
def add_part(part: SparePart):
    return {
        "message": f"Item '{part.name}' successfully added!",
        "received_data": part
    }