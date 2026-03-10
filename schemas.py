from pydantic import BaseModel
from typing import Optional


class SparePart(BaseModel):
    id: Optional[str] = None
    name: str
    price: float
    quantity: int
    category: str