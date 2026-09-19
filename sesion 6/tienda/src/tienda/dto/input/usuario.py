from pydantic import BaseModel

class LoginUsuario(BaseModel):
    email: str
    password: str

class RegistroUsuario(BaseModel):
    email: str
    nombre: str
    password: str
