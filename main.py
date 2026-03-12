import uuid
from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi import Depends
from models import DBPart
from schemas import SparePart
from schemas import SparePartUpdate
from database import engine, Base, get_db
from schemas import CategoryCreate, CategorySchema
from models import Category
from schemas import ManufacturerCreate, ManufacturerSchema
from models import Manufacturer

EXCLUDED_FIELDS = {"id", "name"}
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': "Warehouse System Online with SQL storage"}

@app.get('/status')
def get_status():
    return {'status': 'Operational', 'fuel_level': '100%'}

@app.get('/tools')
def get_tools():
    tools_list = ['Wrench', 'Hammer', 'Screwdriver', 'Multimeter']
    return {'tools': tools_list}
    
@app.get('/parts')
def get_all_parts(db:Session = Depends(get_db)):
    parts_from_db = db.query(DBPart).all()
    return {'inventory': parts_from_db}

@app.get("/part/{part_id}")
def get_part_by_id(part_id: str, db: Session = Depends(get_db)):
    item = db.query(DBPart).filter(DBPart.id == part_id).first()
    if item:
        return item
    
    return {'error': "Part not found"}

@app.get('/category')
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@app.get('/manufacturer')
def get_manufacturers(db: Session = Depends(get_db)):
    return db.query(Manufacturer).all()

@app.delete("/part/{part_id}")
def delete_part_by_id(part_id: str, db: Session = Depends(get_db)):
    db_item = db.query(DBPart).filter(DBPart.id == part_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return {"message": f"Part with ID {part_id} has been deleted"}
        
    return {"error": "No item with this ID was found"}

@app.patch("/part/{part_id}")
def patch_part(part_id: str, update_part: SparePartUpdate, db: Session = Depends(get_db)):
    db_item = db.query(DBPart).filter(DBPart.id == part_id).first()
    if db_item:
        new_data = update_part.model_dump(exclude_unset=True)
        
        for key, values in new_data.items():
            if key in EXCLUDED_FIELDS:
                continue
            
            setattr(db_item, key, values)
            
        db.commit()
        db.refresh(db_item)
        
        return db_item
    
    return {"error": f"Item {part_id} not found"}

@app.put("/part/{part_id}")
def update_part(part_id: str, updated_part: SparePart, db: Session = Depends(get_db)):
    db_item = db.query(DBPart).filter(DBPart.id == part_id).first()
    if db_item:
        new_data = updated_part.model_dump()
        
        for key, values in new_data.items():
            if key in EXCLUDED_FIELDS or values is None:
                continue
            
            setattr(db_item, key, values)
        
        db.commit()
        db.refresh(db_item)
         
        return db_item
        
    return {"error": f"Item {part_id} not found"}

@app.post('/add-part')
def add_part(part: SparePart, db: Session = Depends(get_db)):
    item_data = part.model_dump()
    item_data.pop('id', None)
    
    new_id = str(uuid.uuid4())
    
    new_db_part = DBPart(id=new_id, **item_data)
    
    db.add(new_db_part)
    db.commit()
    db.refresh(new_db_part)
    
    return {'message': f"Part {new_db_part.name} added to SQL database", 'id': new_db_part.id}

@app.post('/categories', response_model=CategorySchema)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@app.post('/manufacturers', response_model=ManufacturerSchema)
def create_manufacturer(manufacturer: ManufacturerCreate, db: Session = Depends(get_db)):
    new_manufacturer = Manufacturer(name=manufacturer.name)
    db.add(new_manufacturer)
    db.commit()
    db.refresh(new_manufacturer)
    return new_manufacturer