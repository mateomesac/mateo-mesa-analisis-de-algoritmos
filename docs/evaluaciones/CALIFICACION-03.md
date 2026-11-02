# Retroalimentación — Laboratorio 03: Estructuras de datos

**Estudiante:** Mateo Mesa Cardona · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `3119700`

Muy buen trabajo: su laboratorio está completo, ordenado y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **98 / 100** |
| **Nota (0–5)** | **4.90** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y usa el ejemplo de las guías 10, 24 y 17 con `m = 7`.
- Compara encadenamiento y direccionamiento abierto con ventajas y costos de cada uno.
- Justifica por qué la tabla no sirve para rangos y muestra lo que ofrece el árbol de búsqueda.
- Estima la altura del árbol degenerado (≈ 400.000) y la del equilibrado (≈ 19), y recomienda una combinación de estructuras.
- La estimación para 5.000.000 de envíos está declarada como estimación y se apoya en sus mediciones.

**Lo que puede mejorar (y cómo corregirlo):**
- En la estimación de la tabla con 5.000.000 de envíos, el rango final (0,13 a 0,6 µs) se justifica de forma muy breve.
  → *Cómo corregirlo:* explique en una frase qué efecto concreto hace subir el tiempo por cada búsqueda cuando hay muchas más casillas, y cómo eso le dio el límite superior del rango.
- Al hablar del árbol equilibrado dice "unas 19 comparaciones", pero no cuenta cuántas comparaciones costaría insertar las 400.000 guías en ese caso, para contrastarlo con las ≈ n²/2 del árbol degenerado.
  → *Cómo corregirlo:* calcule cuántas comparaciones cuesta insertar cada guía en el árbol equilibrado y multiplique por el número de guías.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista por tener que revisar todos los nodos cuando la guía no existe.
- Explica el `Θ(1 + α)` de la tabla: calcular la casilla cuesta `Θ(1)` y recorrer su lista cuesta en promedio `α`.
- Nombra el supuesto de hash uniforme simple y explica que, si todo cae en una casilla, la tabla pasa a costar `Θ(n)`.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Ambas estructuras devuelven el estado correcto en búsquedas exitosas e infructuosas.
- La colisión forzada con `m = 7` funciona y la casilla 3 queda con tres guías.
- `factor_carga` da `3 / 7`, y la lista y la tabla coinciden en 30 colecciones aleatorias.
- La tabla reutiliza `ListaEnlazada` y no usa `dict`, `set` ni `hash()` en `estructuras.py`; la búsqueda es con ciclo `while`.

**Lo que puede mejorar (y cómo corregirlo):**
- Las funciones `graficar_lista_vs_tabla` y `graficar_tiempo_vs_alfa` de `medicion.py` tienen docstring de una sola línea, sin las secciones `Args` y `Returns`.
  → *Cómo corregirlo:* agregue a cada una las secciones `Args:` (con cada parámetro) y `Returns:` (aunque devuelva `None`), con el mismo formato del resto de sus funciones.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera tiene siete valores de `n` con las dos curvas en los mismos ejes y la segunda ocho valores de `α`.
- En la pregunta 2 calcula el factor de crecimiento entre `n = 50.000` y `n = 100.000` (lista ×2,65, tabla ×1,02) y lo contrasta con `Θ(n)` y `Θ(1)`.
- Describe la relación casi lineal entre el tiempo y `α` y la compara con `Θ(1 + α)`.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `lab3-estructuras-datos/` está en la raíz del repositorio con todos los archivos y las dos gráficas del entregable.
- El informe sigue el orden pedido, trae su nombre e instrucciones para reproducir, enlaza el código en cada parte y las imágenes se ven con ruta relativa.
- Hay cinco commits con mensajes descriptivos.

## ¿El código funciona?
Sí. `pruebas.py` termina con el mensaje de que todas las pruebas pasaron, y `medicion.py` corre completo y genera las dos gráficas.
