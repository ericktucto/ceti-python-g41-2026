mi_diccionario = {
    "nombre": "Erick",
    "apellido": "Tucto",
    "edad": 18
}
print(mi_diccionario)

mi_diccionario["nombre"] = "Juan"
print(mi_diccionario)

mi_diccionario["pais"] = "Peru"
print(mi_diccionario)

for clave in mi_diccionario:
    print(clave)

print("-" * 15)

for val in mi_diccionario.values():
    print(val)

print("-" * 15)

for clave, valor in mi_diccionario.items():
    print(clave, valor)


print("-" * 15)

nums = {30, 1, 2, 2, 3, 3, 4, 5, 7}
print(nums)

ciudades = {"Lima", "Quito", "La Paz"}
print(ciudades)
dias = set(["viernes", "sabado", "domingo"])
print(dias)

dias.add("lunes")
print(dias)
dias.discard("viernes")
print(dias)
print(len(dias))

print("viernes" in dias)