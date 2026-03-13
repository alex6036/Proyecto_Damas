import random # Utilizaremos la biblioteca random 
# VARIABLES GLOBALES
SIMBOLO_BLANCAS = 'b'
SIMBOLO_NEGRAS = 'n'
#Pide el nombre de los jugadores
def nombre_jugadores():
    jugadores = [] # Almacena el nombre de los jugadores
    for _ in range(2):
        while True:
            nombre = input("Escribe el nombre del jugador (6-12 caracteres alfanuméricos)\n")
            if 6 <= len(nombre) <= 12 and nombre.isalnum(): # Verifica que las condiciones se cumplan
                jugadores.append(nombre) # Si se cumple la condicion mete el nombre en la lista
                break
            else:
                print("No cumple con los requisitos") #Si no cumple con la condición te imprime esto
    return jugadores

# Sortea el orden en que van a jugar los jugadores
def sorteo(jugadores):
    random.shuffle(jugadores) #la función shuffle pertenece a la biblioteca random y hace que sea aleatoria el orden de los jugadores
    print(f"{jugadores[0]} jugará con las fichas negras (n) y {jugadores[1]} jugará con las fichas blancas (b).\n")
    return {SIMBOLO_NEGRAS: jugadores[0], SIMBOLO_BLANCAS: jugadores[1]}

#Genera el tablero
def tablero():
    tablero = [] # Vamos a quenerear una matriz donde se van a jugardar las filas y las columnas del tablero
    for fila in range(8):
        f1 = []
        for columna in range(8):
            if (fila + columna) % 2 == 0:
                f1.append(" ")
            else:
                if fila < 3:
                    f1.append(SIMBOLO_NEGRAS)  # Piezas negras
                elif fila > 4:
                    f1.append(SIMBOLO_BLANCAS)  # Piezas blancas
                else:
                    f1.append(".")  # Espacios vacíos
        tablero.append(f1)
    return tablero

# Imprime como lo vamos a ver en el terminal 
def imprimir_tablero(tablero):
    print("   "+" A "+"  B "+"  C "+"  D "+"  E "+"  F "+"  G "+"  H ") 
    print("  ╔" + "═══╦" * 7 + "═══╗")
    for i, fila in enumerate(tablero): # enumerate agrega un contador a cada elemento de una lista
        fila_s = " ║ ".join(fila) # .join() toma todos los elementos de una lista y los une en una cadena, usando el " ║ " como separador entre cada elemento de la lista.
        print(f"{i+1} ║ {fila_s} ║")
        if i < 7:
            print("  ╠" + "═══╬" * 7 + "═══╣")
        else:
            print("  ╚" + "═══╩" * 7 + "═══╝")

# Nos tranforma las coordenadas ej 3a a 3 1
def coordenadas(coordenada):
    letras = "ABCDEFGH"
    #Verificamos que las coordenadas no sean 0 o lo que introducimos sea menor que dos
    if not coordenada or len(coordenada) < 2:
        return False
    # Separamos las partes en letras y numeros
    fila_s = coordenada[:-1]
    letra = coordenada[-1].upper()
    #Con prueba que si la variable letra esta en la variable letras y que la parte fila_s son numeros
    if letra not in letras or not fila_s.isdigit(): # Verifica si la parte de letra esta en lo de letras y ferifica si fila_s son numero
        return False
    #Transforma fila_s en int para poder restar 1 y lo colocamos en una variable
    fila = int(fila_s) - 1
    col = letras.index(letra)
    # verificamos que las filas no sea un numero negativo junto a la columna y que las columnas sean mayor o igual a las letras y que las filas sea mayor o igual a 8
    if fila < 0 or fila >= 8 or col < 0 or col >= 8:
        return False
    return fila, col

# Esta fución mueves las piezas
def mover_pieza(tabla, origen, destino, turno): # 
    fila_origen, col_origen = origen # Donde esta la ficha
    fila_destino, col_destino = destino # Donde quiero que se mueva
    # Verifica que los movimientos esten entre los espacios específicos 
    if not (0 <= fila_origen < 8 and 0 <= col_origen < 8 and 0 <= fila_destino < 8 and 0 <= col_destino < 8):
        print("Movimiento fuera de los límites del tablero.")
        return False
    pieza = tabla[fila_origen][col_origen] # Verifica que tipo de ficha es (n o b)
    # Verifica que la pieza pertenece al turno actual
    if pieza.lower() != turno: # Si la pieza es una reina le vuelve a una letra minuscula y compara
        print(f"Es el turno de '{turno}', pero seleccionaste '{pieza}'.")
        return False
    # Verifica que el destino este vacío
    if tabla[fila_destino][col_destino] != '.':
        print("El destino no está vacío.")
        return False
    # Movimiento de piezas básicas
    if pieza == turno:
        # Solo puede moverse un paso en diagonal hacia adelante
        if abs(fila_destino - fila_origen) != 1 or abs(col_destino - col_origen) != 1: # Usamos la función abs para cuando te da negativo te lo vuelve positivo
            print("Solo se permiten movimientos diagonales de un paso para piezas básicas.")
            return False
        # Las piezas negras solo pueden moverse hacia abajo
        if turno == SIMBOLO_NEGRAS and fila_destino <= fila_origen:
            print("Las piezas negras solo pueden moverse hacia adelante (hacia abajo).")
            return False
        # Las piezas blancas solo pueden moverse hacia arriba
        if turno == SIMBOLO_BLANCAS and fila_destino >= fila_origen:
            print("Las piezas blancas solo pueden moverse hacia adelante (hacia arriba).")
            return False
    # Movimiento de pieza reina
    elif pieza == turno.upper():
        # Solo puede moverse en línea diagonal
        if abs(fila_destino - fila_origen) != abs(col_destino - col_origen):
            print("Las reinas solo pueden moverse en línea diagonal.")
            return False
        # Verifica el camino de la reina
        if fila_destino > fila_origen: # Si la reina se mueve hacia abajo fila destino es mayor que fila origen
            paso_fila = 1
        else:
            paso_fila = -1

        if col_destino > col_origen: # Si la reina se mueve hacia la derecha la columna destino es mayor que columna origen
            paso_col = 1
        else:
            paso_col = -1
        # Calcula la posiciones
        fila_actual, col_actual = fila_origen + paso_fila, col_origen + paso_col
        # Nos metemos en un bucle para ver si la pieza se puede mover
        while fila_actual != fila_destino and col_actual != col_destino: # mientras esto no se cumpla el bucle continua
            if tabla[fila_actual][col_actual] != '.': # Si esta condición se cumple 
                fila_actual2, col_actual2 = fila_actual + paso_fila, col_actual + paso_col
                if  tabla[fila_actual][col_actual] == turno.lower() or tabla[fila_actual][col_actual] == turno.upper():
                    print("El camino hacia el destino está bloqueado.")
                    return False
                if tabla[fila_actual2][col_actual2] != '.':
                    print("El camino hacia el destino está bloqueado.")
                    return False
                tabla[fila_actual][col_actual] = '.'
                fila_actual += paso_fila # Si el if no se cumple a fila_actual se suma 1
                col_actual += paso_col # Si el if no se cumple a col_actual se suma 1
            fila_actual += paso_fila # Si el if no se cumple a fila_actual se suma 1
            col_actual += paso_col # Si el if no se cumple a col_actual se suma 1
    # Realizar el movimiento
    tabla[fila_destino][col_destino] = pieza
    tabla[fila_origen][col_origen] = '.'
    # Coronar si es una pieza básica que llega a la última fila
    if turno == SIMBOLO_NEGRAS and fila_destino == 7:
        tabla[fila_destino][col_destino] = SIMBOLO_NEGRAS
        print("Tu ficha negra se ha convertido en reina")
    elif turno == SIMBOLO_BLANCAS and fila_destino == 0:
        tabla[fila_destino][col_destino] = SIMBOLO_BLANCAS
        print("Tu ficha blanca se ha convertido en reina")
    return True

# Esta fución come las piezas
def comer_pieza(tabla, origen, destino, turno):
    fila_origen, col_origen = origen # Sacamos las coordenadas de la ficha 
    fila_destino, col_destino = destino # Colocamos las coordenadas de la ficha a colocar
    pieza = tabla[fila_origen][col_origen] # Sacamos la pieza  del jugador es decir (n o b)
    if turno == SIMBOLO_NEGRAS or turno == SIMBOLO_NEGRAS.upper(): # Si se cumple esta condición sus oponentes son b y B
        oponente = SIMBOLO_BLANCAS
        oponente_reina = SIMBOLO_BLANCAS.upper()
    else: # Si no se cumple la condición sus oponentes son n y B
        oponente = SIMBOLO_NEGRAS
        oponente_reina = SIMBOLO_NEGRAS.upper()
    if pieza == turno:
        # Verifica si se puede comer
        if abs(fila_destino - fila_origen) != 2 or abs(col_destino - col_origen) != 2:
            print("El movimiento no es válido para comer.")
            return False
        # Verificamos si hay una pieza en el medio
        fila_intermedia = (fila_origen + fila_destino) // 2
        col_intermedia = (col_origen + col_destino) // 2
        # Verificamos si hay una pieza del oponente en el medio
        if tabla[fila_intermedia][col_intermedia] not in [oponente, oponente_reina]:
            print("No hay una pieza del oponente para comer en el camino.")
            return False
        # Verificamos si el destino de la ficha esta vacia
        if tabla[fila_destino][col_destino] != '.':
            print("El destino no está vacío.")
            return False
        # Realizamos el movimiento de comer
        tabla[fila_destino][col_destino] = pieza
        tabla[fila_origen][col_origen] = '.'
        tabla[fila_intermedia][col_intermedia] = '.'
        # Coronar si llega a la última fila
        if turno == SIMBOLO_NEGRAS and fila_destino == 7:
            tabla[fila_destino][col_destino] = SIMBOLO_NEGRAS.upper()
            print("¡Tu ficha negra se ha convertido en reina!")
        elif turno == SIMBOLO_BLANCAS and fila_destino == 0:
            tabla[fila_destino][col_destino] = SIMBOLO_BLANCAS.upper()
            print("¡Tu ficha blanca se ha convertido en reina!")
        return True
    elif pieza == turno.upper():
        # Solo puede moverse en línea diagonal
        if abs(fila_destino - fila_origen) != abs(col_destino - col_origen):
            print("Las reinas solo pueden moverse en línea diagonal.")
            return False
        # Verifica el camino de la reina
        if fila_destino > fila_origen: # Si la reina se mueve hacia abajo fila destino es mayor que fila origen
            paso_fila = 1
        else:
            paso_fila = -1

        if col_destino > col_origen: # Si la reina se mueve hacia la derecha la columna destino es mayor que columna origen
            paso_col = 1
        else:
            paso_col = -1
        # Calcula la posiciones
        fila_actual, col_actual = fila_origen + paso_fila, col_origen + paso_col
        # Nos metemos en un bucle para ver si la pieza se puede mover
        while fila_actual != fila_destino and col_actual != col_destino: # mientras esto no se cumpla el bucle continua
            if tabla[fila_actual][col_actual] != '.': # Si esta condición se cumple 
                fila_actual2, col_actual2 = fila_actual + paso_fila, col_actual + paso_col
                if  tabla[fila_actual][col_actual] == turno.lower() or tabla[fila_actual][col_actual] == turno.upper():
                    print("El camino hacia el destino está bloqueado.")
                    return False
                if tabla[fila_actual2][col_actual2] != '.':
                    print("El camino hacia el destino está bloqueado.")
                    return False
                tabla[fila_actual][col_actual] = '.'
                fila_actual += paso_fila # Si el if no se cumple a fila_actual se suma 1
                col_actual += paso_col # Si el if no se cumple a col_actual se suma 1
            fila_actual += paso_fila # Si el if no se cumple a fila_actual se suma 1
            col_actual += paso_col # Si el if no se cumple a col_actual se suma 1
    # Realizar el movimiento
        tabla[fila_destino][col_destino] = pieza
        tabla[fila_origen][col_origen] = '.'
        return True
# puedo comer otro
def puede_comer_otro(tabla, posicion, turno):
    # Posición de una pieza
    fila, col = posicion
    if turno == SIMBOLO_NEGRAS or turno == SIMBOLO_NEGRAS.upper(): # Si esta condición se cumple
        oponente = SIMBOLO_BLANCAS # Este es su oponente
    else: # Si la condición anterior no se cumple 
        oponente = SIMBOLO_NEGRAS #Este es su oponente

    # Creamos una lista que al mismo tiempo cada parte es una tupla
    direcciones = [(-2, -2), (-2, 2), (2, -2), (2, 2)]  
    #Creamos un for en donde df es diagonal fila y dc es diagonal columna
    for df, dc in direcciones:
        nueva_fila, nueva_col = fila + df, col + dc
        fila_intermedia, col_intermedia = fila + df // 2, col + dc // 2
        # Restricción para evitar moverse hacia atrás con piezas normales
        if turno == SIMBOLO_NEGRAS and df < 0:  # Negras no pueden moverse hacia arriba
            continue
        if turno == SIMBOLO_BLANCAS and df > 0:  # Blancas no pueden moverse hacia abajo
            continue
        # Verificar condiciones para comer
        if (
            0 <= nueva_fila < 8 and 0 <= nueva_col < 8 and # Verifica que el tablero este dentro del tablero
            tabla[fila_intermedia][col_intermedia].lower() == oponente and # Verifica que si la pieza intermedia es tu oponente
            tabla[nueva_fila][nueva_col] == '.' # Verifica que si la posición a la que se puede moves este vacio 
        ):
            return True
    return False

# Esta función analiza es estado del tablero
def puede_mover(tabla, turno):
    # Creamos una lista que contiene las direcciones posibles de movimiento
    direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonales
    # Recorremos el tablero
    for fila in range(8):
        for col in range(8):
            # Verificamos las piezas
            if tabla[fila][col] == turno or tabla[fila][col] == SIMBOLO_NEGRAS or tabla[fila][col] == SIMBOLO_BLANCAS:
                for df, dc in direcciones:  # Desempaquetamos las tuplas
                    nueva_fila, nueva_col = fila + df, col + dc
                    # Verificamos si la nueva posición esta dentro del tablero y es una casilla vacia
                    if 0 <= nueva_fila < 8 and 0 <= nueva_col < 8 and tabla[nueva_fila][nueva_col] == '.':
                        return True  # Hay al menos un movimiento válido
                    # Verificamps si podemos comer
                    if 0 <= fila + 2 * df < 8 and 0 <= col + 2 * dc < 8:
                        intermedia = (fila + df, col + dc)
                        destino = (fila + 2 * df, col + 2 * dc)
                        # Verificamos que la pieza del medio es del oponente y la casilla de destino este vacia
                        if (tabla[intermedia[0]][intermedia[1]] in (SIMBOLO_NEGRAS, SIMBOLO_BLANCAS) and 
                            tabla[intermedia[0]][intermedia[1]] != turno and 
                            tabla[destino[0]][destino[1]] == '.'):
                            return True  
    # No se encuentra ningun movimiento
    return False

def contar_fichas(tabla):
    negras = 0
    blancas = 0
    # Recorremos todo el tablero
    for fila in tabla:
        for pieza in fila:
            if pieza == SIMBOLO_NEGRAS or pieza == SIMBOLO_NEGRAS.upper():  # Contamos las piezas negras (normales o reinas)
                negras += 1
            elif pieza == SIMBOLO_BLANCAS or pieza == SIMBOLO_BLANCAS.upper():  # Contamos las piezas blancas (normales o reinas)
                blancas += 1
    return negras, blancas

def damas():
    global SIMBOLO_BLANCAS
    global SIMBOLO_NEGRAS
    jugadores = nombre_jugadores()
    asignacion = sorteo(jugadores)
    turno_actual = SIMBOLO_NEGRAS
    tablero_juego = tablero()
    imprimir_tablero(tablero_juego)

    # Estadísticas del juego
    estadisticas = {
        "turnos": 0,
        "comidas_n": 0,
        "comidas_b": 0,
        "movimientos_totales": 0,
    }

    # Contadores de cambios
    cambios_nombre = {
        SIMBOLO_NEGRAS: 0,
        SIMBOLO_BLANCAS: 0
        }
    cambios_caracter = {
        SIMBOLO_NEGRAS: 0,
        SIMBOLO_BLANCAS: 0
        }

    while True:
        print(f"Turno de: {asignacion[turno_actual]} ({turno_actual})")
        print(f"Estadísticas actuales: Turnos: {estadisticas['turnos']}, Fichas comidas: n={estadisticas['comidas_n']}, b={estadisticas['comidas_b']}")
        
        comando = input("Ingrese la posición de origen (ej. 3A) o un comando (!end, !cn, !cc): ").strip()

        # Comando !end: Finalizar el juego
        if comando == "!end":
            print("El juego ha sido terminado por solicitud de un jugador")
            break

        # Comando !changename o !cn: Cambiar nombre del jugador
        elif comando in ["!changename", "!cn"]:
            if cambios_nombre[turno_actual] >= 2:
                print("No puedes cambiar tu nombre más de dos veces.")
            else:
                while True:
                    nuevo_nombre = input("Escribe tu nuevo nombre (6-12 caracteres alfanuméricos): ").strip()
                    if 6 <= len(nuevo_nombre) <= 12 and nuevo_nombre.isalnum():
                        asignacion[turno_actual] = nuevo_nombre
                        cambios_nombre[turno_actual] += 1
                        print(f"Nombre cambiado con éxito. Nuevo nombre: {nuevo_nombre}")
                        break
                    else:
                        print("El nombre no cumple con los requisitos. Intenta nuevamente.")
            continue  

        # Comando !changechar o !cc: Cambiar carácter de las fichas
        elif comando in ["!changechar", "!cc"]:
            if cambios_caracter[turno_actual] >= 2:
                print("No puedes cambiar tu carácter más de dos veces.")
            else:
                while True:
                    nuevo_caracter = input("Elige un nuevo carácter para tus fichas (letra mayúscula): ").strip()

                    if turno_actual == SIMBOLO_BLANCAS:
                        oponente = SIMBOLO_NEGRAS
                    else:
                        oponente = SIMBOLO_BLANCAS

                    if len(nuevo_caracter) == 1 and nuevo_caracter != turno_actual and nuevo_caracter != oponente:
                        # Guardamos el turno actual antes de hacer el cambio de caracter
                        turno_original = turno_actual
                        # Cambiamos las piezas del jugador actual
                        for fila in range(8):
                            for col in range(8):
                                if tablero_juego[fila][col].lower() == turno_original:  # Sola las piezas del jugador
                                    if tablero_juego[fila][col].islower():
                                        tablero_juego[fila][col] = nuevo_caracter.lower()  # Ficha normal
                                    else:
                                        tablero_juego[fila][col] = nuevo_caracter.upper()  # Reina

                        # Incrementamos el contador de cambios usando el turno original
                        cambios_caracter[turno_original] += 1

                        asignacion[nuevo_caracter.lower()] = asignacion[turno_original]  # Actualizamos el nombre en asignacion
                        del asignacion[turno_original]  # Eliminamos el antiguo turno

                        # Cambiamos el turno actual
                        turno_actual = nuevo_caracter.lower()  # Esta línea asegura que turno_actual se actualice correctamente
                        if turno_actual == SIMBOLO_BLANCAS:
                            SIMBOLO_BLANCAS = nuevo_caracter.lower()
                        else:
                            SIMBOLO_NEGRAS = nuevo_caracter.lower()
                        print(f"Carácter cambiado con éxito. Nuevo carácter: {nuevo_caracter}")
                        imprimir_tablero(tablero_juego)
                
                        break
                    else:
                        print("El carácter no es válido. Intenta nuevamente.")
        
                    continue

        # Transformamos las coordenadas
        origen = coordenadas(comando)
        if origen is False:
            print("Coordenadas invalidas o comando no reconocido. Intenta de nuevo.")
            continue

        destino = input("Ingrese la posición de destino (ej. 4B): ").strip()
        destino = coordenadas(destino)

        if destino is False:
            print("Coordenadas inválidas. Intenta de nuevo.")
            continue
        
        movimiento_valido = False
        if abs(destino[0] - origen[0]) == abs(destino[1] - origen[1]):
            if comer_pieza(tablero_juego, origen, destino, turno_actual):
                imprimir_tablero(tablero_juego)
                movimiento_valido = True
                if turno_actual == SIMBOLO_NEGRAS:
                    estadisticas["comidas_n"] += 1
                else:
                    estadisticas["comidas_b"] += 1
                if puede_comer_otro(tablero_juego, destino, turno_actual):
                    print("¡Tienes otra captura obligatoria! Debes seguir comiendo.")
                    continue
        if abs(destino[0] - origen[0]) == 2:  # movimiento para comer
            if comer_pieza(tablero_juego, origen, destino, turno_actual):
                imprimir_tablero(tablero_juego)
                movimiento_valido = True
                if turno_actual == SIMBOLO_NEGRAS:
                    estadisticas["comidas_n"] += 1
                else:
                    estadisticas["comidas_b"] += 1
                if puede_comer_otro(tablero_juego, destino, turno_actual):
                    print("¡Tienes otra captura obligatoria! Debes seguir comiendo.")
                    continue
        elif mover_pieza(tablero_juego, origen, destino, turno_actual): # mover pieza
            imprimir_tablero(tablero_juego)
            movimiento_valido = True
        else:
            print("Intento de movimiento inválido.")
        
        if movimiento_valido: # sumatorio
            estadisticas["movimientos_totales"] += 1
            
            negras, blancas = contar_fichas(tablero_juego)
            
            # Verificamos si alguien gano
            if negras == 0:
                print("Juego terminado")
                print(f"{asignacion[SIMBOLO_BLANCAS]} (B) ha ganado! Todas las fichas negras han sido eliminadas.\n")
                break
            elif blancas == 0:
                print("\n¡Juego terminado!")
                print(f"¡{asignacion[SIMBOLO_NEGRAS]} (N) ha ganado! Todas las fichas blancas han sido eliminadas.\n")
                break
            
            # Determinamos el turno del oponente
            if turno_actual == SIMBOLO_NEGRAS:
                turno_oponente = SIMBOLO_BLANCAS
            else:
                turno_oponente = SIMBOLO_NEGRAS

            # Verificamos si el oponente puede moverse
            if not puede_mover(tablero_juego, turno_oponente):
                print("\n¡Juego terminado!")
                print(f"{asignacion[turno_actual]} ({turno_actual}) ha ganado. El oponente no puede realizar movimientos.\n")
                break

            turno_actual = SIMBOLO_BLANCAS if turno_actual == SIMBOLO_NEGRAS else SIMBOLO_NEGRAS
            estadisticas["turnos"] += 1
    
    # Estadisticas finales
    print(" ----------Estadísticas Finales---------- ")
    print(f"Total de turnos jugados: {estadisticas['turnos']}")
    print(f"Fichas comidas por negras (n): {estadisticas['comidas_n']}")
    print(f"Fichas comidas por blancas (b): {estadisticas['comidas_b']}")
    print(f"Movimientos totales realizados: {estadisticas['movimientos_totales']}")
    print("\nGracias por jugar. Esperamos que te hayas divertido")

if __name__ == '__main__':
    damas()