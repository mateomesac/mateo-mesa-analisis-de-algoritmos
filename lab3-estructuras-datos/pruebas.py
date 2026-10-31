"""Pruebas con assert para ListaEnlazada y TablaHash."""
import random

from estructuras import ListaEnlazada, TablaHash


# 1. Busqueda exitosa e infructuosa en la lista
lista = ListaEnlazada()
for guia, estado in ((10, "en bodega"), (24, "en reparto"), (17, "entregado")):
    lista.insertar(guia, estado)

assert lista.buscar(24) == "en reparto"
assert lista.buscar(10) == "en bodega"
assert lista.buscar(99) is None         # busqueda infructuosa de la lista
assert lista.tamano == 3
assert lista.cabeza is not None
assert lista.cabeza.guia == 17          # inserta al inicio


# 2. Busqueda exitosa e infructuosa en la tabla
tabla = TablaHash(7)
for guia, estado in ((10, "en bodega"), (24, "en reparto"), (17, "entregado")):
    tabla.insertar(guia, estado)

assert tabla.buscar(24) == "en reparto"
assert tabla.buscar(10) == "en bodega"
assert tabla.buscar(99) is None         # busqueda infructuosa de la tabla


# 3. Colision forzada: m = 7 - las guias 10, 24 y 17 ingresan a la casilla 3 - 10%7 - 24%7 - 17%7
assert tabla.hash(10) == 3  
assert tabla.hash(24) == 3
assert tabla.hash(17) == 3
assert tabla.buscar(17) == "entregado"  # las tres se recuperan despues de insertar
assert tabla.casillas[3].tamano == 3    # longitud de la casilla 3 

longitud = 0                            # longitud contando los nodos
nodo = tabla.casillas[3].cabeza
while nodo is not None:
    longitud += 1
    nodo = nodo.siguiente
assert longitud == 3

# Las demas casillas siguen vacias
for i, casilla in enumerate(tabla.casillas):
    if i != 3:
        assert casilla.cabeza is None


# 4. Factor de carga tras las tres inserciones
assert tabla.factor_carga() == 3 / 7
assert TablaHash(7).factor_carga() == 0


# 5. Veinte o mas colecciones aleatorias: lista y tabla responden lo mismo
estados = ["en bodega", "en reparto", "entregado"]
rng = random.Random(2024)
colecciones = 30

for _ in range(colecciones):
    n = rng.randint(1, 300)
    m = rng.choice([7, 11, 101, 997])
    guias = rng.sample(range(10**9, 10**10), n)  # unicas, de diez digitos

    lista = ListaEnlazada()
    tabla = TablaHash(m)
    esperado: dict[int, str] = {}  # solo en la prueba, como referencia
    for guia in guias:
        estado = rng.choice(estados)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
        esperado[guia] = estado

    assert lista.tamano == tabla.tamano == n
    assert tabla.factor_carga() == n / m

    # Guias existentes
    for guia in guias:
        assert lista.buscar(guia) == tabla.buscar(guia) == esperado[guia]

    # Guias inexistentes
    inexistentes = 0
    while inexistentes < 50:
        candidata = rng.randrange(10**9, 10**10)
        if candidata in esperado:
            continue
        assert lista.buscar(candidata) is None
        assert tabla.buscar(candidata) is None
        inexistentes += 1


print("Todas las pruebas pasaron.")