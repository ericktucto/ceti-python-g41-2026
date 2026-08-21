numero_1 = 0
numero_2 = 0

while True:
    try:
        numero_1 = int(input("Dame el primer numero: "))
        numero_2 = int(input("Dame el segundo numero: "))
        break
    except ValueError:
        print("No colocastes un numero valido")

def divide(a, b):
    try:
        return a / b
    except:
        print(f"No puedes dividir entre cero")
        return 0


print(divide(numero_1, numero_2))
