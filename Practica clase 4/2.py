palabras_usuario = input("Ingrese una lista de palabras separadas por comas: ")
palabra_a_buscar = input("Ingrese la palabra a buscar: ")
final_frase = " en la lista."
palabra = palabras_usuario.split(",")

def buscar_palabras(palabra_a_buscar, *lista_palabras):
    palabra_encontrada = palabra_a_buscar in lista_palabras
    print(f"{'no hay palabras'+ final_frase if lista_palabras == "" else 'La palabra ' +  palabra_a_buscar + ' se encuentra' + final_frase if palabra_encontrada else 'no se encuentra' + final_frase } ")
   
buscar_palabras(palabra_a_buscar,*palabra)


