import matplotlib.pyplot as plt
import random 
import time

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo
)

SEMILLA = 42
REPETICIONES = 5

def generar_datos(n: int) -> list[float]:
    """
    Generar datos con una semilla fija (valores enteros entre -100 y 100)

    Args:
        n: cantidad de días (tamanio lista)

    Returns:
        Arreglo de numeros negativos y positivos    
    """
    datos = [random.randint(-100,100) for _ in range(n)]
    random.shuffle(datos) #Desordenar los elementos de la lista
    return datos

def ejecutar_experimento(tamanios: list[int]) -> tuple[list[float], list[float]]:
    """Mide ambos algoritmos en cada tamanio y verifica sus sumas.
 
    Usa una semilla fija para que los datos sean reproducibles, genera
    una sola lista por tamanio y la usa en los dos algoritmos. 
 
    Args:
        tamanios: tamanios de entrada a medir.
 
    Returns:
        Una tupla (tiempos_fb, tiempos_dv) con el tiempo promedio, en
        segundos, de fuerza bruta y de divide y venceras, en el mismo
        orden que ``tamanios``.
 
    Raises:
        AssertionError: si en algun tamanio las sumas no coinciden.
    """
    random.seed(SEMILLA)
    tiempos_fb: list[float] = []
    tiempos_dv: list[float] = []
 
    print(f"{'n':>6} | {'Fuerza bruta (s)':>17} | "
          f"{'Divide y venceras (s)':>21} | Suma")
    #:>6 - Generar espacio de 6 caracteres
 
    for n in tamanios:
        valores = generar_datos(n)
 
        total_fb = 0.0
        for _ in range(REPETICIONES):
            inicio_reloj = time.perf_counter()
            resultado_fb = subarreglo_fuerza_bruta(valores)
            fin_reloj = time.perf_counter()
            total_fb += fin_reloj - inicio_reloj
 
        total_dv = 0.0
        for _ in range(REPETICIONES):
            inicio_reloj = time.perf_counter()
            resultado_dv = subarreglo_maximo(valores, 0, n - 1)
            fin_reloj = time.perf_counter()
            total_dv += fin_reloj - inicio_reloj
 
        assert resultado_fb[2] == resultado_dv[2], (
            f"Sumas distintas en n = {n}: "
            f"{resultado_fb[2]} != {resultado_dv[2]}"
        )
 
        promedio_fb = total_fb / REPETICIONES
        promedio_dv = total_dv / REPETICIONES
        tiempos_fb.append(promedio_fb)
        tiempos_dv.append(promedio_dv)
        print(f"{n:>6} | {promedio_fb:>17.6f} | {promedio_dv:>21.6f} | "
              f"{resultado_fb[2]}")
 
    return tiempos_fb, tiempos_dv


def graficar_tiempo(tamanios: list[int], tiempos_fb: list[float], tiempos_dv: list[float]) -> None:
    """Grafica tiempo vs n de ambos algoritmos en los mismos ejes.
 
    Args:
        tamanios: tamanios de entrada medidos (eje x).
        tiempos_fb: tiempos de fuerza bruta, en segundos.
        tiempos_dv: tiempos de divide y venceras, en segundos.
 
    Returns:
        None. La grafica se guarda en RUTA_GRAFICA.
    """
    plt.figure()
    plt.plot(tamanios, tiempos_fb, marker="o", label="Fuerza bruta")
    plt.plot(tamanios, tiempos_dv, marker="s", label="Divide y venceras")
    plt.title("Subarreglo maximo: tiempo vs n")
    plt.xlabel("Tamanio de la entrada, n (numero de días)")
    plt.ylabel("Tiempo de ejecucion (s)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/tiempo_vs_n.png")
    plt.close()
    


if __name__ == "__main__":
    TAMANIOS = [10, 50, 100, 500, 1000, 4000, 6000, 8000]
    #Si ejecutamos el subarreglo.py en fuerza bruta cubica y no por Θ(n²), no se ejecutan los arreglos > 1000 valores

    tiempos = []

    inicio_reloj = time.perf_counter()
    tiempos_fb, tiempos_dv = ejecutar_experimento(TAMANIOS)
    fin_reloj = time.perf_counter()
    tiempos.append(fin_reloj - inicio_reloj)
    graficar_tiempo(TAMANIOS, tiempos_fb, tiempos_dv)
    print("\nGrafica guardada en /graficas")
    print(tiempos)
    #print(generar_datos(TAMANIOS[0])) #Para validar los arreglos


