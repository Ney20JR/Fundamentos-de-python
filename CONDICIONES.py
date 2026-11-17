# Tema 6: Condiciones

# Ejercicio 1: positivo, negativo o cero
numero = int(input("Escribe un número: "))
if numero > 0:
    print ("Positivo")
elif numero < 0:
    print ("Negativo")
else:
    print ("Cero")

# Ejercicio 2: año bisiesto
anio = int(input("Escribe un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print (anio, "es bisiesto")
else:
    print (anio, "no es bisiesto")

# Ejercicio 3: saludo según la hora (0 a 23)
hora = int(input("Escribe la hora (0 a 23): "))
if hora < 12:
    print ("Buenos días")
elif hora < 18:
    print ("Buenas tardes")
else:
    print ("Buenas noches")

# Ejercicio 4: promedio de tres notas
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
promedio = (n1 + n2 + n3) / 3 # float
print (f"Promedio: {promedio:.2f}")
if promedio >= 3.0:
    print ("Aprueba")
else:
    print ("No aprueba")
