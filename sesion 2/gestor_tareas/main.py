from tareas import cargar_tareas, agregar_tarea, guardar_tareas, mostrar_tareas, marcar_completada

def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir (guardando)")


def main():
    lista_tareas = cargar_tareas()

    while True:
        #print(lista_tareas)
        mostrar_menu()
        opcion = input("Elige una opción.: ")
        try:
            opcion = int(opcion)
        except ValueError:
            print("Opción no valida")
            continue
        if opcion == 1:
            texto = input("Nueva tarea: ")
            agregar_tarea(lista_tareas, texto)
            print("Tarea agregada.")
        elif opcion == 2:
            mostrar_tareas(lista_tareas)
            pass
        elif opcion == 3:
            mostrar_tareas(lista_tareas)
            index = input("Elige una tarea que deseas marcar como completada.: ")
            try:
                index = int(index)
                marcar_completada(index - 1, lista_tareas)
            except ValueError:
                print("No existe la tarea.")
                pass
            pass
        elif opcion == 4:
            guardar_tareas(lista_tareas)
            print("Tareas guardadas.")
            break
        else:
            print("La opción no es valida.")


main()
