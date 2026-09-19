from pydantic import BaseModel


class NuevoProducto(BaseModel):
    nombre: str
    precio: float

class ActualizarProducto(BaseModel):
    nombre: str
    precio: float
