#ANTES 
def CalcularPromedio(Lista):
    s=0
    for x in Lista:
     s=s+x
    return s/len(Lista)
 
l=[1,2,3,4,5]
print(CalcularPromedio(l))

#DESPUES
def calcular_promedio(Lista: list[int]) -> float:
    """Calcular el promedio de una lista de números
   
    Args:
        lista: números enteros a calcular.
 
    Returns:
        Resultado con el promedio aritmético de los valores de la lista.
    """

    suma = 0
    for numero in Lista:
        suma = suma + numero
    return suma / len(Lista)


def main () -> None:
    """Ejecución lógica del programa"""
    lista_numeros=[1,2,3,4,5]
    promedio = calcular_promedio(lista_numeros)

    print(promedio)

if __name__ == "__main__":
   main()
