from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    parts = relationship('DBPart', back_populates='category')
    
class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    parts = relationship('DBPart', back_populates='manufacturer')
    
class DBPart(Base):
    __tablename__ = 'parts'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    manufacture_id = Column(Integer, ForeignKey('manufactures.id'))
    manufacturer = relationship('Manufacturer', back_populates='parts')
    category = relationship('Category', back_populates='parts')