class Tablero:

    def __init__(self):
        self.tablero = self.crear_tablero()

    def crear_tablero(self):
        tablero = []

        for fila in range(8):
            f = []
            for col in range(8):

                if (fila + col) % 2 == 0:
                    f.append(" ")

                else:
                    if fila < 3:
                        f.append("n")
                    elif fila > 4:
                        f.append("b")
                    else:
                        f.append(".")

            tablero.append(f)

        return tablero

    def imprimir(self):

        print("   A  B  C  D  E  F  G  H")
        print("  ╔" + "═══╦" * 7 + "═══╗")

        for i, fila in enumerate(self.tablero):

            fila_s = " ║ ".join(fila)

            print(f"{i+1} ║ {fila_s} ║")

            if i < 7:
                print("  ╠" + "═══╬" * 7 + "═══╣")
            else:
                print("  ╚" + "═══╩" * 7 + "═══╝")