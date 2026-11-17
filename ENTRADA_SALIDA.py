# Tema 12: Entrada y salida

# Ejercicio 1: operaciones con dos números
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
print ("Suma:", a + b)
print ("Resta:", a - b)
print ("Multiplicación:", a * b)
if b != 0:
    print ("División:", a / b)
else:
    print ("División: no se puede dividir entre cero")

# Ejercicio 2: guardar nombre y ficha en registro.txt
nombre = input("Nombre del aprendiz: ")
ficha = input("Ficha: ")
with open('registro.txt', 'w') as f:
    f.write(nombre + "\n")
    f.write(ficha + "\n")

# Ejercicio 3: leer registro.txt línea por línea
with open('registro.txt', 'r') as f:
    for linea in f:
        print (linea.strip())

# Ejercicio 4: 3 notas, promedio y resultado en un archivo
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
promedio = (n1 + n2 + n3) / 3
mensaje = "Aprobó" if promedio >= 3.0 else "No aprobó"
with open('resultado.txt', 'w') as f:
    f.write(f"Promedio: {promedio:.2f} - {mensaje}\n")
print (f"Promedio: {promedio:.2f} - {mensaje}")
