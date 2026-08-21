contador = 0
while contador <= 20:
    if contador % 3 == 0:
        contador = contador + 1
        continue
    print(f"El valor del contador es: {contador}")
    if contador % 2 == 0:
        print("Contador es par")
    if contador == 16:
        break
    contador = contador + 1
print("Saliste del bucle while")

print("-" * 15)

for numero in range(1, 20):
    if numero % 3 == 0:
        continue
    print(f"El valor del contador es: {numero}")
    if numero % 2 == 0:
        print("Contador es par")
    if numero == 16:
        break