# Tema 4: Formato de cadenas

# Ejercicio 1: presentación con f-strings
nombre = "Ana" # str
edad = 21 # int
ciudad = "Cali" # str
print (f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}")

# Ejercicio 2: precio con dos decimales
precio = 1999.5 # float
print (f"Precio: {precio:.2f}")

# Ejercicio 3: tabla del 7 hasta el 3 con .format()
for i in range(1, 4):
    print ("7 x {} = {}".format(i, 7 * i))

# Ejercicio 4: ceros a la izquierda
n = 7 # int
print (f"{n:03d}")
