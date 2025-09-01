class Paleta: # clase padre
    def __init__(self, sabor, precio): # constructor
        self.sabor = sabor
        self.precio = precio

    def mostrarInformacion(self): # metodo
        print(f"Paleta de sabor {self.sabor}, precio: ${self.precio}")


class PaletaAgua(Paleta): # subclase
    def __init__(self, sabor, precio, baseAgua):
        super().__init__(sabor, precio) 
        self.baseAgua = baseAgua

    def mostrarBaseAgua(self): # metodo
        print(f"¿Es de base de agua?: {'Sí' if self.baseAgua else 'No'}") 


class PaletaCrema(Paleta): # subclase
    def __init__(self, sabor, precio, cremosa):
        super().__init__(sabor, precio)
        self.cremosa = cremosa

    def mostrarTexturaCremosa(self): # metodo
        print(f"¿Es cremosa?: {'Sí' if self.cremosa else 'No'}")

# salidas
p1 = PaletaAgua("Mango", 15, True)
p2 = PaletaCrema("Fresas con crema", 20, True)

p1.mostrarInformacion()
p1.mostrarBaseAgua()
p1.precio += 2   # aumenta 2 pesos
print(f"Nuevo precio: ${p1.precio}")

p2.mostrarInformacion()
p2.mostrarTexturaCremosa()
p2.precio += 6   # aumenta 6 pesos
print(f"Nuevo precio: ${p2.precio}")
