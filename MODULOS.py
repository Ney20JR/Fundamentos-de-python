# Tema 11: Módulos y paquetes
import math
import random
import datetime
import calculadora

# Ejercicio 1: área de un círculo de radio 5, redondeada
print (round(math.pi * 5 ** 2, 2))

# Ejercicio 2: lanzar un dado 5 veces
for i in range(5):
    print ("Lanzamiento", i + 1, ":", random.randint(1, 6))

# Ejercicio 3: usar el módulo calculadora.py
print (calculadora.sumar(10, 5))
print (calculadora.restar(10, 5))

# Ejercicio 4: fecha de hoy
print (datetime.date.today())
