"""Experimentos de la Parte 3: insertion sort sobre los escenarios de Tamiza.

Ejecuta insertion_sort sobre los tres escenarios de entrada para varios
tamanos, registra comparaciones y tiempo, y genera las dos graficas
del laboratorio en la carpeta graficas/.
"""

import time
from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 5
SEMILLA_BASE = 42
CARPETA_GRAFICAS = Path(__file__).resolve().parent / "graficas"

# Cada escenario se envuelve en una funcion con la misma firma
# (n, semilla), porque el escenario C no usa semilla.
ESCENARIOS: dict[str, Callable[[int, int], list[int]]] = {
    "A - Aleatorio": lambda n, semilla: generar_aleatorio(n, semilla),
    "B - Casi ordenado": lambda n, semilla: generar_casi_ordenado(n, semilla),
    "C - Orden inverso": lambda n, semilla: generar_inverso(n),
}

Resultados = dict[str, dict[str, list[float]]]


def esta_en_orden_descendente(lista: list[int]) -> bool:
    """Indica si la lista esta ordenada de mayor a menor.

    Args:
        lista: lista de indices de riesgo.

    Returns:
        True si cada elemento es mayor o igual que el siguiente.
    """
    return all(lista[i] >= lista[i + 1] for i in range(len(lista) - 1))


def verificar_resultado(
    original: list[int], copia_previa: list[int], ordenada: list[int]
) -> None:
    """Comprueba que insertion_sort haya trabajado correctamente.

    Se ejecuta fuera del bloque cronometrado, asi que no afecta el tiempo.

    Args:
        original: lista que se le paso al algoritmo.
        copia_previa: copia de esa lista tomada antes de ordenar.
        ordenada: lista que devolvio el algoritmo.

    Raises:
        ValueError: si el resultado no esta en orden descendente, no
            contiene los mismos elementos o la lista original cambio.
    """
    if original != copia_previa:
        raise ValueError("insertion_sort modifico la lista recibida.")
    if len(ordenada) != len(original) or set(ordenada) != set(original):
        raise ValueError("El resultado no contiene los mismos elementos.")
    if not esta_en_orden_descendente(ordenada):
        raise ValueError("El resultado no esta en orden descendente.")


def medir_escenario(
    generador: Callable[[int, int], list[int]], n: int
) -> tuple[float, float]:
    """Mide insertion_sort sobre un escenario y un tamano dado.

    Repite la medicion con semillas distintas (SEMILLA_BASE + repeticion)
    y promedia. Solo se cronometra la llamada al algoritmo: el lote se
    genera antes y la verificacion se hace despues.

    Args:
        generador: funcion (n, semilla) que produce el lote del escenario.
        n: tamano del lote.

    Returns:
        Tupla (tiempo promedio en segundos, comparaciones promedio).
    """
    tiempos: list[float] = []
    comparaciones: list[int] = []

    for repeticion in range(REPETICIONES):
        lote = generador(n, SEMILLA_BASE + repeticion)
        copia_previa = list(lote)

        inicio = time.perf_counter()
        ordenada, cantidad = insertion_sort(lote)
        fin = time.perf_counter()

        verificar_resultado(lote, copia_previa, ordenada)
        tiempos.append(fin - inicio)
        comparaciones.append(cantidad)

    return sum(tiempos) / REPETICIONES, sum(comparaciones) / REPETICIONES


def ejecutar_experimentos() -> Resultados:
    """Corre insertion_sort en todos los escenarios y tamanos.

    Returns:
        Diccionario {escenario: {"comparaciones": [...], "tiempo": [...]}}
        con un valor por cada tamano de TAMANOS, en el mismo orden.
    """
    resultados: Resultados = {}
    for nombre, generador in ESCENARIOS.items():
        resultados[nombre] = {"comparaciones": [], "tiempo": []}
        for n in TAMANOS:
            tiempo, comparaciones = medir_escenario(generador, n)
            resultados[nombre]["comparaciones"].append(comparaciones)
            resultados[nombre]["tiempo"].append(tiempo)
            print(f"{nombre} | n={n:>5} | "
                  f"comparaciones={comparaciones:>12,.0f} | "
                  f"tiempo={tiempo:.6f} s")
    return resultados


def graficar(
    resultados: Resultados,
    metrica: str,
    etiqueta_y: str,
    titulo: str,
    archivo: str,
    con_teoricas: bool = False,
) -> None:
    """Grafica una metrica contra el tamano de entrada y la guarda.

    Args:
        resultados: salida de ejecutar_experimentos.
        metrica: "comparaciones" o "tiempo".
        etiqueta_y: texto del eje vertical.
        titulo: titulo de la grafica.
        archivo: nombre del archivo de salida dentro de graficas/.
        con_teoricas: si es True, dibuja las curvas n(n-1)/2 y n(n-1)/4.
    """
    figura, eje = plt.subplots(figsize=(8, 5))

    marcadores = ["o", "s", "^"]
    for (nombre, datos), marcador in zip(resultados.items(), marcadores):
        eje.plot(TAMANOS, datos[metrica], marker=marcador, label=nombre)

    if con_teoricas:
        peor = [n * (n - 1) / 2 for n in TAMANOS]
        promedio = [n * (n - 1) / 4 for n in TAMANOS]
        eje.plot(TAMANOS, peor, "--", color="gray", linewidth=1,
                 label="n(n-1)/2 (teórico)")
        eje.plot(TAMANOS, promedio, ":", color="gray", linewidth=1,
                 label="n(n-1)/4 (teórico)")

    eje.set_title(titulo)
    eje.set_xlabel("Tamaño de entrada n (registros)")
    eje.set_ylabel(etiqueta_y)
    eje.grid(True, alpha=0.3)
    eje.legend()
    figura.tight_layout()

    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    figura.savefig(CARPETA_GRAFICAS / archivo, dpi=150)
    plt.close(figura)


def main() -> None:
    """Ejecuta los experimentos de la Parte 3 y genera las graficas."""
    resultados = ejecutar_experimentos()
    graficar(
        resultados, "comparaciones", "Comparaciones entre elementos",
        "Insertion sort: comparaciones vs. tamaño de entrada",
        "parte3_comparaciones.png", con_teoricas=True,
    )
    graficar(
        resultados, "tiempo", "Tiempo de ejecución (s)",
        "Insertion sort: tiempo vs. tamaño de entrada",
        "parte3_tiempo.png",
    )
    print(f"Graficas guardadas en {CARPETA_GRAFICAS}")


if __name__ == "__main__":
    main()