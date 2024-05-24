def calcular_promedio(*numeros):
  print(len(numeros))
  return f"El promedio es: {round(sum(numeros) / len(numeros),2)}" if len(numeros) >= 0 else "No hay suficientes numeros para calcular un Promedio"

print(calcular_promedio(6,5,5,4,3))
