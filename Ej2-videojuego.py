class Personaje: # Clase padre
    def __init__(self, nombre, nivel): # constructor
        self.nombre = nombre
        self.nivel = nivel

    def atacar(self): # metodo
        print(f"{self.nombre} ataca con fuerza nivel {self.nivel}!") # mensaje


class Jugador(Personaje): # subclase que hereda de Personaje
    def __init__(self, nombre, nivel, clase):
        super().__init__(nombre, nivel) # llama al constructor
        self.clase = clase

    def usarHabilidadEspecial(self): # metodo
        print(f"{self.nombre} ({self.clase}) usa una habilidad especial de nivel {self.nivel}!")


class Enemigo(Personaje): # subclase
    def __init__(self, nombre, nivel, tipo):
        super().__init__(nombre, nivel) # llama al constructor
        self.tipo = tipo

    def gritar(self): # metodo
        print(f"¡El {self.tipo} {self.nombre} grita de dolor!")


# Salidas
jugador1 = Jugador("Betito", 13, "Guerrero")
enemigo1 = Enemigo("Antrax", 9, "Dragon")

jugador1.atacar()
jugador1.usarHabilidadEspecial()

enemigo1.atacar()
enemigo1.gritar()
