import asyncio

async def hervir():
    await asyncio.sleep(3)
    print("Agua lista")

async def cortar():
    await asyncio.sleep(2)
    print("Verduras listas")

async def main():
    await asyncio.gather(
        hervir(),
        cortar()
    )


asyncio.run(main())


async def get_tareas():
    # 100ms
    response = await http.get("http://api.tareas.com")
    return response

async def get_usuario():
    # 60ms
    filas = await conexion.query("--- query ---")
    return filas


async def inicio():
    # ~100ms
    tareas, filas = await asyncio.gather(
        get_tareas(),
        get_usuario()
    )
