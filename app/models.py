from sqlalchemy import Column, Integer, String, Numeric
from .database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    precio = Column(Numeric(10, 2), nullable=False) # <--- Cambiado a Numeric
    stock = Column(Integer, nullable=False)
    categoria = Column(String(50))