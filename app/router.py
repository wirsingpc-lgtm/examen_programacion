from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas, models

# ESTA LÍNEA ES LA QUE FALTA (La definición del router)
router = APIRouter(prefix="/productos", tags=["Productos"])

# 1. OBTENER PRODUCTOS
@router.get("/", response_model=list[schemas.ProductoResponse])
def obtener_productos(db: Session = Depends(get_db)):
    return db.query(models.Producto).all()

# 2. CREAR PRODUCTO
@router.post("/", response_model=schemas.ProductoResponse)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    datos_producto = producto.model_dump() 
    nuevo_p = models.Producto(**datos_producto)
    db.add(nuevo_p)
    db.commit()
    db.refresh(nuevo_p)
    return nuevo_p

# 3. ELIMINAR PRODUCTO
@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return {"mensaje": f"Producto con ID {producto_id} eliminado exitosamente"}

# 4. ACTUALIZAR PRODUCTO
@router.put("/{producto_id}", response_model=schemas.ProductoResponse)
def actualizar_producto(producto_id: int, producto_actualizado: schemas.ProductoCreate, db: Session = Depends(get_db)):
    query = db.query(models.Producto).filter(models.Producto.id == producto_id)
    producto_existente = query.first()
    
    if not producto_existente:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    query.update(producto_actualizado.model_dump())
    db.commit()
    return query.first()