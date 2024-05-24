try:
   
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    resultado = num1 / num2

except ValueError:
    print("Error: Debe ingresar números válidos.")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

else:
    print("El resultado de la división es:", resultado)

finally:
    print("Fin del programa.")