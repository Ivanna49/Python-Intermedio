try:
    with open("archivo.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo 'archivo.txt' no existe. Intentando crearlo...")
    with open("archivo.txt", "w") as f:
        f.write("Este es un nuevo archivo.")
