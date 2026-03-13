class Movimiento:

    @staticmethod
    def mover_pieza(tablero, origen, destino, turno):

        fila_origen, col_origen = origen
        fila_destino, col_destino = destino

        pieza = tablero[fila_origen][col_origen]

        if pieza.lower() != turno:
            return False

        if tablero[fila_destino][col_destino] != ".":
            return False

        tablero[fila_destino][col_destino] = pieza
        tablero[fila_origen][col_origen] = "."

        return True