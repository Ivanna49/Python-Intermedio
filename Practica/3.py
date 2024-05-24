diccionario = {"a": 1, "b": 2}

try:
    valor = diccionario["c"]
except KeyError:
    print("La clave 'c' no existe.")
