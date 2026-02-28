from fastapi import APIRouter, Depends
from database.db import get_db
from sqlalchemy.orm import Session
from schemas.schema_producto import schema_product
from models.producto import producto
import httpx
from sqlalchemy.ext.asyncio import AsyncSession
import os
from dotenv import load_dotenv

#HAY QUE CREAR LE ENV

load_dotenv()
token_id=os.getenv("TOKEN_ID")
canal_id=os.getenv("CHAT_ID")
url_api=f"https://api.telegram.org/bot{token_id}/sendMessage"

app=APIRouter()

#bot telegramn
async def send_message(data: schema_product):
    diferencia = abs(data.precios_web1 - data.precios_web2)
    
    mensaje = f"""
📦 <b>Producto:</b> {data.nombre}
💰 <b>Precio Web 1:</b> ${data.precios_web1:.2f}
💰 <b>Precio Web 2:</b> ${data.precios_web2:.2f}
📊 <b>Diferencia:</b> ${diferencia:.2f}
    """

    payload = {
        "chat_id": canal_id, 
        "text": mensaje,
        "parse_mode": "HTML"
    }

    async with httpx.AsyncClient() as client: 
        response = await client.post(url_api, json=payload)
        return response.json()

    


#base de datos
@app.post("/create")
async def message(product: schema_product, db: AsyncSession = Depends(get_db)):
    producto_nuevo=producto(
        nombre=product.nombre,
        precios_web1=product.precios_web1,
        precios_web2=product.precios_web2
    )
    db.add(producto_nuevo)
    await db.commit()
    await db.refresh(producto_nuevo)

    await send_message(producto_nuevo)

    return {"status": "success", "data": product.nombre}









