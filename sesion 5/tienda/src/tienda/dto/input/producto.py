from pydantic import BaseModel

class ProductoNuevo(BaseModel):
    nombre: str
    precio: float

