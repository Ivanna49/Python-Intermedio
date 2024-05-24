try:
    mi_diccionario = {'clave1': 'valor1', 'clave2': 'valor2'}

    valor = mi_diccionario['clave3']

except KeyError:
    print("La clave especificada no existe en el diccionario.")

else:
    print("El valor asociado a la clave es:", valor)

finally:
    print("Fin del programa.")