"""Subarreglo maximo: fuerza bruta y divide y venceras."""
 
def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).
 
    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.
 
    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    # implemente la solucion en Θ(n²): acumule la suma dentro del
    # ciclo en vez de recalcularla desde cero para cada par.

    n = len(valores)
    mejor_inicio, mejor_fin = 0,0
    suma_maxima = float("-inf")

    for i in range(n):
        suma = 0
        for j in range(i, n):
            suma += valores[j]

            if suma > suma_maxima:
                suma_maxima = suma
                mejor_inicio = i
                mejor_fin = j

    return mejor_inicio, mejor_fin, suma_maxima


 
def suma_cruzada(valores: list[float], inicio: int, medio: int, fin: int) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.
 
    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).
 
    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    # barrido lineal desde el punto medio hacia cada lado.
 
    suma = 0
    suma_maxima_izquierda = float("-inf")
    mejor_inicio = medio
    for i in range(medio, inicio-1, -1):
        suma += valores[i]
        if suma > suma_maxima_izquierda:
            suma_maxima_izquierda = suma
            mejor_inicio = i
            
    suma = 0
    suma_maxima_derecha = float("-inf")
    mejor_fin = medio + 1
    for j in range(medio+1, fin+1):
        suma += valores[j]
        if suma > suma_maxima_derecha:
            suma_maxima_derecha = suma
            mejor_fin = j

    return mejor_inicio, mejor_fin, suma_maxima_izquierda + suma_maxima_derecha



def subarreglo_maximo(valores: list[float], inicio: int, fin: int) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.
 
    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).
 
    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    # caso base, dos llamadas recursivas, caso cruzado y combinar.

    if inicio == fin:
        return inicio, fin, valores[inicio]
 
    medio = (inicio + fin) // 2
 
    izquierdo = subarreglo_maximo(valores, inicio, medio)
    derecho = subarreglo_maximo(valores, medio + 1, fin)
    cruzado = suma_cruzada(valores, inicio, medio, fin)
 
    mejor = izquierdo
    if cruzado[2] > mejor[2]:
        mejor = cruzado
    if derecho[2] > mejor[2]:
        mejor = derecho
    return mejor


if __name__ == "__main__":

    serie = [-3, 5, -2, 8, -6, 3, 9, -4]

    #serie2 = [-3, -5, -2, 8, -6, 3, 9, -4] # OTRA PRUEBA
    #serie3 = [-3, 5, -2, -8, -6, 3, 9, -4] # OTRA PRUEBA

    ultimo = len(serie) - 1
    medio = ultimo // 2
 
    print(f"Serie: {serie}")
 
    inicio_fb, fin_fb, suma_fb = subarreglo_fuerza_bruta(serie)
    print(f"Fuerza bruta        :  dia {inicio_fb + 1} al {fin_fb + 1}, "
          f"suma = {suma_fb}")
 
    inicio_scr, fin_scr, suma_scr = suma_cruzada(serie, 0, medio, ultimo)
    print(f"Suma cruzada        :  dia {inicio_scr + 1} al {fin_scr + 1}, "
          f"suma = {suma_scr}")
 
    inicio_dv, fin_dv, suma_dv = subarreglo_maximo(serie, 0, ultimo)
    print(f"Divide y venceras   :  dia {inicio_dv + 1} al {fin_dv + 1}, "
          f"suma = {suma_dv}")
    
# from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo
 
# serie = [-3, 5, -2, 8, -6, 3, 9, -4]
# assert subarreglo_fuerza_bruta(serie)[2] == 17
# assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17