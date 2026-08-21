def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"

def es_par(numero: int) -> bool:
    return numero % 2 == 0

def area_rectangulo(
    base: float,
    altura: float = 1
) -> float:
    return base * altura


print(saludar("Claudio"))
print(es_par(13))
print(es_par(8))
print(area_rectangulo(5))
print(area_rectangulo(8, 3))