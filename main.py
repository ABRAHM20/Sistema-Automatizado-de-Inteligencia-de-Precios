from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime # <--- 1. NUEVA IMPORTACIÓN DE PYTHON

from database.db import engine
from models.producto import Base
from routes.routes import app as rutas_bot

from scrapper.main_scraper import enviar

def tarea_reporte_automatico():
    print("🤖 Ejecutando tarea programada: Buscando precios...")
    enviar() 

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("⏳ Iniciando servidor: Revisando la base de datos...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tablas sincronizadas.")
    
    # ❌ 2. BORRA la llamada manual que te hice poner antes (tarea_reporte_automatico())
    
    scheduler = AsyncIOScheduler()
    # ✅ 3. Le agregamos 'next_run_time=datetime.now()' para que el primer reporte sea inmediato
    scheduler.add_job(tarea_reporte_automatico, 'interval', hours=4, next_run_time=datetime.now())
    scheduler.start()
    print("⏰ Programador de reportes iniciado (Primer envío ahora, luego cada 4 horas).")
    
    yield  # Aquí el servidor abre la puerta del puerto 8000
    
    scheduler.shutdown()
    print("🛑 Servidor y programador apagados correctamente.")

app = FastAPI(title="API Bot de Precios", lifespan=lifespan)
app.include_router(rutas_bot)

@app.get("/")
def ruta_raiz():
    return {"mensaje": "¡Hola! Soy tu API y estoy esperando los precios del scraper."}