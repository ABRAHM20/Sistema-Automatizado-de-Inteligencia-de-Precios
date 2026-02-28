from database.db import Base
from sqlalchemy.types import Integer,String, DECIMAL,Date
from sqlalchemy import Column
import datetime

class producto(Base):
    __tablename__="producto"
    id=Column(Integer,primary_key=True, autoincrement=True)
    nombre=Column(String)
    precios_web1=Column(DECIMAL(10,2))
    precios_web2=Column(DECIMAL(10,2))
    fecha_reporte=Column(Date,default=datetime.date.today)





