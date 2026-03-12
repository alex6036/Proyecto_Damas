class Jugador:

    def __init__(self, nombre, simbolo):
        self.nombre = nombre
        self.simbolo = simbolo
        self.cambios_nombre = 0
        self.cambios_caracter = 0

    def cambiar_nombre(self, nuevo_nombre):
        if 6 <= len(nuevo_nombre) <= 12 and nuevo_nombre.isalnum():
            self.nombre = nuevo_nombre
            self.cambios_nombre += 1
            return True
        return False

    def cambiar_simbolo(self, nuevo_simbolo):
        self.simbolo = nuevo_simbolo
        self.cambios_caracter += 1