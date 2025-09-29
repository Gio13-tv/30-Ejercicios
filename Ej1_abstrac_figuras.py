import math
from abc import ABC, abstractmethod

# Interface for calculable objects
class Calculable(ABC):
    @abstractmethod
    def calcularArea(self):
        pass
    
    @abstractmethod
    def calcularPerimetro(self):
        pass

# Abstract base class for geometric figures
class FiguraGeometrica(Calculable):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

    def mostrarInformacion(self):
        print(f"Figura: {self.nombre}")

# Concrete class for Circle
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcularArea(self):
        return math.pi * (self.radio ** 2)

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio

# Concrete class for Rectangle
class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)

# Concrete class for Triangle
class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, lado2=None, lado3=None):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura
        self.lado2 = lado2 if lado2 else base
        self.lado3 = lado3 if lado3 else base

    def calcularArea(self):
        return (self.base * self.altura) / 2

    def calcularPerimetro(self):
        return self.base + self.lado2 + self.lado3

# Test the implementation
figuras = [Circulo(6), Rectangulo(2, 8), Triangulo(4, 8)]

print("Tabla de Figuras Geométricas")
print("---------------------------")
for f in figuras:
    f.mostrarInformacion()
    print(f"Área: {f.calcularArea():.2f}")
    print(f"Perímetro: {f.calcularPerimetro():.2f}")
    print("---------------------------")