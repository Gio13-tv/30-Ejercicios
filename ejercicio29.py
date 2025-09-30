# Ejercicio 29: Creación del juego Piedra, Papel o Tijeras

import random

class PiedraPapelTijeras:
    def __init__(self):
        # Constructor: inicializa los atributos de la clase
        # Lista con las opciones posibles
        self.opciones = ["Piedra", "Papel", "Tijeras"]
        
        # Diccionario para registrar partidas ganadas, perdidas o empatadas
        self.puntajes = {"Ganado": 0, "Perdido": 0, "Empate": 0}
        
        # Resultado de la partida actual
        self.resultado = None
        
        # Historial de partidas (tuplas con (jugador, computadora))
        self.historial = []

    def obtener_resultado(self):
        """Devuelve el resultado de la última partida."""
        return self.resultado

    def ultima_eleccion_jugador(self):
        """Devuelve la última elección del jugador."""
        if self.historial:
            return self.historial[-1][0]
        return None

    def ultima_eleccion_ordenador(self):
        """Devuelve la última elección del ordenador."""
        if self.historial:
            return self.historial[-1][1]
        return None

    def obtener_puntuacion_jugador(self):
        """Devuelve el puntaje acumulado del jugador."""
        return self.puntajes

    def jugar_de_nuevo(self):
        """Pregunta si el jugador desea jugar otra partida."""
        return input("¿Deseas jugar otra partida? [S/N]: ").strip().upper()

    def obtener_historial(self):
        """Devuelve el historial de partidas."""
        return self.historial

    def jugar(self):
        """Inicia una partida del juego."""
        print("\nOpciones disponibles:", ", ".join(self.opciones))
        eleccion_jugador = input("Introduce tu elección: ").capitalize().strip()

        # Validar entrada
        if eleccion_jugador not in self.opciones:
            print("Opción no válida. Intenta de nuevo.")
            return

        # Elección aleatoria del ordenador
        eleccion_computadora = random.choice(self.opciones)
        print(f"Elección de la computadora: {eleccion_computadora}")

        # Registrar en el historial
        self.historial.append((eleccion_jugador, eleccion_computadora))

        # Determinar resultado
        if eleccion_jugador == eleccion_computadora:
            self.resultado = "Empate"
            self.puntajes["Empate"] += 1
        elif (
            (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijeras") or
            (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or
            (eleccion_jugador == "Tijeras" and eleccion_computadora == "Papel")
        ):
            self.resultado = "Ganado"
            self.puntajes["Ganado"] += 1
        else:
            self.resultado = "Perdido"
            self.puntajes["Perdido"] += 1

        # Mostrar resultado
        print(f"Resultado de la partida: {self.resultado}")

    def mostrar_resultado_final(self):
        """Muestra el resultado acumulado al final del juego."""
        print("\n--- RESULTADO FINAL ---")
        print(f"Ganadas: {self.puntajes['Ganado']}")
        print(f"Perdidas: {self.puntajes['Perdido']}")
        print(f"Empates: {self.puntajes['Empate']}")
        print("------------------------")


# Programa principal
if __name__ == "__main__":
    partida = PiedraPapelTijeras()

    jugar_una_partida = input("¿Quieres jugar una partida? [S/N]: ").strip().upper()
    turno = 0

    while jugar_una_partida == "S":
        turno += 1
        print(f"\n--- Turno #{turno} ---")
        partida.jugar()
        print("-" * 30)
        jugar_una_partida = partida.jugar_de_nuevo()

    # Mostrar resumen final
    print("\n¡La partida ha terminado!\n")
    print("Historial de partidas jugadas:")
    for i, (jug, comp) in enumerate(partida.obtener_historial(), start=1):
        print(f"Partida {i}: Jugador -> {jug}, Computadora -> {comp}")

    print()
    print("Tu puntuación:", partida.obtener_puntuacion_jugador())
    partida.mostrar_resultado_final()
