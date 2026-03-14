from sqlalchemy import Column, String, Float, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class DBCategory(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    parts = relationship('DBPart', back_populates='category')
    
class DBManufacturer(Base):
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
    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))
    is_active = Column(Boolean, default=True)
    manufacturer = relationship('DBManufacturer', back_populates='parts')
    category = relationship('DBCategory', back_populates='parts')