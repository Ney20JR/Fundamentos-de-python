# Tema 5: Operaciones básicas con cadenas

# Ejercicio 1: cantidad de caracteres de una palabra
palabra = input("Escribe una palabra: ")
print ("Tiene", len(palabra), "caracteres")

# Ejercicio 2: quitar espacios y pasar a mayúsculas
frase = '  hola mundo  ' # str
print (frase.strip().upper())

# Ejercicio 3: contar la letra 'a'
texto = "La casa de Ana es amarilla" # str
print ("La letra a aparece", texto.lower().count('a'), "veces")

# Ejercicio 4: invertir y verificar palíndromo
cadena = "reconocer" # str
invertida = cadena[::-1]
print (invertida)
if cadena == invertida:
    print (cadena, "es un palíndromo")
else:
    print (cadena, "no es un palíndromo")
