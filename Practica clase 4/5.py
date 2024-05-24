def dame_args(*args):
  if len(args) < 2:
    print("Error: No se han pasado suficientes argumentos.")
    
def dame_args2(*args):
  return print("Error: No se han pasado suficientes argumentos.") if len(args) < 2 else print()

def dame_args3(*args):
  try:
    if len(args) < 2:
      raise ValueError("No se han pasado suficientes argumentos.")
  except ValueError as e:
    print(f"Error: {e}")
    
#dame_args()
#dame_args(1)
#dame_args(1, 2)

#dame_args2()
#dame_args2(1)
#dame_args2(1, 2)

#dame_args3()
#dame_args3(1)
#dame_args3(1, "hola")

#Este es un ejemplo , que les envie por el grupo

def sumatoria(*args):
    s = 0
    try:
        if len(args) < 2:
            raise ValueError("No hay suficientes numeros para sumar.")
        else:
            for n in args:
                if isinstance(n, (int,float)):
                    if n < 0:
                        raise ValueError("Solo se admiten valores positivos.")
                    else:
                        s += n
                else:
                    raise ValueError("Solo se admiten valores numericos.")
    except ValueError as e:
        s = f"Error: {e}"
    
    return print(s)

sumatoria(1,2)
sumatoria(1)
sumatoria(1,2,-5)
sumatoria(1,2,"hola")
sumatoria(1,2,3.2)

