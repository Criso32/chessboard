def paint_chessboard(size):
    # Verifica si el tamaño del tablero es válido (par)
    if size % 2 != 0:
        print("El tamaño del tablero debe ser un número par.")
        return None

    # Inicializa el tablero como una matriz de tamaño size x size
    board = [['' for _ in range(size)] for _ in range(size)]

    # Pinta el tablero alternando entre rojo (R) y azul (B)
    for i in range(size):
        for j in range(size):
            # Determina el color de la celda según la paridad de la fila y la columna
            if (i + j) % 2 == 0:
                board[i][j] = 'R'
            else:
                board[i][j] = 'B'

    # Verifica si la solución es válida (cumple con las condiciones)
    for i in range(size):
        red_count = board[i].count('R')
        blue_count = board[i].count('B')
        if red_count == blue_count:
            return None

    for j in range(size):
        column = [board[i][j] for i in range(size)]
        red_count = column.count('R')
        blue_count = column.count('B')
        if red_count == blue_count:
            return None

    # Si la solución es válida, devuelve el tablero pintado
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

# Tablero de ajedrez estándar de 8x8
print("Tablero de ajedrez estándar de 8x8:")
chessboard_8x8 = paint_chessboard(8)
if chessboard_8x8:
    print_board(chessboard_8x8)
else:
    print("No se puede pintar el tablero según las pautas dadas.")

# Tablero monumental de 1000x1000
print("\nTablero monumental de 1000x1000:")
chessboard_1000x1000 = paint_chessboard(1000)
if chessboard_1000x1000:
    print("El tablero monumental se puede pintar de acuerdo con las pautas dadas.")
else:
    print("No se puede pintar el tablero monumental según las pautas dadas.")
