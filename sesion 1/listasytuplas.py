frutas = ["manzana", "pera", "mango"]
print(frutas)
print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[1:])
print(frutas[:2])


frutas.append("naranja")

print(frutas)

eliminado = frutas.pop(1)

print(frutas, eliminado)

print(len(frutas))

frutas[0] = "kiwi"
print(frutas)

print("kiwi" in frutas)


print("-" * 15)

mi_tupla = (10, 20)
print(len(mi_tupla), mi_tupla[0])
print(20 in mi_tupla)