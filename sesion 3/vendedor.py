class Usuario:
    def  __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def presentarse(self):
        return f"Hola, soy {self.nombre}"


class Vendedor(Usuario):
    def __init__(self, nombre, email, horario):
        super().__init__(nombre, email)
        self.horario = horario

    def presentarse(self):
        return  super().presentarse()
        #return f"Hola, soy vendedor, {self.nombre}"



u1 = Usuario("Tom", "tom@ericktucto.com")
v1 = Vendedor("John", "john@gmail.com", "part-time")

print("Usuario ->", u1.presentarse())
print("Vendedor ->", v1.presentarse())