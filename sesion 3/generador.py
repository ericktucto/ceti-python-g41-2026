def mi_generador():
    #for n in range(10_000_000):
    for n in range(10):
        yield n

for a in mi_generador():
    print(f"valor {a}")

generador = (n for n in range(10))


print(mi_generador)
print(generador)

def fib():
    a, b = 0, 1
    while True:
        a, b = b, b + a
        yield a

for a in fib():
    if a > 100:
        break
    print(f"valor fib {a}")
