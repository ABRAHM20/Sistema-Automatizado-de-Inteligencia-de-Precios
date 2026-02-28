from pydantic import Field, BaseModel
import datetime
class schema_product(BaseModel):
    nombre: str
    precios_web1: float
    precios_web2: float


