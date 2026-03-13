from pydantic import BaseModel
from typing import Optional


class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategorySchema(CategoryBase):
    id: int

    class Config:
        from_attributes = True

class ManufacturerBase(BaseModel):
    name: str
    
class ManufacturerCreate(ManufacturerBase):
    pass

class ManufacturerSchema(ManufacturerBase):
    id: int
    
    class Config:
        from_attributes = True

class SparePartBase(BaseModel):
    name: str
    price: float
    quantity: int

class SparePartCreate(SparePartBase):
    pass

class SparePart(SparePartBase):
    id: str
    category: Optional[CategorySchema] = None
    manufacturer: Optional[ManufacturerSchema] = None

    class Config:
        from_attributes = True

class SparePartUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    category_id: Optional[int] = None
    manufacturer_id: Optional[int] = None