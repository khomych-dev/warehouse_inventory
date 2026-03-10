from sqlalchemy import Column, String, Float, Integer
from database import Base


class DBPart(Base):
    __tablename__ = "parts"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    category = Column(String)