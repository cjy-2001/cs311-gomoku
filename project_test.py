import sys, unittest

import project

class Tests(unittest.TestCase):
    def test_is_terminal(self):
        BOARD_SIZE = 9
        INITIAL_BOARD = {}

        for row in range(0, BOARD_SIZE):
            for col in range(0, BOARD_SIZE):
                INITIAL_BOARD[(row, col)] = 0

        # Test 5-in-a-column
        INITIAL_BOARD[1, 3] = 2
        INITIAL_BOARD[2, 3] = 1
        INITIAL_BOARD[3, 3] = 1
        INITIAL_BOARD[4, 3] = 1
        INITIAL_BOARD[5, 3] = 1
        INITIAL_BOARD[6, 3] = 1

        gomoku = project.Gomoku(state=INITIAL_BOARD)
        self.assertEqual(gomoku.is_terminal(), True)

        # Test 5-in-a-row
        INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 0)
        INITIAL_BOARD[7, 0] = 1
        INITIAL_BOARD[7, 1] = 2
        INITIAL_BOARD[7, 2] = 2
        INITIAL_BOARD[7, 3] = 2
        INITIAL_BOARD[7, 4] = 2
        INITIAL_BOARD[7, 5] = 2
        gomoku = project.Gomoku(state=INITIAL_BOARD)
        self.assertEqual(gomoku.is_terminal(), True)
        

        # Test five-in-a-diagonal (top left - bottom right)
        INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 0)
        INITIAL_BOARD[1, 2] = 1
        INITIAL_BOARD[2, 3] = 2
        INITIAL_BOARD[3, 4] = 2
        INITIAL_BOARD[4, 5] = 2
        INITIAL_BOARD[5, 6] = 2
        INITIAL_BOARD[6, 7] = 2
        gomoku = project.Gomoku(state=INITIAL_BOARD)
        self.assertEqual(gomoku.is_terminal(), True)

        
        # Test five-in-a-diagonal (top right - bottom left)
        INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 0)
        INITIAL_BOARD[7, 4] = 1
        INITIAL_BOARD[6, 5] = 1
        INITIAL_BOARD[5, 6] = 1
        INITIAL_BOARD[4, 7] = 1
        INITIAL_BOARD[3, 8] = 1

        gomoku = project.Gomoku(state=INITIAL_BOARD)
        self.assertEqual(gomoku.is_terminal(), True)



        INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 0)
        INITIAL_BOARD[0, 8] = 2
        INITIAL_BOARD[1, 7] = 2 
        INITIAL_BOARD[2, 6] = 2
        INITIAL_BOARD[3, 5] = 2
        INITIAL_BOARD[4, 4] = 2

        gomoku = project.Gomoku(state=INITIAL_BOARD)
        self.assertEqual(gomoku.is_terminal(), True)

        # Test draws

        INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 1)
        for i in range(0, BOARD_SIZE):
            for j in range(0, BOARD_SIZE):
                if i%2 == 0:
                    if j%2 == 0:
                        INITIAL_BOARD[(i,j)] == 2
                else:
                    if j%2 == 1:
                        INITIAL_BOARD[(i,j)]==2

        gomoku = project.Gomoku(state=INITIAL_BOARD)
        self.assertEqual(gomoku.gameStatus, "game_on")
        self.assertEqual(gomoku.is_terminal(), True)
        self.assertEqual(gomoku.gameStatus, 1)


    def test_fours(self):
        BOARD_SIZE = 9
        INITIAL_BOARD = {}

        for row in range(0, BOARD_SIZE):
            for col in range(0, BOARD_SIZE):
                INITIAL_BOARD[(row, col)] = 0
            

        INITIAL_BOARD[2, 3] = 1
        INITIAL_BOARD[3, 3] = 1
        INITIAL_BOARD[4, 3] = 1
        INITIAL_BOARD[5, 3] = 1

        gomoku = project.Gomoku(state=INITIAL_BOARD)

        self.assertEqual(gomoku.get_threat_patterns(color=1, length=4), (1,0))


    def test_threes(self):
        BOARD_SIZE = 9
        INITIAL_BOARD = {}

        for row in range(0, BOARD_SIZE):
            for col in range(0, BOARD_SIZE):
                INITIAL_BOARD[(row, col)] = 0
            

        INITIAL_BOARD[1, 2] = 1
        INITIAL_BOARD[1, 3] = 1
        INITIAL_BOARD[1, 4] = 1
        INITIAL_BOARD[1, 5] = 2

        INITIAL_BOARD[3, 4] = 1
        INITIAL_BOARD[4, 4] = 1
        INITIAL_BOARD[5, 4] = 1
        INITIAL_BOARD[6, 4] = 1        

        gomoku = project.Gomoku(state=INITIAL_BOARD)

        self.assertEqual(gomoku.get_threat_patterns(color=1, length=3), (0,1))
        self.assertEqual(gomoku.get_threat_patterns(color=1, length=4), (1,0))
    
    def test_possible_moves(self):
        BOARD_SIZE = 9
        INITIAL_BOARD = {}

        for row in range(0, BOARD_SIZE):
            for col in range(0, BOARD_SIZE):
                INITIAL_BOARD[(row, col)] = 0
            

        INITIAL_BOARD[2, 3] = 1
        INITIAL_BOARD[3, 3] = 1
        INITIAL_BOARD[4, 3] = 1
        INITIAL_BOARD[5, 3] = 1

        gomoku = project.Gomoku(state=INITIAL_BOARD)

        self.assertEqual(len(gomoku.get_possible_moves()), 14)


if __name__ == '__main__':
    unittest.main(argv=sys.argv[:1])
