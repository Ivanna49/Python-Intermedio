def dividir(numerador, denominador):
  try:
    resultado = int(numerador) / int(denominador)
    
  except ZeroDivisionError:
    resultado = "Error: No se puede dividir por cero."
  except ValueError:
    resultado = "Error: El numerador o el denominador no son válidos."
  
  return resultado

#dividir(1,3)
#dividir(10,0)
#dividir("a",3)


#otra alternativa

def dividirDos(numerador, denominador):
  try:
    resultado = numerador / denominador
  except ZeroDivisionError:
    resultado = "Error: No se puede dividir por cero."

  return resultado


def comprobar(numerador,denominador):
  try:
    numerador = int(numerador)
  except ValueError:
    print("Error: El numerador no es válido.")
  else:
      print(dividirDos(numerador, denominador))

#comprobar(1,3)
#comprobar(10,0)
#comprobar("a",3)