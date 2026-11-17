# Tema 1: Variables y Tipos de Datos
edad = 21 # int
promedio = 4.5 # float
nombre = "Ana" # str
activo = True # bool
print ("Hola, mi nombre es", nombre)

# Ejercicio 1: variables con nombre, edad, estatura y si es aprendiz (bool)
nombre = "Christian" # str
edad = 21 # int
estatura = 1.71 # float (en metros)
es_aprendiz = True # bool
ciudad = "Cali" # str
cargo = "Analista de aplicativos" # str
ficha = "ADSO36" # str
deporte = "fútbol" # str
equipo = "Manchester City" # str
print ("Nombre:", nombre)
print ("Edad:", edad)
print ("Estatura:", estatura, "m")
print ("Es aprendiz:", es_aprendiz)
print ("Vivo en:", ciudad)
print ("Soy:", cargo)
print ("Ficha:", ficha)
print ("Me encanta el", deporte, "y ¡viva el", equipo + "!")

# Ejercicio 2: tipo de cada variable
print (type(nombre), type(edad), type(estatura), type(es_aprendiz))
print (type(ciudad), type(cargo), type(ficha), type(deporte), type(equipo))

# Ejercicio 3: convertir '3.75' a decimal y sumarle 1
texto = '3.75' # str
numero = float(texto) # float
print (numero + 1)

# Ejercicio 4: intercambiar x e y sin usar una tercera variable
x, y = 10, 20
print ("Antes:", x, y)
x, y = y, x
print ("Después:", x, y)
