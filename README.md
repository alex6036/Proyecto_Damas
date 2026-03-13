# Proyecto_Damas

## Descripción

Este es un juego de damas (checkers) implementado en Python que se ejecuta en la línea de comandos. El juego permite a dos jugadores competir en un tablero de 8x8, con reglas tradicionales de damas incluyendo movimientos diagonales, capturas obligatorias y promoción a reina.

## Características

- **Interfaz de línea de comandos**: Juego completamente basado en terminal con un tablero visual atractivo.
- **Dos jugadores**: Modo local para dos jugadores humanos.
- **Reglas completas**: Incluye movimientos básicos, capturas, promoción a reina y capturas múltiples.
- **Estadísticas del juego**: Seguimiento de turnos, fichas comidas y movimientos totales.
- **Comandos especiales**: Permite cambiar nombre de jugador y carácter de las fichas durante el juego.
- **Validación de movimientos**: Verifica movimientos válidos y previene jugadas ilegales.
- **Fin del juego automático**: Detecta cuando un jugador gana por eliminación de fichas o falta de movimientos.

## Requisitos

- Python 3.x instalado en el sistema.
- No se requieren bibliotecas externas adicionales (solo usa la biblioteca estándar `random`).

## Instalación

1. Clona o descarga este repositorio.
2. Asegúrate de tener Python instalado.
3. Ejecuta el archivo `proyecto_final.py`.

## Cómo jugar

1. **Ejecutar el juego**:
   ```bash
   python proyecto_final.py
   ```

2. **Ingreso de nombres**:
   - Cada jugador debe ingresar un nombre de 6-12 caracteres alfanuméricos.

3. **Asignación de turnos**:
   - El orden de juego se sortea aleatoriamente.
   - Un jugador juega con fichas negras ('n'), el otro con blancas ('b').

4. **Movimientos**:
   - Ingresa la posición de origen (ej. `3A`) y destino (ej. `4B`).
   - Las coordenadas usan números para filas (1-8) y letras para columnas (A-H).

5. **Reglas básicas**:
   - Las fichas se mueven diagonalmente una casilla.
   - Las capturas se hacen saltando sobre fichas enemigas.
   - Las capturas son obligatorias cuando están disponibles.
   - Al llegar al extremo opuesto, una ficha se convierte en reina.
   - Las reinas pueden moverse múltiples casillas en diagonal.

## Comandos especiales

Durante el juego, puedes usar estos comandos en lugar de coordenadas:

- `!end`: Termina el juego inmediatamente.
- `!cn` o `!changename`: Cambia el nombre del jugador actual (máximo 2 cambios por jugador).
- `!cc` o `!changechar`: Cambia el carácter usado para las fichas del jugador actual (máximo 2 cambios por jugador).

## Ejemplo de partida

```
   A   B   C   D   E   F   G   H
  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗
1 ║   ║ n ║   ║ n ║   ║ n ║   ║ n ║
  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
2 ║ n ║   ║ n ║   ║ n ║   ║ n ║   ║
  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
3 ║   ║ n ║   ║ n ║   ║ n ║   ║ n ║
  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
4 ║ . ║   ║ . ║   ║ . ║   ║ . ║   ║
  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
5 ║   ║ . ║   ║ . ║   ║ . ║   ║ . ║
  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
6 ║ b ║   ║ b ║   ║ b ║   ║ b ║   ║
  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
7 ║   ║ b ║   ║ b ║   ║ b ║   ║ b ║
  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
8 ║ b ║   ║ b ║   ║ b ║   ║ b ║   ║
  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝

Turno de: Jugador1 (n)
Estadísticas actuales: Turnos: 0, Fichas comidas: n=0, b=0
Ingrese la posición de origen (ej. 3A) o un comando (!end, !cn, !cc): 6C
Ingrese la posición de destino (ej. 4B): 5B
```

## Contribuciones

Si deseas contribuir al proyecto, puedes:

- Reportar bugs o sugerir mejoras.
- Enviar pull requests con nuevas características.
- Mejorar la documentación o el código.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

---

¡Disfruta jugando damas!