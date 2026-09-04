import random
from productos import cargar_productos, guardar_productos

def mostrar_menu():
    print("\n=== TIENDA VIRTUAL ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir (guardando)")

def main():
    lista_productos = cargar_productos()
    while True:
        print(lista_productos)
        mostrar_menu()
        opcion = input("Elige una opción.: ")
        try:
            opcion = int(opcion)
        except ValueError:
            print("Opción no valida")
            continue
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            guardar_productos(lista_productos)
            print("Tareas guardadas.")
            break
        else:
            print("La opción no es valida.")

main()
