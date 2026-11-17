# Tema 9: Clases y objetos

# Ejercicio 1: clase Aprendiz
class Aprendiz:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def mostrar(self):
        print (f"Aprendiz: {self.nombre} - Ficha: {self.ficha}")

Aprendiz("Ana", "2900001").mostrar()

# Ejercicio 2: clase Rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

r = Rectangulo(8, 5)
print ("Área:", r.area(), "- Perímetro:", r.perimetro())

# Ejercicio 3: Cuenta con retirar (sin saldo negativo)
class Cuenta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def retirar(self, valor):
        if valor > self.saldo:
            print ("Fondos insuficientes")
        else:
            self.saldo -= valor

c = Cuenta(1000)
c.retirar(300)
print (c.saldo)
c.retirar(5000)
print (c.saldo)

# Ejercicio 4: Vehiculo y subclase Moto
class Vehiculo:
    def describir(self):
        print ("Soy un vehículo")

class Moto(Vehiculo):
    def describir(self):
        print ("Soy una moto de dos ruedas")

Vehiculo().describir()
Moto().describir()
