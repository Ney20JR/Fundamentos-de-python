# Tema 10: Diccionarios

# Ejercicio 1: datos de un libro
libro = {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'anio': 1967} # dict
for clave, valor in libro.items():
    print (clave, ":", valor)

# Ejercicio 2: 4 productos y total
productos = {'arroz': 4500, 'leche': 3800, 'huevos': 12000, 'pan': 5000} # dict
print ("Total:", sum(productos.values()))

# Ejercicio 3: traductor español-inglés
traducciones = {'casa': 'house', 'perro': 'dog', 'gato': 'cat', 'libro': 'book'} # dict
palabra = input("Palabra en español: ").lower()
if palabra in traducciones:
    print (palabra, "=", traducciones[palabra])
else:
    print ("La palabra no está en el diccionario")

# Ejercicio 4: contar palabras de una frase
frase = "el sol sale el lunes y el sol se oculta" # str
conteo = {}
for p in frase.split():
    conteo[p] = conteo.get(p, 0) + 1
print (conteo)
