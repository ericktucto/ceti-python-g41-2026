ARCHIVO = "tareas.txt"

def cargar_tareas():
    """Lee las tareas dentro de un archivo. Devuelve una lista"""
    tareas = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                
                estado, texto = linea.split("|", 1)
                tareas.append({
                    "texto": texto,
                    "hecha": estado == "1"
                })
    except FileNotFoundError:
        print("No existe el archivo de tareas")
    return tareas


def agregar_tarea(tareas, texto):
    tareas.append({
        "texto": texto,
        "hecha": False
    })

def guardar_tareas(tareas):
    """Guardar las tareas en un archivo."""
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            estado = "1" if tarea["hecha"] else "0"
            archivo.write(f"{estado}|{tarea['texto']}\n")

#def marcar_completada...
#def mostrar_tareas...