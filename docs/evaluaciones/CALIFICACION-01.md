# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Mateo Mesa Cardona · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `6b5f3cb`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 13 / 25 |
| Calidad de la explicación teórica | 7 / 25 |
| Corrección de la implementación | 16 / 20 |
| Calidad del análisis de las gráficas | 9 / 20 |
| Documentación y organización del informe | 4 / 10 |
| **Total** | **49 / 100** |
| **Nota (0–5)** | **2.45** |

## 1. Corrección conceptual (13 / 25)
**Lo que hizo bien:**
- Distingue que el algoritmo es correcto pero ya no sirve porque no termina en las 4 horas.
- Explica que duplicar el servidor es una solución temporal y costosa.
- Menciona que el paciente asume el costo cuando la lista queda incompleta.

**Lo que puede mejorar:**
- El segundo ejemplo (la tienda en línea) no dice qué algoritmo falla ni qué límite se incumple; solo cuenta que era lento.
- Las cuentas de la Parte 1 no cuadran: 60 × 1,41 no da 85, y no se explica bien por qué duplicar la velocidad no cambia el crecimiento del tiempo.
- En la Parte 2 falta explicar cuánta energía se acumula al correr el proceso todas las madrugadas durante años.
- Solo aparece un perjuicio concreto; se pedían al menos dos, cada uno con quién asume el costo.
- La tensión de que el orden de la lista decide a quién se llama primero casi no se discute (solo una frase al final de 4.3).

## 2. Calidad de la explicación teórica (7 / 25)
**Lo que hizo bien:**
- Plantea una predicción antes del experimento y justifica por qué el orden descendente cambia los casos.
- La recomendación de usar una sola implementación está bien razonada.

**Lo que puede mejorar:**
- Los tres casos no se definen con claridad: falta decir sobre qué conjunto de entradas se toma el máximo, el mínimo y el promedio. Además, la explicación mezcla "ascendente" y "descendente" y las predicciones por escenario (A, B, C) no coinciden con los escenarios de Tamiza.
- La Parte 4.1 no está en el informe: no hay recurrencia de merge sort, ni su solución paso a paso, ni el cálculo línea a línea de insertion sort, ni la tabla de complejidades. Este es el faltante más importante.

## 3. Corrección de la implementación (16 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor), no cambian la lista recibida y cuentan solo comparaciones entre elementos.
- `merge_sort` tiene su propia mezcla recursiva y no usa `sorted()` ni `sort()`.
- Los tres generadores dan listas del tamaño pedido, sin repetidos, y con semilla.
- Casi todas las funciones tienen type hints y docstrings.

**Lo que puede mejorar:**
- Hay varios problemas de estilo PEP 8 (líneas muy largas, espacios antes de paréntesis).
- Las funciones `main` de `algoritmos.py` y `datos.py` tienen docstrings incompletos, y el docstring del módulo en `datos.py` quedó después de un import.

## 4. Calidad del análisis de las gráficas (9 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes con unidades y leyenda, y se ven en el informe.
- En 3.2 identifica correctamente el peor caso (C), el mejor (B) y el promedio (A), con cifras de n = 6400.
- En 4.3 recomienda merge sort y dice que la extrapolación parte de n = 6.400.

**Lo que puede mejorar:**
- La lectura de la gráfica de 4.2 quedó con marcadores sin llenar ([t(3200)], [R], etc.) y no hay contraste con las complejidades de 4.1.
- En 4.3 la respuesta al servidor del doble de velocidad también tiene marcadores sin llenar ([t_ins], [R], [estimado / 2]); no se dan los tiempos estimados para 1.200.000 registros ni se concluye si caben en 4 horas.
- No se explica por qué merge sort puede no ganar con tamaños muy pequeños.
- Falta anotar que la extrapolación es una estimación (se dice cómo se calculó, pero no los resultados).

## 5. Documentación y organización del informe (4 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en el lugar correcto, con todos los archivos y las gráficas pedidas.
- Hay más de cinco commits con mensajes descriptivos.
- Las gráficas se incrustan con rutas que sí funcionan.

**Lo que puede mejorar:**
- El informe no trae su nombre completo ni las instrucciones para reproducir el experimento.
- Ninguna parte práctica enlaza su código (`algoritmos.py`, `datos.py`, `parte3_casos.py`, `parte4_complejidad.py`).
- Falta la sección de la Parte 4.1 en el orden pedido.

## ¿El código funciona?
Sí. Ambos algoritmos ordenan bien y los dos scripts corren sin errores y generan las gráficas. Las mediciones tienen la forma esperada: insertion sort crece mucho más rápido que merge sort.

## Para el próximo laboratorio
- Revise el informe completo antes de entregar: no deje marcadores sin llenar ni partes sin escribir.
- Escriba la recurrencia de merge sort y resuélvala paso a paso, y calcule insertion sort línea a línea.
- Ponga su nombre, las instrucciones de ejecución y los enlaces a cada archivo de código.
- Responda cada punto que pide el enunciado (dos perjuicios, quién asume el costo, ejemplo propio con datos y restricción).
- Corrija el estilo del código (PEP 8) antes de cada commit.
