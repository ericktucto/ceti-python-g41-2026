with open("data.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, soy Erick\r\n")

with open("dias.txt", "r", encoding="utf-8") as ar:
    for linea in ar:
        print(linea)