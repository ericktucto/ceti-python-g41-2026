from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlmodel import select

from tienda.db import SessionDep
from tienda.dto.input.producto import ActualizarProducto, NuevoProducto
from tienda.dto.input.usuario import LoginUsuario, RegistroUsuario
from tienda.jwt import encode
from tienda.models.producto import Producto
from tienda.models.usuario import Usuario
from tienda.hashing import pwd

app = FastAPI()

# autenticacion

@app.post("/api/auth/login")
def iniciar_sesion(datos_usuario: LoginUsuario, session: SessionDep):
    usuario = session.exec(
        select(Usuario).where(Usuario.email == datos_usuario.email)
    ).first()
    if usuario is None:
        return JSONResponse(
            status_code=422,
            content={
                "detail": "Credenciales invalida"
            }
        )

    checked = pwd.verify(datos_usuario.password, usuario.password)
    if checked is False:
        return JSONResponse(
            status_code=422,
            content={
                "detail": "Credenciales invalida"
            }
        )

    token = encode({
        "usuario_id": usuario.id,
    })

    return JSONResponse(
        content={
            "token": token,
            "id": usuario.id,
            "email": usuario.email,
            "nombre": usuario.nombre,
        }
    )


@app.post("/api/auth/registro")
def registra_usuario(datos_usuario: RegistroUsuario, session: SessionDep):
    usuario_email = session.exec(
        select(Usuario).where(Usuario.email == datos_usuario.email)
    ).first()
    if usuario_email is not None:
        return JSONResponse(
            status_code=422,
            content={
                "detail": "Correo no disponible"
            }
        )

    password_hash = pwd.hash(datos_usuario.password)
    nuevo_usuario = Usuario(
        nombre=datos_usuario.nombre,
        email=datos_usuario.email,
        password=password_hash,
    )
    session.add(nuevo_usuario)
    session.commit()

    return JSONResponse(
        content={
            "id": nuevo_usuario.id,
            "email": nuevo_usuario.email,
            "nombre": nuevo_usuario.nombre,
        }
    )

# navegador -> [POST] http://localhost:8000/api/productos {json} -> servidor (fastapi)
@app.post("/api/productos")
def guardar_productos(producto: NuevoProducto, session: SessionDep):
    nuevo_producto = Producto(
        nombre=producto.nombre,
        precio=producto.precio,
    )
    session.add(nuevo_producto)
    session.commit()

    return JSONResponse(
        content={
            "id": nuevo_producto.id,
            "nombre": nuevo_producto.nombre,
            "precio": nuevo_producto.precio,
        }
    )


# CRUD de productos

@app.get("/api/productos")
def todos_los_productos(session: SessionDep):
    return session.exec(
        select(Producto)
    ).all()

@app.get("/api/productos/{id}")
def un_producto(id: int, session: SessionDep):
    return session.exec(
        select(Producto).where(Producto.id == id)
    ).first()

@app.delete("/api/productos/{id}")
def eliminar_producto(id: int, session: SessionDep):
    producto = session.get(Producto, id)
    if producto is None:
        return JSONResponse(
            status_code=404,
            content={"detail": "Producto no encontrado"}
        )
    session.delete(producto)
    session.commit()
    return JSONResponse(status_code=200, content={"detail": "Producto eliminado"})

@app.put("/api/productos/{id}")
def actualizar_producto(id: int, producto: ActualizarProducto, session: SessionDep):
    producto_db = session.get(Producto, id)
    if producto_db is None:
        return JSONResponse(
            status_code=404,
            content={"detail": "Producto no encontrado"}
        )
    producto_db.nombre = producto.nombre
    producto_db.precio = producto.precio
    session.commit()
    return JSONResponse(status_code=200, content={"detail": "Producto actualizado"})
