from fastapi import FastAPI
from app.database import engine, Base
from app.router import router

# Crea las tablas físicamente en MySQL si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mi Proyecto FastAPI")

# Incluimos el router que definimos en app/router.py
app.include_router(router)

@app.get("/")
def inicio():
    return {"mensaje": "API lista. Ve a /docs para probar"}