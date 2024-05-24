try:
    numero = int(input("Ingrese un numero: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
else:
    print(resultado)
