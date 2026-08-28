def mi_generador():
    #for n in range(10_000_000):
    for n in range(10):
        yield n

for a in mi_generador():
    print(f"valor {a}")

generador = (n for n in range(10))


print(mi_generador)
print(generador)