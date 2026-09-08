def es_primo(numero: int) -> bool:
    """Determina si un numero es primo."""
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
 
 
def main() -> None:
    """Punto de entrada del script."""
    print(es_primo(15))
 
 
if __name__ == "__main__":
    main()