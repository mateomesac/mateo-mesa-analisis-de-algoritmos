"""Lista enlazada y tabla hash para consultar guias de envio."""

class Nodo:
    """Nodo de una lista enlazada que guarda una guia y su estado."""

    def __init__(self, guia: int, estado: str) -> None:
        """Crea un nodo sin siguiente.

        Args:
            guia: numero de guia del envio.
            estado: estado actual del envio.
        """
        self.guia = guia
        self.estado = estado
        self.siguiente: Nodo | None = None


class ListaEnlazada:
    """Lista simplemente enlazada de guias, con insercion al inicio."""


    def __init__(self) -> None:
        """Crea una lista vacia."""
        self.cabeza: Nodo | None = None
        self.tamano = 0


    def insertar(self, guia: int, estado: str) -> None:  # Θ(1)
        """Agrega una guia al inicio de la lista.

        Args:
            guia: numero de guia del envio.
            estado: estado actual del envio.
        """
        nuevo_nodo = Nodo(guia, estado)
        # El nuevo nodo apunta a la antigua cabeza
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo    # el nuevo nodo pasa a ser la cabeza
        self.tamano += 1


    def buscar(self, guia: int) -> str | None:  # Θ(n) en el peor caso
        """Busca una guia recorriendo la lista.

        Args:
            guia: numero de guia a buscar.

        Returns:
            El estado del envio, o None si la guia no existe.
        """
        actual = self.cabeza
        while actual is not None:
            if actual.guia == guia:
                return actual.estado
            actual = actual.siguiente
        # A este punto quiere decir que se recorrio toda la lista sin encontrarla
        return None


class TablaHash:
    """Tabla hash con encadenamiento y funcion hash por division."""


    def __init__(self, m: int) -> None:
        """Crea una tabla con m casillas vacias.

        Args:
            m: numero de casillas de la tabla.
        """
        self.m = m
        self.casillas: list[ListaEnlazada] = [
            ListaEnlazada() for _ in range(m)
        ]
        self.tamano = 0


    def hash(self, guia: int) -> int:  # Θ(1)
        """Calcula la casilla de una guia con el metodo de la division.

        Args:
            guia: numero de guia.

        Returns:
            Un indice entre 0 y m - 1.
        """
        return guia % self.m


    def insertar(self, guia: int, estado: str) -> None:  # Θ(1)
        """Inserta una guia en la lista de su casilla.

        Args:
            guia: numero de guia del envio.
            estado: estado actual del envio.
        """
        indice = self.hash(guia)
        # Insercion al inicio de la lista de la casilla: Θ(1)
        self.casillas[indice].insertar(guia, estado)
        self.tamano += 1


    def buscar(self, guia: int) -> str | None:  # Θ(1 + α) esperado
        """Busca una guia recorriendo solo la lista de su casilla.

        Args:
            guia: numero de guia a buscar.

        Returns:
            El estado del envio, o None si la guia no existe.
        """
        indice = self.hash(guia)
        return self.casillas[indice].buscar(guia)


    def factor_carga(self) -> float:  # Θ(1)
        """Calcula el factor de carga de la tabla.

        Returns:
            El cociente entre guias almacenadas y casillas (n / m).
        """
        return self.tamano / self.m


if __name__ == "__main__":
    ejemplo = [
        (1000000010, "en bodega"),
        (1000000024, "en reparto"),
        (1000000017, "en bodega"),
        (1000000005, "entregado"),
    ]
    lista = ListaEnlazada()
    tabla = TablaHash(7)
    for guia, estado in ejemplo:
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    for guia in (1000000017, 9999999999):  # una existente y una inexistente
        en_lista = lista.buscar(guia)
        en_tabla = tabla.buscar(guia)
        print(f"{guia}: lista={en_lista} | tabla={en_tabla}")
    print(f"Factor de carga: {tabla.factor_carga():.2f}")

    # print(tabla.casillas)
    # print(tabla.m)
    # print(tabla.tamano)