from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    email: str

#class Usuario:
#    def  __init__(self, nombre, email):
#        self.nombre = nombre
#        self.email = email
#
#    def __str__(self):
#        return f"Usuario(nombre={self.nombre}, email={self.email})"


u = Usuario("Juan", "juan@gmail.com")

print(str(u) + " <- esto es un usuario")