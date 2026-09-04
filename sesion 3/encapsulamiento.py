class Cliente:
    def __init__(self, nombre, apellido, saldo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__saldo = saldo


    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"


    @property
    def saldo(self):
        return self.__saldo


    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor

    

c1 = Cliente("Erick", "Tucto", 2500)
print("antes de modificar", c1.nombre_completo)
print("antes de modificar", c1.saldo)

c1.saldo = -1000

print("despues de modificar", c1.saldo)



class Guerrero:
    def __init__(self, vida):
        self.__vida = vida

    @property
    def vida(self):
        return self.__vida


    @vida.setter
    def vida(self, valor):
        if valor >= self.__vida:
            self.__vida = valor
        else:
            self.__vida = 0



g1 = Guerrero(1000)

danio = 3000

g1.vida = g1.vida - danio

print(g1.vida)