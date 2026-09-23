# Desarrollo del Laboratorio

## <span style="color:red">Parte 1</span>

Inicialmente vemos un **algoritmo correcto** pero que actualmente no está siendo viable debido a que la cantidad de registros `"n"` pasó de **20.000 a 1.200.000** y no se están ordenando todos los datos en el tiempo definido de **4 horas**, es decir, `n` creció **x60**, es necesario buscar la forma de cambiar el algoritmo de **insertion sort** que crece en `n²`.

El tiempo del algoritmo creció **x3.600** y se ejecutó durante **8 años** y actualmente no logra ordenar todos los datos en las **4 horas definidas** debido a la expansión en todos los laboratorios del departamento y por ende, la cantidad de registros aumentó.

Se busca mejorar la ejecución realizando una actualización del algoritmo a **merge sort** que trabaja con `n log n`, el tiempo se multiplicaría solo **x85** `60 × log₂(1.200.000) / log₂(20.000) ≈ 60 × 1,41` y así buscar mejorar el **tiempo de CPU** para que los datos puedan ser ordenados entre las **2:00 a. m. y las 6:00 a. m.**

Duplicar la capacidad del servidor implica tener una **máquina mucho más veloz** para lograr llegar a una solución temporal pero que va a generar **gastos de recursos monetarios frecuentemente** cada vez que `n` crezca y por otro lado, **afectaciones al medio ambiente por el alto consumo energético**.

### Ejemplo

Al consultar los productos en un **ecommerce**, la carga de productos era demasiado lenta y tardaba más de **15 segundos** en mostrar los resultados. En este caso, el algoritmo pudo haber sido correcto; sin embargo, al ser tantos productos a mostrar, siempre tardaba en cargar los resultados.

La tienda tiene aproximadamente más de **1.000 productos** cargados en el sistema, por lo que cada búsqueda tendrá diferentes tiempos según cuántos productos tenga asociados la categoría seleccionada.

### Resultado

Por esta razón, muchos ecommerce pierden clientes; actualmente migraron la tienda a **Shopify** y es mucho más ligero.
