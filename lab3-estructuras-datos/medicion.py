"""Experimentos de medicion: lista enlazada frente a tabla hash."""
import gc
import os
import random
import statistics
import time
from collections.abc import Callable

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

ESTADOS = ["en bodega", "en reparto", "entregado"]
SEMILLA_GUIAS = 42        # semilla de las guias almacenadas
BUSQUEDAS = 200           # busquedas inexistentes por medicion
REPETICIONES = 5          # minimo de repeticiones de cada medicion
TIEMPO_MINIMO = 1.0       # segundos de medicion acumulada por punto
MAX_REPETICIONES = 2000   # tope de repeticiones para busquedas muy rapidas
MUESTRA_VERIFICACION = 200
CARPETA_GRAFICAS = "graficas"

# Experimento A: dos n menores de 1.000 y varios de 20.000 o mas
VALORES_N = [100, 500, 1000, 5000, 20000, 50000, 100000]

# Experimento B: n fijo y factores de carga objetivo entre 0,25 y 10
N_FIJO = 20000
ALFAS_OBJETIVO = [0.25, 0.5, 1, 2, 4, 6, 8, 10]


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_guias(n: int, semilla: int = SEMILLA_GUIAS) -> list[int]:
    """Genera n guias distintas de diez digitos, de forma reproducible.

    Args:
        n: cantidad de guias.
        semilla: semilla del generador.

    Returns:
        Una lista de n enteros distintos entre 10**9 y 10**10 - 1.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), n)


def es_primo(numero: int) -> bool:
    """Indica si un numero es primo, probando divisores hasta su raiz.

    Args:
        numero: entero a evaluar.

    Returns:
        True si el numero es primo.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: int) -> int:
    """Busca el primo mas cercano a un valor, probando hacia ambos lados.

    Args:
        objetivo: valor alrededor del cual se busca el primo.

    Returns:
        El primo mas cercano a `objetivo` (el menor si hay empate).
    """
    distancia = 0
    while True:
        if es_primo(objetivo - distancia):
            return objetivo - distancia
        if es_primo(objetivo + distancia):
            return objetivo + distancia
        distancia += 1


def construir_estructuras(
    guias: list[int], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Carga las mismas guias, en el mismo orden, en lista y tabla.

    Args:
        guias: guias a almacenar.
        m: numero de casillas de la tabla.

    Returns:
        La lista enlazada y la tabla hash ya cargadas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for posicion, guia in enumerate(guias):
        estado = ESTADOS[posicion % len(ESTADOS)]
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar_equivalencia(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int],
    inexistentes: list[int],
) -> None:
    """Comprueba que lista y tabla responden lo mismo antes de medir.

    Args:
        lista: lista enlazada cargada.
        tabla: tabla hash cargada con las mismas guias.
        guias: guias existentes de las que se toma una muestra.
        inexistentes: guias que no estan en las estructuras.

    Raises:
        AssertionError: si las dos estructuras difieren en alguna guia.
    """
    azar = random.Random(SEMILLA_GUIAS)
    muestra = azar.sample(guias, min(MUESTRA_VERIFICACION, len(guias)))
    for guia in muestra:
        estado_lista = lista.buscar(guia)
        assert estado_lista is not None, f"la lista no hallo {guia}"
        assert estado_lista == tabla.buscar(guia), f"difieren en {guia}"
    for guia in inexistentes[:MUESTRA_VERIFICACION]:
        assert lista.buscar(guia) is None, f"la lista invento {guia}"
        assert tabla.buscar(guia) is None, f"la tabla invento {guia}"


def medir_busquedas(
    buscar: Callable[[int], str | None],
    guias: list[int],
    repeticiones: int = REPETICIONES,
) -> float:
    """Mide el tiempo medio por busqueda, cronometrando solo las busquedas.

    Cada repeticion cronometra todas las busquedas juntas y divide entre su
    cantidad. Las busquedas rapidas se repiten mas veces, hasta acumular
    `TIEMPO_MINIMO` segundos, para que el ruido del sistema pese poco. Se
    devuelve la mediana de las repeticiones, que es poco sensible a picos.

    Args:
        buscar: metodo de busqueda a medir.
        guias: guias a buscar en cada repeticion.
        repeticiones: minimo de repeticiones de la medicion.

    Returns:
        El tiempo medio por busqueda, en segundos.
    """
    tiempos: list[float] = []
    acumulado = 0.0
    gc.disable()  # evita que el recolector de basura contamine la medicion
    try:
        while len(tiempos) < MAX_REPETICIONES and (
            len(tiempos) < repeticiones or acumulado < TIEMPO_MINIMO
        ):
            inicio = time.perf_counter()
            for guia in guias:
                buscar(guia)
            fin = time.perf_counter()
            acumulado += fin - inicio
            tiempos.append((fin - inicio) / len(guias))
    finally:
        gc.enable()
    return statistics.median(tiempos)


def experimento_a() -> list[dict[str, float]]:
    """Compara lista y tabla variando n, con busquedas de guias inexistentes.

    Returns:
        Una fila por valor de n, con n, m, alfa y los tiempos en segundos.
    """
    resultados: list[dict[str, float]] = []
    print("Experimento A: lista frente a tabla (guias inexistentes)")
    print(f"{'n':>8} {'m':>7} {'alfa':>6} {'lista (µs)':>12} "
          f"{'tabla (µs)':>11} {'lista/tabla':>12}")
    for n in VALORES_N:
        guias = generar_guias(n)
        inexistentes = generar_guias_inexistentes(set(guias), BUSQUEDAS)
        m = primo_cercano(n // 2)
        lista, tabla = construir_estructuras(guias, m)
        verificar_equivalencia(lista, tabla, guias, inexistentes)

        t_lista = medir_busquedas(lista.buscar, inexistentes)
        t_tabla = medir_busquedas(tabla.buscar, inexistentes)
        resultados.append({
            "n": n, "m": m, "alfa": n / m,
            "lista": t_lista, "tabla": t_tabla,
        })
        print(f"{n:>8} {m:>7} {n / m:>6.2f} {t_lista * 1e6:>12.2f} "
              f"{t_tabla * 1e6:>11.3f} {t_lista / t_tabla:>12.0f}")
    return resultados


def experimento_b() -> list[dict[str, float]]:
    """Mide el efecto del factor de carga con n fijo y m variable.

    Returns:
        Una fila por tabla, con m, alfa, cadena mas larga y el tiempo.
    """
    guias = generar_guias(N_FIJO)
    inexistentes = generar_guias_inexistentes(set(guias), BUSQUEDAS)
    resultados: list[dict[str, float]] = []
    print(f"\nExperimento B: efecto del factor de carga (n = {N_FIJO})")
    print(f"{'alfa obj.':>9} {'m':>7} {'alfa':>7} {'cadena max':>11} "
          f"{'tabla (µs)':>11}")
    for alfa_objetivo in ALFAS_OBJETIVO:
        m = primo_cercano(round(N_FIJO / alfa_objetivo))
        lista, tabla = construir_estructuras(guias, m)
        verificar_equivalencia(lista, tabla, guias, inexistentes)

        t_tabla = medir_busquedas(tabla.buscar, inexistentes)
        cadena_max = max(casilla.tamano for casilla in tabla.casillas)
        resultados.append({
            "m": m, "alfa": tabla.factor_carga(),
            "cadena_max": cadena_max, "tabla": t_tabla,
        })
        print(f"{alfa_objetivo:>9} {m:>7} {tabla.factor_carga():>7.2f} "
              f"{cadena_max:>11} {t_tabla * 1e6:>11.3f}")
    return resultados


def graficar_lista_vs_tabla(
    tamanios: list[int],
    tiempos_lista: list[float],
    tiempos_tabla: list[float],
) -> None:
    """
    Grafica tiempo medio por busqueda vs n para lista y tabla hash
    """
    plt.figure()
    plt.plot(tamanios, tiempos_lista, marker="o", label="Lista enlazada")
    plt.plot(tamanios, tiempos_tabla, marker="s",
             label="Tabla hash (alfa aprox. 2)")

    plt.title("Busqueda de guias inexistentes: lista enlazada vs tabla hash")
    plt.xlabel("Numero de guias almacenadas (n)")
    plt.ylabel("Tiempo medio por busqueda (µs)")
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(CARPETA_GRAFICAS, "lista_vs_tabla.png"))
    plt.close()


def graficar_tiempo_vs_alfa(
    alfas: list[float], tiempos_tabla: list[float]
) -> None:
    """
    Grafica tiempo medio por busqueda vs factor de carga en la tabla hash
    """
    plt.figure()
    plt.plot(alfas, tiempos_tabla, marker="o",
             label=f"Tabla hash, guias inexistentes (n = {N_FIJO})")

    plt.title("Tabla hash: tiempo de busqueda vs factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m, guias por casilla)")
    plt.ylabel("Tiempo medio por busqueda (µs)")
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(CARPETA_GRAFICAS, "tiempo_vs_alfa.png"))
    plt.close()


def main() -> None:
    """Ejecuta los dos experimentos y guarda las graficas."""
    os.makedirs(CARPETA_GRAFICAS, exist_ok=True)

    resultados_a = experimento_a()
    graficar_lista_vs_tabla(
        [int(fila["n"]) for fila in resultados_a],
        [fila["lista"] * 1e6 for fila in resultados_a],  # segundos a µs
        [fila["tabla"] * 1e6 for fila in resultados_a],
    )

    resultados_b = experimento_b()
    graficar_tiempo_vs_alfa(
        [fila["alfa"] for fila in resultados_b],
        [fila["tabla"] * 1e6 for fila in resultados_b],
    )

    print("\nGraficas generadas en la carpeta 'graficas/':")
    print("  lista_vs_tabla.png")
    print("  tiempo_vs_alfa.png")


if __name__ == "__main__":
    main()