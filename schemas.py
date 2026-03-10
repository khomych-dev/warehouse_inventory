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

class SparePart(BaseModel):
    id: Optional[str] = None
    name: str
    price: float
    quantity: int
    category_id: int