# Tema 2: Listas

# Ejercicio 1: 5 ciudades de Colombia, primera y última
ciudades = ['Cali', 'Bogotá', 'Medellín', 'Barranquilla', 'Cartagena'] # list
print ("Primera:", ciudades[0], "- Última:", ciudades[-1])

# Ejercicio 2: agregar dos ciudades, eliminar una
ciudades.append('Pereira')
ciudades.append('Manizales')
ciudades.remove('Bogotá')
print (ciudades)

# Ejercicio 3: ordenar 6 números de mayor a menor
numeros = [15, 3, 42, 8, 27, 1] # list
numeros.sort(reverse=True)
print (numeros)

# Ejercicio 4: suma, mayor y menor
datos = [12, 7, 30, 5, 18] # list
print ("Suma:", sum(datos))
print ("Mayor:", max(datos))
print ("Menor:", min(datos))
