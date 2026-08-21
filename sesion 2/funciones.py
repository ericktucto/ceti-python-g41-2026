def saludar(usuario):
    print(f"Hola, {usuario}")

saludar("Erick")
saludar("Juan")
saludar("Peter")

def hola(nombre):
    return f"Hola, soy {nombre}"

mensaje = hola("Pedro")
print(mensaje)

x = 5
def suma():
    y = 10
    return x + y

print(suma())
# print(y) # lanza error por que y solo vive  dentro de suma

def area(
    base: float,
    altura: float
) -> float:
    """Calcula la area de un rectangulo
    """
    return base * altura

print(area(5.5, 5))