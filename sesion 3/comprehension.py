# List Comprehension
# [expresion for variable in iterable condicional]

# Set Comprehension
# {expresion for variable in iterable condicional}

# Dict Comprehension
# {clave: valor for variable in iterable condicional}

precios_dolares = {
    "pan": 3,
    "mantequilla": 2,
    "mermelada": 4
}
print("Precio de productos en dolares", precios_dolares)
precios_soles = { clave: valor * 3.5 for clave, valor in precios_dolares.items() }
print("Precio de productos en soles", precios_soles)

alumnos = {
    "Ana": 8,
    "Juan": 18,
    "Carlos": 5,
    "Pedro": 15,
    "Juana": 10
}

alumnos_aprobados = { nombre: nota for nombre, nota in alumnos.items() if nota >= 11 }
print("Alumno aprobados", alumnos_aprobados)

print("Lista de 1-10", range(1, 11))
print("Numeros pares", [n for n in range(1, 11) if n % 2 == 0])