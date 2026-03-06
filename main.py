import os
import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

DB_FILE = "warehouse.json"

class SparePart(BaseModel):
    name: str
    price: float
    quantity: int
    category: str
    
def load_data():
    if not os.path.exists(DB_FILE):
        return []
    
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def save_data(data):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
warehouse_db = load_data()

@app.get("/")
def read_root():
    return {"message": "Warehouse System Online with JSON storage"}

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
    warehouse_db.append(part.model_dump()) 
    save_data(warehouse_db)
    return {"message": f"Part {part.name} added to list", "count": len(warehouse_db)}