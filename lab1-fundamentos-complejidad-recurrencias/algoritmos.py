"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""
 
 
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    
    lista = list(datos)
    comparaciones = 0
 
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        # Se cuenta cada comparacion entre dos elementos de la lista.
        # La condicion j >= 0 es de indices, no de elementos: no se cuenta.
        while j >= 0:
            comparaciones += 1
            if lista[j] < clave: # "<" Para ordenar descendente y ">" para ordenar de forma ascendente: En este caso vamos a trabajar de forma descendente para darle prioridad a los pacientes con mayor indice de riesgo
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        lista[j + 1] = clave
 
    return lista, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    if len(datos) <= 1:
        return list(datos), 0

    mitad = len(datos) // 2

    izquierda, comparaciones_izquierda = merge_sort(datos[:mitad])
    derecha, comparaciones_derecha = merge_sort(datos[mitad:])

    resultado = []
    i = 0
    j = 0
    comparaciones = (
        comparaciones_izquierda + comparaciones_derecha
    )

    while i < len(izquierda) and j < len(derecha):
        # Se cuenta cada comparación entre dos elementos.
        comparaciones += 1

        # Orden descendente: primero el mayor índice de riesgo.
        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado, comparaciones


def main () -> None:
    """Ejecución lógica del programa"""
    indices_riesgo = [
        34, 12, 45, 2, 6, 24, 10, 4, 23, 20, 32, 48, 19, 7, 39, 15, 28, 5, 41, 17, 50, 8, 31, 
        22, 32, 46, 11, 3, 27, 14, 36, 49, 1, 25, 43, 9, 33, 20, 47, 6, 30, 
        16, 38, 4, 24, 42, 13, 35, 18, 29, 44, 10, 37, 21, 40, 26, 32
    ] #57 registros con valores repetidos

    ##orden_asc = list(range(1, 100001)) # PRUEBA

    lista_ordenada = insertion_sort(indices_riesgo)# Insertion sort ya trabaja sobre una copia

    
    lista_ordenada_merge_sort = merge_sort(indices_riesgo)# Insertion sort ya trabaja sobre una copia

    print("\nLista ordenada de forma descentente insertion sort: \n", lista_ordenada)
    print("\nLista ordenada de forma descentente merge sort: \n", lista_ordenada_merge_sort)
    print("\nLista original: \n", indices_riesgo)

    


if __name__ == "__main__":
   main()