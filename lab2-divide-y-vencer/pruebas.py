"""Pruebas con assert para el subarreglo maximo.

Ejecutar con: python pruebas.py
Cada llamada a verificar imprime una linea [OK] si el caso pasa.
"""

import math
import random

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
    suma_cruzada,
)

LIMITE_IMPRESION = 12


def suma_del_tramo(valores: list[float], inicio: int, fin: int) -> float:
    """
    Suma valores[inicio..fin] para validar los indices devueltos.

    Args:
        valores: lista de variaciones diarias de caja.
        inicio: indice inicial del tramo (inclusive).
        fin: indice final del tramo (inclusive).

    Returns:
        La suma de los elementos de valores[inicio..fin], con ambos
        extremos incluidos.
    """
    total: float = 0
    for k in range(inicio, fin + 1):
        total += valores[k]
    return total #suma total de todos los valores de valores = 10


def verificar(valores: list[float], esperada: float | None = None, mostrar: bool = True,) -> None:
    """
    Ejecuta ambos algoritmos y comprueba que sean coherentes.

    Args:
        valores: lista de variaciones diarias, con al menos un
            elemento. La funcion no la modifica.
        esperada: suma maxima conocida de antemano. Si es None, solo
            se verifica la coherencia entre los dos algoritmos.
            Por defecto, None.
        mostrar: si es True, imprime el resultado del caso cuando
            pasa; las listas de mas de LIMITE_IMPRESION elementos se
            resumen. Por defecto, True.

    Returns:
        None. Si todas las comprobaciones pasan, imprime el caso (con
        mostrar=True); si alguna falla, lanza AssertionError.

    Raises:
        AssertionError: si alguna de las comprobaciones falla.
    """
    copia = list(valores)
    subarreglo_fb = subarreglo_fuerza_bruta(valores)
    subarreglo_dv = subarreglo_maximo(valores, 0, len(valores) - 1)

    # Las sumas deben coincidir (los indices pueden diferir en empates).
    assert math.isclose(subarreglo_fb[2], subarreglo_dv[2]), (
        valores, subarreglo_fb, subarreglo_dv
    )
    # Los indices devueltos deben reproducir la suma reportada.
    for inicio, fin, suma in (subarreglo_fb, subarreglo_dv):
        assert 0 <= inicio <= fin < len(valores)
        assert math.isclose(suma_del_tramo(valores, inicio, fin), suma)
    # Ninguna funcion modifica la lista recibida.
    assert valores == copia
    if esperada is not None:
        assert math.isclose(subarreglo_fb[2], esperada)
        assert math.isclose(subarreglo_dv[2], esperada)

    if mostrar:
        entrada: object = valores
        if len(valores) > LIMITE_IMPRESION:
            entrada = f"lista de {len(valores)} elementos"
        print(f"[OK] verificar({entrada}, {esperada})")
        print(f"     Fuerza bruta       :   {subarreglo_fb}")
        print(f"     Dividr y vencer    :   {subarreglo_dv}")


# Serie de ocho dias de la situacion problema (suma 17): dias del 2 al 7
serie: list[float] = [-3, 5, -2, 8, -6, 3, 9, -4]
verificar(serie, 17)
assert subarreglo_fuerza_bruta(serie) == (1, 6, 17)
assert subarreglo_maximo(serie, 0, len(serie) - 1) == (1, 6, 17)

# Solo un elemento (positivo, negativo y cero).
verificar([7], 7)
verificar([-4], -4)
verificar([0], 0)

# Todos los elementos negativos.
verificar([-8, -3, -6, -2, -5], -2)

# Todos los elementos positivos.
verificar([4, 1, 3, 2, 5], 15)

# El mejor tramo cruza el punto medio (medio = 4, tramo 3..6, suma 6).
serie_cruzado = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
verificar(serie_cruzado, 6)
assert subarreglo_maximo(serie_cruzado, 0, len(serie_cruzado) - 1) == (3, 6, 6)
assert suma_cruzada(serie_cruzado, 0, 4, 8) == (3, 6, 6)

# Casos borde adicionales.
verificar([5, -10, 1], 5)  # maximo en el extremo izquierdo
verificar([1, -10, 5], 5)  # maximo en el extremo derecho
verificar([0, 0, 0, 0], 0)  # empates: cualquier tramo vale
verificar([2, 3])  # n = 2
verificar([-1, -1, -1, -1])  # empates con negativos
verificar([1.5, -0.5, 2.25, -4.0, 1.0], 3.25)  # valores flotantes

# Pruebas aleatorias: 30 listas, longitudes de 1 a 60.
random.seed(42)
for _ in range(30):
    n = random.randint(1, 60)
    verificar([random.randint(-100, 100) for _ in range(n)], mostrar = False)
print("[OK] 30 listas aleatorias: ambos algoritmos coinciden en suma")

# Casos aleatorios con valores negativos y uno de los dos con flotantes.
verificar([random.randint(-100, 20) for _ in range(50)])
verificar([random.uniform(-10, 10) for _ in range(50)])

print("\nTodas las pruebas pasaron.")