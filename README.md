# Curso de Analisis de Algoritmos

## Estudiante: Mateo Mesa Cardona

Estudio de la complejidad computacional y las técnicas fundamentales de diseño de algoritmos: recurrencias, dividir y vencer, ordenamiento, estructuras de datos, programación dinámica y algoritmos voraces.

## Temario
1. Fundamentos de control de versiones
2. Sintaxis básica de Python
3. [Buenas prácticas y entornos de trabajo en Python](#buenas-prácticas-entornos-trabajo-Python)

### <div id="buenas-prácticas-entornos-trabajo-Python">3. Buenas prácticas y entornos de trabajo en Python</div>
- En la raiz del repositorio, con el comando ```python -m venv venv``` crear un entorno virtual en caso que no haya sido creado.
- Activar el entorno virtual, en mi caso **(Windows)** ```venv\Scripts\activate``` o para **(Linux/Mac)** ```source venv/bin/activate```, verificar el prefijo **(venv)** en la terminal e instalar las librerias necesarias, luego ejecutar ```pip freeze > requirements.txt``` para registrar lo instalado en el archivo **requirements.txt**.
- Agregar **venv/** en archivo .gitignore para no versionar la carpeta
- Para reproducir el entorno con **requirements.txt**
    - Crear el entorno virtual en la raiz ```python -m venv venv```.
    - Activar el entorno ```venv\Scripts\activate```.
    - Validar prefijo (venv).
    - Ejecutar el comando ```pip install -r requirements.txt``` para reinstalar todas las dependencias.
    - Validar que se hayan cargado todas las librerías con ```pip list```.

```Python
print("¡Hola, mundo!")
```