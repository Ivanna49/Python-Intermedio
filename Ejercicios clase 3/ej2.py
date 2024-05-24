try:
    resultado = 5 + "cadena"

except TypeError:
    print("Error: No se puede sumar un número y una cadena.")

else:
    print("El resultado de la suma es:", resultado)

finally:
    print("Fin del programa.")