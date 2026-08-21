ciudades = ["Lima", "La Paz", "Madrid", "New York", "Quito"]

print(ciudades[0])
print(ciudades[-1])
print(ciudades[:3])

ciudades.append("Iquitos")
print(ciudades)
ciudades.pop(1)
print(ciudades)

capitales = {
    "Peru": "Lima",
    "Chile": "Santiago",
    "Colombia": "Bogota"
}

for pais, capital in capitales.items():
    print(f"La capital de {pais} es {capital}")