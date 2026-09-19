edad = 0
try:
    edad = int(
        "18" #input("Dime cual es tu edad: ")
    )
except ValueError:
    print("La edad es invalida")

print(type(edad))

def dividir(dividendo, divisor):
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError:
        print("No puedes dividir entre zero")
        return None
    except TypeError:
        print("Ocurrio un error")
        return None
    else:
        print("Estas dentro del else")
        return resultado
    finally:
        print("Fin de la funcion dividir")

print(dividir(10, 0))


def main():
    db = DatabaseConexion() # Conexion
    try:
        # codigo
        pass
    except ValueError:
        print("Ocurrio un error")
    finally:
        db.close()

class SaldoInsuficienteError(Exception):
    pass

def retirar(saldo, monto):

    if monto > saldo:
        raise SaldoInsuficienteError(
            "No tienes suficiente saldo"
        )
    return saldo - monto

print(retirar(500, 1000))


