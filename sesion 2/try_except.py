edad = 0
while True:
    try:
        edad = int(input("Dime tu edad: "))
        break
    except ValueError:
        print("El valor de tu edad debe ser en numero")

print(edad * 5)