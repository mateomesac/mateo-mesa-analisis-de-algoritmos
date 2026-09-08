# print("Hola, mundo")

# n = 10000
# print(type(n))
tiempo = 0.0034
# print(type(tiempo))
# algoritmo = "algoritmo de ordenamiento"
# print(type(algoritmo))
# ordenado = True
# print(type(ordenado))
# resultado = None
# print(type(resultado))


##CONDICIONALES
## if
# if tiempo < 0.001:
#     categoria = "rapido"
# elif tiempo < 0.01:
#     categoria = "moderado"
# else:
#     categoria = "lento"

# print(categoria)

#for
# for tamano in [100, 1000, 10000]:
#     print(f"Probando con n = {tamano}")
 
# for i in range(2, 15, 3): #Incremento, Tope, Salto
#     print(i)

#while
# intentos = 0
# while intentos <3:
#     intentos = intentos + 1
#     print(intentos)

##FUNCIONES
# def contar_comparaciones(lista: list) -> int:
#     """Cuenta cuantas comparaciones hace insertion sort sobre 'lista'.
 
#     Args:
#         lista: lista de numeros a ordenar.
 
#     Returns:
#         El numero total de comparaciones realizadas.
#     """
#     comparaciones = 0
#     for i in range(1, len(lista)):
#         j = i
#         while j > 0 and lista[j - 1] > lista[j]:
#             comparaciones = comparaciones + 1
#             lista[j - 1], lista[j] = lista[j], lista[j - 1]
#             j = j - 1
#     return comparaciones
 
# total = contar_comparaciones([5, 2, 9, 1])

# print(total)

##ESTRUCTURAS DE DATOS EN PYTHON
##Listas
# numeros = [5,2,9,1]
# print(numeros[2])
# for numero in numeros:
#     print(numero)

##Tuplas
# puntos = (1000, 0.34, True)
# print(puntos[-1])
# for punto in puntos:
#     print(punto)

##Diccionario
# tiempo = {
#     1000: 0.0002,
#     10000: 0.0034,
#     100000: 0.1,
#     "Llave1": 100
# }
# print(tiempo.get("Llave1"))
# print(tiempo.get(10000))

##Conjuntos (No admite valores repetidos)
# tamanios = {100,1000,10000,20000}
# print(tamanios)


## Quieres contruir la lista de los cuadros de los tamaños
## de entrada que vas a probar: [100,1000,10000]->[10000, 1000000, 100000000]
#for clasico
# tamanios = [100,1000,10000]
# cuadrados = [] #Lista vacia
# for i in tamanios:
#     cuadrados.append(i**2)

##compresion de listas - Aplica cuando es una sola operación
# tamanios = [100,1000,10000]
# cuadrados = [i**2 for i in tamanios]
# cuadrados2 = [i**2 for i in tamanios if i > 1000] #Con condicion/filtro

# print(cuadrados)
# print(cuadrados2)

##Excepciones
# try:
#     print(1000/1)
#     a = 2
#     a.shor() #AttributeError
# except ZeroDivisionError:
#     print("No se puede dividir por cero")
# except:
#     print("Ocurrio un error al ejecutar el programa")
# print("El programa se sigue ejecutando")

