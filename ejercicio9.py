class Vehiculo:
    def _init_(self, marca, velocidad_i=0):
        self.marca = marca
        self.velocidad = velocidad_i
        
    def acelerar(self, v):
        self.velocidad += v
        
    def desacelerar(self, v):
        self.velocidad -= v
        
    def mostrar_velocidad(self):
        print(f"Tu velocidad actual es: {self.velocidad} km/h")

class Coche(Vehiculo):
    def _init_(self, marca, velocidad_i, bocina="¡tuuut!"):
        super()._init_(marca, velocidad_i)
        self.bocina = bocina
        
    def tocar_claxon(self):
        print(self.bocina)

coche_1 = Coche("Peugeot 208", 10.5)

print("La velocidad inicial del coche es:", coche_1.velocidad, "km/h")

coche_1.acelerar(50)
coche_1.desacelerar(15)
coche_1.mostrar_velocidad()
coche_1.tocar_claxon()