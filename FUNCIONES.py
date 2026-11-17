# Tema 8: Funciones

# Ejercicio 1: es_par
def es_par(n):
    return n % 2 == 0

print (es_par(4), es_par(7))

# Ejercicio 2: área del círculo con pi = 3.1416
def area_circulo(radio):
    return 3.1416 * radio ** 2

print (round(area_circulo(5), 2))

# Ejercicio 3: mayor de una lista sin usar max
def mayor(lista):
    m = lista[0]
    for x in lista:
        if x > m:
            m = x
    return m

print (mayor([4, 19, 7, 33, 2]))

# Ejercicio 4: factorial con un ciclo
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print (factorial(5))
