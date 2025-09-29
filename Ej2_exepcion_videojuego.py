# Custom exceptions
class InvalidLevelError(Exception):
    """Exception raised for invalid level values"""
    pass

class InsufficientLevelError(Exception):
    """Exception raised when level is too low for an action"""
    pass

class Personaje:
    def __init__(self, nombre, nivel):
        # Verify level is at least 1
        if nivel < 1:
            raise InvalidLevelError(f"Level cannot be less than 1. Received: {nivel}")
        
        self.nombre = nombre
        self.nivel = nivel

    def atacar(self):
        # Verify level is at least 5 to attack
        if self.nivel < 5:
            raise InsufficientLevelError(f"{self.nombre} needs at least level 5 to attack. Current level: {self.nivel}")
        
        print(f"{self.nombre} attacks with level {self.nivel} strength!")


class Jugador(Personaje):
    def __init__(self, nombre, nivel, clase):
        super().__init__(nombre, nivel)
        self.clase = clase

    def usarHabilidadEspecial(self):
        print(f"{self.nombre} ({self.clase}) uses a special ability of level {self.nivel}!")


class Enemigo(Personaje):
    def __init__(self, nombre, nivel, tipo):
        super().__init__(nombre, nivel)
        self.tipo = tipo

    def gritar(self):
        print(f"The {self.tipo} {self.nombre} screams in pain!")


# Test the implementation with exceptions
try:
    # Test valid characters
    print("Testing valid characters:")
    personajes = [
        Jugador("Betito", 13, "Warrior"),
        Enemigo("Antrax", 9, "Dragon")
    ]

    for p in personajes:
        p.atacar()

    # Test specific methods
    personajes[0].usarHabilidadEspecial()
    personajes[1].gritar()

    # Test invalid level
    print("\nTesting invalid level:")
    invalid_character = Personaje("Test", 0)  # This will raise an exception

except InvalidLevelError as e:
    print(f"Error creating character: {e}")

try:
    # Test insufficient level for attack
    print("\nTesting insufficient level for attack:")
    weak_character = Personaje("Newbie", 3)
    weak_character.atacar()  # This will raise an exception

except InsufficientLevelError as e:
    print(f"Error during attack: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")