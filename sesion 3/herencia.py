class Usuario:
    def  __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def presentarse(self):
        return f"Hola, soy {self.nombre}"


class Notificable:
    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}"

    def notificar(self):
        return "Notificando"


class Cliente(Usuario):
    def __init__(self, nombre, email, saldo):
        super().__init__(nombre, email)
        self.saldo = saldo

    def comprar(self, precio):
        self.saldo = self.saldo - precio

    def presentarse(self):
        return f"Hola, soy cliente, {self.nombre}"


class Empresa(Notificable):
    pass


class Vendedor(Usuario):
    def __init__(self, nombre, email, horario):
        super().__init__(nombre, email)
        self.horario = horario

    def presentarse(self):
        return f"Hola, soy vendedor, {self.nombre}"



u1 = Usuario("Tom", "tom@ericktucto.com")

c1 = Cliente("Erick", "erick@ericktucto.com", 5000)

print("Usuario ->", u1.presentarse())
print("Cliente ->", c1.presentarse())
c1.comprar(30)
print("Saldo -> ", c1.saldo)

v1 = Vendedor("John", "john@gmail.com", "part-time")

print("Cliente  ->", c1.presentarse())
print("Vendedor ->", v1.presentarse())