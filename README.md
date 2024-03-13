# Para llegar a la conclusion definimos una funcion `paint_chessboard(size)` que toma como argumento el tamaño del tablero
# y genera una solucion valida teniendo en cuenta que no haya 2 filas o columnas con el mismo numero de celdas rojas.

# Creamos una matriz de tamaño `size x size` y asignamos los colores rojo (R) y azul (B) a las celdas del tablero alternadamente
# asegurando de que cada fila y columna tengan un numero diferente de celdas rojas.

# Verificamos si la solucion generada cumple con las condiciones. Si encuentra que 2 filas o columnas tienen el mismo numero de celdas
# rojas devuelve `None` para indicar que no se puede pintar el tablero segun las pautas dadas.

# Finalmente el codigo imprime el tablero pintado si la solucion es valida o, de lo contrario, indica que no se puede pintar
# el tablero segun las pautas dadas
