board = []#El tablero 
 
for i in range(8):#Determina la cantidad de filas
    row = [EMPTY for EMPTY in range(8)]#Especifica la cantidad de celdas por fila
    board.append(row)

#Colocaremos las torres
board[0][0] = 'DARK_ROOK'
board[0][7] = 'DARK_ROOK'
board[7][0] = 'WHITE_ROOK'
board[7][7] = 'WHITE_ROOK'

#Colocaremos los caballos
board[0][1] = 'DARK_HORSE'
board[0][6] = 'DARK_HORSE'
board[7][1] = 'WHITE_HORSE'
board[7][6] = 'WHITE_HORSE'

#Colocaremos los alfines
board[0][2] = 'DARK_ALFIN'
board[0][5] = 'DARK_ALFIN'
board[7][2] = 'WHITE_ALFIN'
board[7][5] = 'WHITE_ALFIN'

#Colocaremos la reina
board[0][3] = 'DARK_QUEEN'
board[7][3] = 'WHITE_QUEEN'

#Colocaremos el rey
board[0][4] = 'DARK_KING'
board[7][4] = 'WHITE_KING'

#Colocaremos los peones
for i in range(8):
    board[1][i] = 'DARK_PAWN'
for i in range(8):
    board[6][i] = 'WHITE_PAWN'

for i in range(8):
    for j in range(8):
        print(board[i][j],end=' ')
    print('\n')

