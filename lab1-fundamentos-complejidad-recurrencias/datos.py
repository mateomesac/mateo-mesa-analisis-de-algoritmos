import random # Importar random para generar las listar aleatoriamente

FRACCION_NO_ORDENADOS = 0.02

"""Generadores de lotes de registros para los escenarios de Tamiza."""
 
def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    generador = random.Random(semilla)
    lote = list(range(n))
    generador.shuffle(lote)
    return lote


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """

    generador = random.Random(semilla)
    cantidad_no_ordenados = round(n * FRACCION_NO_ORDENADOS) #Calcular cuantos registros no están ordenados
    lote = generador.sample(range(n), cantidad_no_ordenados)
    conjunto_no_ordenados = set(lote) # 2% de los datos no ordenados
    ordenados = [i for i in range(n - 1, -1, -1) if i not in conjunto_no_ordenados] # 98% de los datos ordenados
    
    return ordenados + lote



def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).
 
    Args:
        n: cantidad de registros del lote.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    return list(range(n))
    

def main () -> None:
    """Ejecución lógica del programa"""
    lista_orden_aleatorio = generar_aleatorio(10)
    lista_casi_ordenados = generar_casi_ordenado(100)
    lista_orden_inverso = generar_inverso(100)

    print("\nDatos aleatorios: \n", lista_orden_aleatorio)
    print("\nDatos 98% ordenados: \n", lista_casi_ordenados)
    print("\nDatos orden inverso: \n", lista_orden_inverso)

if __name__ == "__main__":
   main()