from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from tienda.dto.input.producto import ProductoNuevo
from tienda.dto.output.producto import ProductoRespuesta

app = FastAPI()

@app.get("/")
def hola():
    return JSONResponse(
        content={
            "message": "hola mundo"
        }
    )

@app.post("/productos", responses={
    200: {"model": ProductoRespuesta}
})
def guardar_producto(producto: ProductoNuevo):
    # guarda producto
    return producto
