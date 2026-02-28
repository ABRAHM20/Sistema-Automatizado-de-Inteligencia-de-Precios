
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy import text
import os
from dotenv import load_dotenv


load_dotenv()
password=os.getenv('DB_PASSWORD')
user=os.getenv('DB_USER')
host=os.getenv('DB_HOST','localhost')

# Configuración
URL_DB = f"postgresql+asyncpg://{user}:{password}@{host}:5432/Articulos"

# 1. El motor (Engine)
engine = create_async_engine(URL_DB, echo=True) # echo=True para ver el SQL en consola

# 2. El fabricador de sesiones (SessionMaker) CONECTA LOS MODELOS CON LA BDD
SessionLocal = async_sessionmaker(
    bind=engine, 
    expire_on_commit=False, 
    class_=AsyncSession
)

Base = declarative_base()

# --- FUNCIONES DE COMPROBACIÓN ---

async def test_connect():
    try:
        async with SessionLocal() as session:
            response= await session.execute(text("SELECT 1"))
            value=response.scalar()
            print("La conexion se hizo con exito")
    except Exception as e:
        print(e)

async def get_db():
    try:
        async with SessionLocal() as session:
            yield session
    except Exception as e:
        print(e)


async def main():
    await test_connect()



    



