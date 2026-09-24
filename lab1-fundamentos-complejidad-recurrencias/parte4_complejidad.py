"""Parte 4: comparacion experimental de insertion sort y merge sort.

Mide el tiempo de ambos algoritmos sobre el escenario A con los tamanos
de la Parte 3, genera la grafica parte4_tiempo.png y estima, por
extrapolacion, el tiempo con 1.200.000 registros para el concepto
tecnico de la seccion 4.3.
"""

import math
import time
from typing import Callable

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from parte3_casos import (
    CARPETA_GRAFICAS,
    ESCENARIOS,
    REPETICIONES,
    SEMILLA_BASE,
    TAMANOS,
    verificar_resultado,
)

N_TAMIZA = 1_200_000
VENTANA_SEGUNDOS = 4 * 60 * 60
FACTOR_SERVIDOR = 2
# Medicion adicional de merge sort con n = 1.200.000, para comparar con
# la extrapolacion. Tarda unos segundos; ponga False para omitirla.
VALIDAR_MERGE_EN_N_TAMIZA = True

Algoritmo = Callable[[list[int]], tuple[list[int], int]]
Generador = Callable[[int, int], list[int]]


def medir_tiempo(algoritmo: Algoritmo, generador: Generador, n: int) -> float:
    """Mide el tiempo promedio de un algoritmo sobre un escenario.

    Usa las mismas semillas para todos los algoritmos, asi que ambos
    ordenan exactamente los mismos lotes. Solo se cronometra la llamada
    al algoritmo.

    Args:
        algoritmo: funcion que ordena y devuelve (lista, comparaciones).
        generador: funcion (n, semilla) que produce el lote.
        n: tamano del lote.

    Returns:
        Tiempo promedio de ejecucion, en segundos.
    """
    tiempos: list[float] = []
    for repeticion in range(REPETICIONES):
        lote = generador(n, SEMILLA_BASE + repeticion)
        copia_previa = list(lote)

        inicio = time.perf_counter()
        ordenada, _ = algoritmo(lote)
        fin = time.perf_counter()

        verificar_resultado(lote, copia_previa, ordenada)
        tiempos.append(fin - inicio)
    return sum(tiempos) / REPETICIONES


def extrapolar_cuadratico(
    tiempo: float, n_medido: int, n_objetivo: int
) -> float:
    """Estima el tiempo de un algoritmo de orden n^2 en otro tamano.

    Supone T(n) = c * n^2, asi que T(N) = T(n) * (N / n)^2.

    Args:
        tiempo: tiempo medido con n_medido registros, en segundos.
        n_medido: tamano con el que se midio.
        n_objetivo: tamano para el que se estima.

    Returns:
        Tiempo estimado con n_objetivo registros, en segundos.
    """
    return tiempo * (n_objetivo / n_medido) ** 2


def extrapolar_n_log_n(
    tiempo: float, n_medido: int, n_objetivo: int
) -> float:
    """Estima el tiempo de un algoritmo de orden n log n en otro tamano.

    Supone T(n) = c * n * log2(n), asi que
    T(N) = T(n) * (N * log2 N) / (n * log2 n).

    Args:
        tiempo: tiempo medido con n_medido registros, en segundos.
        n_medido: tamano con el que se midio.
        n_objetivo: tamano para el que se estima.

    Returns:
        Tiempo estimado con n_objetivo registros, en segundos.
    """
    factor = (n_objetivo * math.log2(n_objetivo)) / (
        n_medido * math.log2(n_medido)
    )
    return tiempo * factor


def formatear_duracion(segundos: float) -> str:
    """Convierte segundos a un texto legible (s, min o h).

    Args:
        segundos: duracion en segundos.

    Returns:
        Texto como "12.3 s", "4.5 min" o "6.4 h".
    """
    if segundos < 60:
        return f"{segundos:.2f} s"
    if segundos < 3600:
        return f"{segundos / 60:.1f} min"
    return f"{segundos / 3600:.1f} h"


def graficar_tiempos(
    tiempos_insertion: list[float],
    tiempos_merge: list[float],
    archivo: str,
    escala_log: bool = False,
) -> None:
    """Grafica el tiempo de ambos algoritmos contra el tamano de entrada.

    Args:
        tiempos_insertion: tiempos de insertion sort, uno por tamano.
        tiempos_merge: tiempos de merge sort, uno por tamano.
        archivo: nombre del archivo de salida dentro de graficas/.
        escala_log: si es True, usa escala logaritmica en ambos ejes.
    """
    figura, eje = plt.subplots(figsize=(8, 5))
    eje.plot(TAMANOS, tiempos_insertion, marker="o",
             label="Insertion sort")
    eje.plot(TAMANOS, tiempos_merge, marker="s", label="Merge sort")

    titulo = "Tiempo de ordenamiento en el escenario A"
    if escala_log:
        eje.set_xscale("log")
        eje.set_yscale("log")
        titulo += " (escala logarítmica)"
    eje.set_title(titulo)
    eje.set_xlabel("Tamaño de entrada n (registros)")
    eje.set_ylabel("Tiempo de ejecución (s)")
    eje.grid(True, alpha=0.3)
    eje.legend()
    figura.tight_layout()

    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    figura.savefig(CARPETA_GRAFICAS / archivo, dpi=150)
    plt.close(figura)


def imprimir_tabla_a(
    tiempos_insertion: list[float], tiempos_merge: list[float]
) -> None:
    """Imprime tiempos, razon entre algoritmos y constantes por tamano.

    Las constantes T/n^2 (insertion) y T/(n log2 n) (merge) sirven para
    justificar la extrapolacion: si se estabilizan al crecer n, el
    modelo teorico describe bien la medicion.

    Args:
        tiempos_insertion: tiempos de insertion sort, uno por tamano.
        tiempos_merge: tiempos de merge sort, uno por tamano.
    """
    print("\nEscenario A: insertion sort vs. merge sort")
    print(f"{'n':>6} | {'insertion (s)':>13} | {'merge (s)':>10} | "
          f"{'ins/merge':>9} | {'T/n^2 (ns)':>10} | {'T/nlog2n (ns)':>13}")
    for n, t_ins, t_mer in zip(TAMANOS, tiempos_insertion, tiempos_merge):
        print(f"{n:>6} | {t_ins:>13.6f} | {t_mer:>10.6f} | "
              f"{t_ins / t_mer:>9.1f} | {t_ins / n ** 2 * 1e9:>10.1f} | "
              f"{t_mer / (n * math.log2(n)) * 1e9:>13.1f}")


def estimar_ventana() -> None:
    """Estima, para cada escenario, si 1.200.000 registros caben en 4 h.

    Mide ambos algoritmos con el tamano mas grande de TAMANOS y
    extrapola: modelo n^2 para insertion sort y n log n para merge sort.
    Los resultados son estimaciones, no mediciones.
    """
    n_base = TAMANOS[-1]
    print(f"\nEstimacion para n = {N_TAMIZA:,} (base: n = {n_base}).")
    print("Son ESTIMACIONES por extrapolacion, no mediciones.")
    print(f"{'escenario':<20} | {'algoritmo':<14} | {'medido':>9} | "
          f"{'estimado 1,2 M':>14} | {'cabe x1':>7} | {'cabe x2':>7}")

    for nombre, generador in ESCENARIOS.items():
        for etiqueta, algoritmo, extrapolar in (
            ("insertion sort", insertion_sort, extrapolar_cuadratico),
            ("merge sort", merge_sort, extrapolar_n_log_n),
        ):
            medido = medir_tiempo(algoritmo, generador, n_base)
            estimado = extrapolar(medido, n_base, N_TAMIZA)
            cabe = "si" if estimado <= VENTANA_SEGUNDOS else "no"
            cabe_doble = (
                "si"
                if estimado / FACTOR_SERVIDOR <= VENTANA_SEGUNDOS
                else "no"
            )
            print(f"{nombre:<20} | {etiqueta:<14} | "
                  f"{formatear_duracion(medido):>9} | "
                  f"{formatear_duracion(estimado):>14} | "
                  f"{cabe:>7} | {cabe_doble:>7}")


def validar_merge_en_n_tamiza() -> None:
    """Mide merge sort con n = 1.200.000 y lo compara con la estimacion."""
    generador = ESCENARIOS["A - Aleatorio"]
    lote = generador(N_TAMIZA, SEMILLA_BASE)
    copia_previa = list(lote)

    inicio = time.perf_counter()
    ordenada, comparaciones = merge_sort(lote)
    fin = time.perf_counter()
    verificar_resultado(lote, copia_previa, ordenada)

    n_base = TAMANOS[-1]
    base = medir_tiempo(merge_sort, generador, n_base)
    estimado = extrapolar_n_log_n(base, n_base, N_TAMIZA)
    print(f"\nMerge sort con n = {N_TAMIZA:,} (escenario A):")
    print(f"  medido:   {formatear_duracion(fin - inicio)} "
          f"({comparaciones:,} comparaciones)")
    print(f"  estimado: {formatear_duracion(estimado)} "
          f"(extrapolado desde n = {n_base})")


def main() -> None:
    """Ejecuta la comparacion de la Parte 4 y genera las graficas."""
    generador_a = ESCENARIOS["A - Aleatorio"]
    tiempos_insertion = [
        medir_tiempo(insertion_sort, generador_a, n) for n in TAMANOS
    ]
    tiempos_merge = [
        medir_tiempo(merge_sort, generador_a, n) for n in TAMANOS
    ]

    imprimir_tabla_a(tiempos_insertion, tiempos_merge)
    graficar_tiempos(tiempos_insertion, tiempos_merge, "parte4_tiempo.png")
    graficar_tiempos(tiempos_insertion, tiempos_merge,
                     "parte4_tiempo_log.png", escala_log=True)
    print(f"\nGraficas guardadas en {CARPETA_GRAFICAS}")

    estimar_ventana()
    if VALIDAR_MERGE_EN_N_TAMIZA:
        validar_merge_en_n_tamiza()


if __name__ == "__main__":
    main()