# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Mateo Mesa Cardona · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `67f88ed`

Muy buen trabajo: entregó todo completo y con análisis propio basado en sus mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 21 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **92 / 100** |
| **Nota (0–5)** | **4.60** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identifica el cruce entre n = 10 y n = 50 con sus propios datos y explica por qué ocurre (costo fijo de las llamadas recursivas).
- Compara con el máximo de un arreglo: la recurrencia `T(n) = 2T(n/2) + Θ(1)` da `Θ(n)`, igual que recorrerlo una vez, y concluye bien que dividir no mejora.
- La estimación a 1.000.000 de registros está declarada como estimación, usa un modelo `n²` y `n log n` y explica por qué no usa regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 5, la cuenta de la regla lineal quedó mal escrita (1,325 × 125 es cerca de 166 s, no "1,66"). Revise las cifras antes de entregar.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` explicando de dónde sale cada término.
- Aplica el método maestro (caso 2) verificando que `n^(log₂2) = n` coincide con `f(n)`.
- Justifica el `Θ(n²)` de la fuerza bruta contando los pares (i, j) y la suma acumulada.

**Lo que puede mejorar:**
- Podría explicar un poco más por qué la recurrencia se mantiene igual cuando las mitades no son exactamente iguales.

## 3. Corrección de la implementación (21 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en listas aleatorias; no modifican la lista y `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta.
- `pruebas.py` es completo: cubre más casos de los pedidos (30 listas aleatorias, decimales, empates, extremos).

**Lo que puede mejorar:**
- En los tres archivos faltan las dos líneas en blanco que PEP 8 pide entre funciones.
- En `medicion.py` las funciones llevan docstring, pero el archivo no tiene el de módulo; en `subarreglo.py` hay código de prueba comentado que conviene retirar.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con 8 tamaños. Lo que dice el informe coincide con ella (fuerza bruta cerca de 1,3 s en n = 8000, divide y vencerás pegada al eje).
- Calcula el factor al duplicar de 4000 a 8000 (×5,21 y ×2,12) y lo contrasta con ×4 y ×2,17.
- Incluye una tabla con los valores medidos y repite cada medición 5 veces.

**Lo que puede mejorar:**
- La frase sobre 500 → 1000 quedó incompleta y no se entiende qué concluye; complétela con los factores y su comparación con la teoría.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Siguió la estructura exacta de carpetas y archivos; la gráfica se ve en el README y los enlaces al código funcionan.
- Tiene instrucciones de reproducción y varios commits descriptivos.

**Lo que puede mejorar:**
- En el paso 3 de las instrucciones, el texto entre paréntesis sobre lo que imprimen las pruebas está mal redactado y no coincide con la salida real.

## ¿El código funciona?
Sí. Las pruebas pasan, la medición corre completa en pocos segundos y genera la gráfica. En 500 listas aleatorias los resultados también fueron iguales entre ambos algoritmos.

## Para el próximo laboratorio
- Deje dos líneas en blanco entre todas las funciones.
- Retire el código comentado y agregue docstring a cada módulo.
- Releve el informe terminado para detectar frases incompletas y errores de cuentas.
- Complete siempre las comparaciones numéricas (factor medido vs. teórico) en cada par de tamaños que mencione.
