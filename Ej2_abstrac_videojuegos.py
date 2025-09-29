from abc import ABC, abstractmethod

# Abstract base class for characters
class Personaje(ABC):
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
    
    @abstractmethod
    def atacar(self):
        pass

# Interface for magical abilities
class HabilidadesMagicas(ABC):
    @abstractmethod
    def lanzarHechizo(self, hechizo):
        pass
    
    @abstractmethod
    def usarMagiaElemental(self, elemento):
        pass

# Interface for physical abilities
class HabilidadesFisicas(ABC):
    @abstractmethod
    def ataqueFisico(self):
        pass
    
    @abstractmethod
    def defender(self):
        pass

# Player class with physical abilities
class Jugador(Personaje, HabilidadesFisicas):
    def __init__(self, nombre, nivel, clase):
        super().__init__(nombre, nivel)
        self.clase = clase
    
    def atacar(self):
        print(f"{self.nombre} ataca con fuerza nivel {self.nivel}!")
    
    def ataqueFisico(self):
        print(f"{self.nombre} realiza un poderoso ataque físico nivel {self.nivel}!")
    
    def defender(self):
        print(f"{self.nombre} se defiende con su escudo nivel {self.nivel}!")
    
    def usarHabilidadEspecial(self):
        print(f"{self.nombre} ({self.clase}) usa una habilidad especial de nivel {self.nivel}!")

# Enemy class with magical abilities
class Enemigo(Personaje, HabilidadesMagicas):
    def __init__(self, nombre, nivel, tipo):
        super().__init__(nombre, nivel)
        self.tipo = tipo
    
    def atacar(self):
        print(f"{self.nombre} ataca con maldad nivel {self.nivel}!")
    
    def lanzarHechizo(self, hechizo):
        print(f"{self.nombre} lanza el hechizo '{hechizo}' nivel {self.nivel}!")
    
    def usarMagiaElemental(self, elemento):
        print(f"{self.nombre} invoca magia de {elemento} nivel {self.nivel}!")
    
    def gritar(self):
        print(f"¡El {self.tipo} {self.nombre} grita de dolor!")

# Hybrid character with both abilities
class PersonajeHibrido(Personaje, HabilidadesMagicas, HabilidadesFisicas):
    def __init__(self, nombre, nivel, clase):
        super().__init__(nombre, nivel)
        self.clase = clase
    
    def atacar(self):
        print(f"{self.nombre} ataca con poder equilibrado nivel {self.nivel}!")
    
    def lanzarHechizo(self, hechizo):
        print(f"{self.nombre} lanza el hechizo '{hechizo}' nivel {self.nivel}!")
    
    def usarMagiaElemental(self, elemento):
        print(f"{self.nombre} controla el elemento {elemento} nivel {self.nivel}!")
    
    def ataqueFisico(self):
        print(f"{self.nombre} ejecuta un combo físico nivel {self.nivel}!")
    
    def defender(self):
        print(f"{self.nombre} se protege con magia y armadura nivel {self.nivel}!")
    
    def mostrarHabilidades(self):
        print(f"{self.nombre} es un {self.clase} con habilidades mágicas y físicas!")

# Test the implementation
print("=== SISTEMA DE PERSONAJES DEL VIDEOJUEGO ===")
print()

# Create characters
personajes = [
    Jugador("Betito", 13, "Guerrero"),
    Enemigo("Antrax", 9, "Dragón"),
    PersonajeHibrido("Mystera", 15, "Paladín Mágico")
]

# Demonstrate polymorphism
print("--- ATAQUES DE PERSONAJES ---")
for p in personajes:
    p.atacar()
print()

# Demonstrate specific abilities
print("--- HABILIDADES ESPECÍFICAS ---")
personajes[0].ataqueFisico()  # Physical abilities
personajes[0].defender()

personajes[1].lanzarHechizo("Bola de Fuego")  # Magical abilities
personajes[1].usarMagiaElemental("Fuego")

personajes[2].mostrarHabilidades()  # Hybrid abilities
personajes[2].ataqueFisico()
personajes[2].lanzarHechizo("Curación")
personajes[2].defender()
print()

# Special methods
print("--- MÉTODOS ESPECIALES ---")
personajes[0].usarHabilidadEspecial()
personajes[1].gritar()