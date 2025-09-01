import math # libreria para funciones matematicas

class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre  # nombre de la figura

    def calcularArea(self):
        raise NotImplementedError("método sobrescrito por la subclase")
        # metodo para calcular el area

class Circulo(FiguraGeometrica): # subclase
    def __init__(self, radio):
        super().__init__("Círculo") # llama al constructor de la super clase
        self.radio = radio 

    def calcularArea(self):
        return math.pi * (self.radio ** 2)

class Rectangulo(FiguraGeometrica): # subclase
    def __init__(self, base, altura):
        super().__init__("Rectángulo")  # llama al constructor de la super clase
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

class Triangulo(FiguraGeometrica): # subclase
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura

    def calcularArea(self): 
        return (self.base * self.altura) / 2
    
# todas las subclases llaman a la clase padre y sobrescriben el metodo calcularArea

# salidas
figuras = [
    Circulo(6),
    Rectangulo(2, 8),
    Triangulo(4, 8)
]

for figura in figuras: # 
    print(f"El área del {figura.nombre} es: {figura.calcularArea():.2f}")
