numero = int(input("Escribe un numero: "))

if numero % 2 == 0:
    print(f"Tu numero {numero} es par")
else:
    print(f"Tu numero {numero} es impar")


print("-" * 15)

for factor in range(1, 13):
    print(f"{numero} x {factor} = {numero * factor}")