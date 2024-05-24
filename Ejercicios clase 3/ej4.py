try:
    with open('archivo.txt', 'r') as file:
        contenido = file.read()
    print("Contenido del archivo:", contenido)

except FileNotFoundError:
    print("El archivo no existe. Creando el archivo...")

    try:
        with open('archivo.txt', 'w') as file:
            file.write("Este es un nuevo archivo creado.")

    except Exception as e:
        print("Error al crear el archivo:", e)

else:
    print("¡El archivo se ha abierto con éxito!")
finally:
    print("Fin del programa.")