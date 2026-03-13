import random
from jugador import Jugador
from tablero import Tablero


class Juego:

    def __init__(self):

        self.tablero = Tablero()

        self.jugadores = self.crear_jugadores()

        self.turno = "n"

        self.estadisticas = {
            "turnos": 0,
            "comidas_n": 0,
            "comidas_b": 0,
            "movimientos_totales": 0
        }

    def crear_jugadores(self):

        jugadores = []

        for i in range(2):

            while True:

                nombre = input("Nombre del jugador: ")

                if 6 <= len(nombre) <= 12 and nombre.isalnum():

                    jugadores.append(nombre)

                    break

        random.shuffle(jugadores)

        jugador1 = Jugador(jugadores[0], "n")
        jugador2 = Jugador(jugadores[1], "b")

        return {"n": jugador1, "b": jugador2}

    def iniciar(self):

        self.tablero.imprimir()

        while True:

            jugador = self.jugadores[self.turno]

            print(f"Turno de {jugador.nombre}")

            origen = input("Origen: ")
            destino = input("Destino: ")

            # aquí iría la lógica de mover

            self.turno = "b" if self.turno == "n" else "n"