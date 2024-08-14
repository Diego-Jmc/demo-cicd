# Tic-Tac-Toe en Python





def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check filas
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    # Check columnas
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    # Check diagonales
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    
    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        
        # Solicitar movimiento
        move = input(f"Jugador {current_player}, introduce tu movimiento (fila y columna): ")
        row, col = map(int, move.split())
        
        # Verificar si el movimiento es válido
        if board[row][col] != ' ':
            print("Movimiento inválido. Intenta de nuevo.")
            continue
        
        # Realizar movimiento
        board[row][col] = current_player
        
        # Verificar si hay un ganador
        if check_winner(board, current_player):
            print_board(board)
            print(f"¡Jugador {current_player} gana!")
            break
        
        # Verificar si el tablero está lleno
        if is_full(board):
            print_board(board)
            print("¡Empate!")
            break
        
        # Cambiar de jugador
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
