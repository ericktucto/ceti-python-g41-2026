from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    email: str

class Cliente(Usuario):
    pass

cliente1 = Cliente("Ana", "a@gmail.com")
print(cliente1)