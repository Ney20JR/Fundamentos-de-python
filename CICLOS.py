# Tema 7: Ciclos

# Ejercicio 1: pares del 1 al 50
for i in range(2, 51, 2):
    print (i)

# Ejercicio 2: suma de 1 a 100
suma = 0 # int
for i in range(1, 101):
    suma += i
print ("Suma del 1 al 100:", suma)

# Ejercicio 3: tabla de multiplicar de un número ingresado
n = int(input("¿Qué tabla quieres ver? "))
for i in range(1, 11):
    print (f"{n} x {i} = {n * i}")

# Ejercicio 4: pedir la clave hasta que sea correcta
clave_correcta = "sena2026" # str
clave = input("Clave: ")
while clave != clave_correcta:
    print ("Clave incorrecta, intenta de nuevo")
    clave = input("Clave: ")
print ("Acceso concedido")
