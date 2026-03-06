from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class SparePart(BaseModel):
    name: str
    price: float
    quantity: int
    category: str
    
warehouse_db = []

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
    
@app.get("/parts")
def get_all_parts():
    return {"inventory": warehouse_db}

@app.post("/add-part")
def add_part(part: SparePart):
    warehouse_db.append(part)
    return {"message": f"Part {part.name} added to list", "count": len(warehouse_db)}