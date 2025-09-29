from abc import ABC, abstractmethod

# Abstract base class for all ice pops
class Paleta(ABC):
    def __init__(self, sabor, precio):
        self.sabor = sabor
        self.precio = precio
    
    @abstractmethod
    def mostrar_informacion(self):
        pass
    
    @abstractmethod
    def obtener_tipo(self):
        pass

# Interface for water-based products
class ConBaseAgua(ABC):
    @abstractmethod
    def mostrar_base_agua(self):
        pass

# Interface for cream-based products
class ConTexturaCremosa(ABC):
    @abstractmethod
    def mostrar_textura_cremosa(self):
        pass

# Water-based ice pop class
class PaletaAgua(Paleta, ConBaseAgua):
    def __init__(self, sabor, precio):
        super().__init__(sabor, precio)
        self.base_agua = True
    
    def mostrar_informacion(self):
        print(f"Paleta de agua sabor {self.sabor}, precio: ${self.precio}")
    
    def obtener_tipo(self):
        return "Paleta de Agua"
    
    def mostrar_base_agua(self):
        print(f"Base de agua: Sí")

# Cream-based ice pop class
class PaletaCrema(Paleta, ConTexturaCremosa):
    def __init__(self, sabor, precio):
        super().__init__(sabor, precio)
        self.cremosa = True
    
    def mostrar_informacion(self):
        print(f"Paleta de crema sabor {self.sabor}, precio: ${self.precio}")
    
    def obtener_tipo(self):
        return "Paleta de Crema"
    
    def mostrar_textura_cremosa(self):
        print(f"Textura cremosa: Sí")

# Test the implementation
print("=== PALETERÍA CON CLASES ABSTRACTAS E INTERFACES ===")
print()

paletas = [
    PaletaAgua("Mango", 15),
    PaletaCrema("Fresas con crema", 20)
]

print("--- INFORMACIÓN DE PALETAS ---")
for p in paletas:
    p.mostrar_informacion()
    print(f"Tipo: {p.obtener_tipo()}")
    
    if isinstance(p, ConBaseAgua):
        p.mostrar_base_agua()
    
    if isinstance(p, ConTexturaCremosa):
        p.mostrar_textura_cremosa()
    
    print("---------------------------")