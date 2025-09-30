## Ejercicio 38: Creación del juego Tres en Línea (Tic Tac Toe)

import random
from IPython.display import clear_output

# --------------------------------------------------------
# Clase que representa el tablero del juego
# --------------------------------------------------------
class TableroDeJuego:
    def __init__(self):
        """Constructor que inicializa el tablero vacío."""
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]

    def set_tablero(self, tablero):
        """Permite modificar el tablero completo."""
        self.tablero = tablero

    def insertar_simbolo(self, simbolo, posicion):
        """
        Inserta un símbolo ('X' u 'O') en la posición indicada.
        Parámetros:
            simbolo (str): 'X' o 'O'
            posicion (tuple): (i, j) coordenadas
        Retorna True si se insertó correctamente, False si la posición estaba ocupada.
        """
        i, j = posicion
        if self.tablero[i][j] == ' ':
            self.tablero[i][j] = simbolo
            return True
        return False

    def mostrar_tabla(self):
        """Muestra el tablero de juego."""
        print("\n")
        for fila in self.tablero:
            print("-" * 9)
            print("|".join(f" {x} " for x in fila))
        print("-" * 9)

    def reiniciar(self):
        """Reinicia el tablero a vacío."""
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]

    def estado_del_juego(self):
        """
        Verifica el estado del juego.
        Retorna:
          - 'X' si gana X
          - 'O' si gana O
          - 'Empate' si no hay espacios vacíos
          - None si el juego sigue
        """

        # Verificar filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != ' ':
                return fila[0]

        # Verificar columnas
        for c in range(3):
            if (self.tablero[0][c] == self.tablero[1][c] == self.tablero[2][c]) and self.tablero[0][c] != ' ':
                return self.tablero[0][c]

        # Verificar diagonales
        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] and self.tablero[0][0] != ' ') or \
           (self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] and self.tablero[1][1] != ' '):
            return self.tablero[1][1]

        # Verificar empate
        for fila in self.tablero:
            if ' ' in fila:
                return None
        return "Empate"


# --------------------------------------------------------
# Clase Jugador
# --------------------------------------------------------
class Jugador:
    def __init__(self):
        """Permite al jugador elegir su símbolo."""
        simbolo = ''
        while simbolo not in ['X', 'O']:
            simbolo = input("Ingrese el símbolo con el que desea jugar [X/O]: ").upper().strip()
        self.simbolo = simbolo


# --------------------------------------------------------
# Clase Juego
# --------------------------------------------------------
class Juego:
    def __init__(self):
        """Constructor principal del juego."""
        self.tablero_juego = TableroDeJuego()
        self.jugador = Jugador()
        self.puntuacion = {'X': 0, 'O': 0}

        # Asignar símbolo del ordenador
        self.ordenador = 'O' if self.jugador.simbolo == 'X' else 'X'

        # Elegir al azar quién inicia
        self.jugador_actual = random.choice(['X', 'O'])
        if self.jugador_actual == self.jugador.simbolo:
            print(f"\nComienza el jugador humano ({self.jugador.simbolo})")
        else:
            print(f"\nComienza el ordenador ({self.ordenador})")

    def jugar(self):
        """Método principal para jugar Tic Tac Toe."""
        self.tablero_juego.mostrar_tabla()

        while True:
            # Mostrar turno
            print(f"\nTurno del jugador ({self.jugador_actual})")

            # Si es el turno del jugador humano
            if self.jugador_actual == self.jugador.simbolo:
                try:
                    x, y = map(int, input("Ingrese las coordenadas (fila columna) [0-2 0-2]: ").split())
                    if x not in range(3) or y not in range(3):
                        print("Coordenadas fuera del rango (0-2). Intente de nuevo.")
                        continue
                except ValueError:
                    print("Entrada inválida. Debe ingresar dos números separados por un espacio.")
                    continue
            else:
                # Turno del ordenador (elige al azar)
                posiciones_disponibles = [(i, j) for i in range(3) for j in range(3) if self.tablero_juego.tablero[i][j] == ' ']
                if posiciones_disponibles:
                    x, y = random.choice(posiciones_disponibles)
                    print(f"El ordenador eligió: {x} {y}")

            # Intentar colocar el símbolo
            if not self.tablero_juego.insertar_simbolo(self.jugador_actual, (x, y)):
                print("Esa posición ya está ocupada. Intente otra.")
                continue

            clear_output(wait=True)
            self.tablero_juego.mostrar_tabla()

            # Verificar estado
            estado = self.tablero_juego.estado_del_juego()
            if estado:
                if estado == "Empate":
                    print("\n¡Empate!")
                else:
                    print(f"\n¡El jugador con símbolo '{estado}' ha ganado!")
                    self.puntuacion[estado] += 1
                break

            # Cambiar turno
            self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'

        # Mostrar puntuación final
        print("\nPuntuación actual:")
        print(f"Jugador ({self.jugador.simbolo}): {self.puntuacion[self.jugador.simbolo]}")
        print(f"Ordenador ({self.ordenador}): {self.puntuacion[self.ordenador]}")


# --------------------------------------------------------
# Programa principal
# --------------------------------------------------------
if __name__ == "__main__":
    juego = Juego()
    while True:
        juego.jugar()
        opcion = input("\n¿Desea jugar otra partida? [S/N]: ").strip().upper()
        if opcion != 'S':
            print("\nGracias por jugar. ¡Hasta la próxima!")
            break
        else:
            juego.tablero_juego.reiniciar()
