from math import *

class Circulo:
    def __init__(self, x, y, R):
        self.x = x
        self.y = y
        self.R = R
    
    def area(self):
        return pi * self.R ** 2
    
    def perimetro(self):
        return 2 * pi * self.R
    
    def mostrar_propiedades(self):
        return ("El circulo tiene un radio de " + str(self.R) + "cm, y su centro es O(" +
                str(self.x) + "," + str(self.y) + ")")
    
circulo_1 = Circulo(3, 4, 5)

print(circulo_1.mostrar_propiedades())
print("El perímetro del circulo_1 es:", round(circulo_1.perimetro(), 2))
print("El área del circulo_1 es:", round(circulo_1.area(), 2))