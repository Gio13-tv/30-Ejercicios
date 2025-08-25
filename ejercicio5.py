from math import *

class Operacion:
    def _init_(self, x,y):
        self.x=x
        self.y=y
        
    def suma(self):
        return self.x +self.y
    
    def multiplicacion(self):
        return self.x*self.y
    
    def division(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return "¡División de x por y es imposible!"

operation1 = Operacion(3, 2)

print("La suma es:", operation1.suma())
print("La multiplicación es:", operation1.multiplicacion())
print("La división es:", operation1.division())

operation1.y = 0

print("La división con y = 0 es:", operation1.division())