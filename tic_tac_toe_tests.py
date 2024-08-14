import unittest

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def suma(a, b):
    return a + b

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

class TestTicTacToe(unittest.TestCase):

    def test_check_winner_row(self):
        board = [
            ['X', 'X', 'X'],
            ['O', ' ', 'O'],
            [' ', ' ', ' ']
        ]
        self.assertTrue(check_winner(board, 'X'))

    def test_is_full(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertTrue(is_full(board))



class TestSumaFunction(unittest.TestCase):

    def test_suma_positivos(self):
        self.assertEqual(suma(3, 5), 10)
    




if __name__ == "__main__":
    unittest.main()
