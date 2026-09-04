from dataclasses import dataclass

ARCHIVO = "productos.txt"

@dataclass
class Producto:
    id: int
    nombre: str
    precio: int
    stock: int


def cargar_productos():
    """Lee los productos del archivo y los devuelve"""
    productos = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue

                id, nombre, precio, stock = linea.split("|")
                producto = Producto(int(id), nombre, int(precio), int(stock))

                productos.append(producto)
    except FileNotFoundError:
        print("No existe el archivo de productos")
    return productos

def guardar_productos(productos):
    """Guardar los productos en un archivo."""
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for producto in productos:
            archivo.write(f"{producto.id},{producto.nombre},{producto.precio},{producto.stock}\n")
