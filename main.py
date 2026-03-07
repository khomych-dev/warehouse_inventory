import os
import json
import uuid
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

DB_FILE = "warehouse.json"

class SparePart(BaseModel):
    id: Optional[str] = None
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

@app.get('/')
def read_root():
    return {'message': "Warehouse System Online with JSON storage"}

@app.get('/status')
def get_status():
    return {'status': 'Operational', 'fuel_level': '100%'}

@app.get('/tools')
def get_tools():
    tools_list = ['Wrench', 'Hammer', 'Screwdriver', 'Multimeter']
    return {'tools': tools_list}
    
@app.get('/parts')
def get_all_parts():
    return {'inventory': warehouse_db}

@app.get("/part/{part_id}")
def get_part_name(part_id: str):
    for item in warehouse_db:
        if item['id'] == part_id:
            return item
    return {'error': "Part not found"}

@app.delete("/part/{part_id}")
def delete_part_by_id(part_id: str):
    for item in warehouse_db:
        if item['id'] == part_id:
            warehouse_db.remove(item)
            save_data(warehouse_db)
            return {"message": f"Part with ID {part_id} has been deleted"}
    
    return {"error": "No item with this ID was found"}

@app.put("/part/{part_id}/{new_quantity}")
def updating_quantity(part_id: str, new_quantity: int):
    for item in warehouse_db:
        if item['id'] == part_id:
            item['quantity'] = new_quantity
            save_data(warehouse_db)
            return item
        
    return {"error": f"Item {part_id} not found"}

@app.post('/add-part')
def add_part(part: SparePart):
    item = part.model_dump()
    item['id'] = str(uuid.uuid4())
    warehouse_db.append(item)
    save_data(warehouse_db)
    return {'message': f"Part {part.name} added to list", 'count': len(warehouse_db)}