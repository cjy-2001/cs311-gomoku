import sys, unittest

import project


class Tests(unittest.TestCase):
    # def test_is_terminal(self):
    #     BOARD_SIZE = 9
    #     INITIAL_BOARD = {}

    #     for row in range(0, BOARD_SIZE):
    #         for col in range(0, BOARD_SIZE):
    #             INITIAL_BOARD[(row, col)] = 0

    #     # Test 5-in-a-column
    #     INITIAL_BOARD[1, 3] = 2
    #     INITIAL_BOARD[2, 3] = 1
    #     INITIAL_BOARD[3, 3] = 1
    #     INITIAL_BOARD[4, 3] = 1
    #     INITIAL_BOARD[5, 3] = 1
    #     INITIAL_BOARD[6, 3] = 1

    #     gomoku = project.Gomoku(state=INITIAL_BOARD)
    #     self.assertEqual(gomoku.is_terminal(), True)

    #     # Test 5-in-a-row
    #     INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 0)
    #     INITIAL_BOARD[7, 0] = 1
    #     INITIAL_BOARD[7, 1] = 2
    #     INITIAL_BOARD[7, 2] = 2
    #     INITIAL_BOARD[7, 3] = 2
    #     INITIAL_BOARD[7, 4] = 2
    #     INITIAL_BOARD[7, 5] = 2
    #     gomoku = project.Gomoku(state=INITIAL_BOARD)
    #     self.assertEqual(gomoku.is_terminal(), True)
        

    #     # Test five-in-a-diagonal (top left - bottom right)
    #     INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 0)
    #     INITIAL_BOARD[1, 2] = 1
    #     INITIAL_BOARD[2, 3] = 2
    #     INITIAL_BOARD[3, 4] = 2
    #     INITIAL_BOARD[4, 5] = 2
    #     INITIAL_BOARD[5, 6] = 2
    #     INITIAL_BOARD[6, 7] = 2
    #     gomoku = project.Gomoku(state=INITIAL_BOARD)
    #     self.assertEqual(gomoku.is_terminal(), True)

        
    #     # Test five-in-a-diagonal (top right - bottom left)
    #     INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 0)
    #     INITIAL_BOARD[7, 4] = 1
    #     INITIAL_BOARD[6, 5] = 1
    #     INITIAL_BOARD[5, 6] = 1
    #     INITIAL_BOARD[4, 7] = 1
    #     INITIAL_BOARD[3, 8] = 1

    #     gomoku = project.Gomoku(state=INITIAL_BOARD)
    #     self.assertEqual(gomoku.is_terminal(), True)



    #     INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 0)
    #     INITIAL_BOARD[0, 8] = 2
    #     INITIAL_BOARD[1, 7] = 2 
    #     INITIAL_BOARD[2, 6] = 2
    #     INITIAL_BOARD[3, 5] = 2
    #     INITIAL_BOARD[4, 4] = 2

    #     gomoku = project.Gomoku(state=INITIAL_BOARD)
    #     self.assertEqual(gomoku.is_terminal(), True)

    #     # Test draws

    #     INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 2)

    #     for i in range(BOARD_SIZE):
    #         if i%2 ==0:
    #             for j in range(4):
    #                 INITIAL_BOARD[(i, j)] = 1
    #                 INITIAL_BOARD[(i, 8)] = 1
            
    #         else:
    #             for j in range(4,9):
        
    #                 INITIAL_BOARD[(i, j)] = 1
    #                 INITIAL_BOARD[(i, 8)] = 2
        
    #     #print(INITIAL_BOARD)

    #     gomoku = project.Gomoku(state=INITIAL_BOARD)
    #     self.assertEqual(gomoku.gameStatus, "game_on")
    #     self.assertEqual(gomoku.is_terminal(), True)
    #     self.assertEqual(gomoku.gameStatus, 0)


    # def test_fours(self):
    #     BOARD_SIZE = 9
    #     INITIAL_BOARD = {}

    #     for row in range(0, BOARD_SIZE):
    #         for col in range(0, BOARD_SIZE):
    #             INITIAL_BOARD[(row, col)] = 0
            

    #     INITIAL_BOARD[2, 3] = 1
    #     INITIAL_BOARD[3, 3] = 1
    #     INITIAL_BOARD[4, 3] = 1
    #     INITIAL_BOARD[5, 3] = 1
    #     gomoku = project.Gomoku(state=INITIAL_BOARD)

    #     self.assertEqual(gomoku.get_threat_patterns(color=1, length=4), (1,0))

    #     INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 0)
    #     INITIAL_BOARD[4, 4] = 1
    #     INITIAL_BOARD[5, 5] = 2 
    #     INITIAL_BOARD[6, 6] = 2
    #     INITIAL_BOARD[7, 7] = 2
    #     INITIAL_BOARD[8, 8] = 2
    #     gomoku = project.Gomoku(state=INITIAL_BOARD)

    #     self.assertEqual(gomoku.get_threat_patterns(color=2, length=4), (0,0))

    # def test_threes(self):
    #     BOARD_SIZE = 9
    #     INITIAL_BOARD = {}

    #     for row in range(0, BOARD_SIZE):
    #         for col in range(0, BOARD_SIZE):
    #             INITIAL_BOARD[(row, col)] = 0
            

    #     INITIAL_BOARD[1, 2] = 1
    #     INITIAL_BOARD[1, 3] = 1
    #     INITIAL_BOARD[1, 4] = 1
    #     INITIAL_BOARD[1, 5] = 2

    #     INITIAL_BOARD[3, 4] = 1
    #     INITIAL_BOARD[4, 4] = 1
    #     INITIAL_BOARD[5, 4] = 1
    #     INITIAL_BOARD[6, 4] = 2
        
               

    #     gomoku = project.Gomoku(state=INITIAL_BOARD)

    #     self.assertEqual(gomoku.get_threat_patterns(color=1, length=3), (0,2))
    #     self.assertEqual(gomoku.get_threat_patterns(color=1, length=4), (0,0))


    # def test_twos(self):
    #     BOARD_SIZE = 9
    #     INITIAL_BOARD = {}

    #     for row in range(0, BOARD_SIZE):
    #         for col in range(0, BOARD_SIZE):
    #             INITIAL_BOARD[(row, col)] = 0
            

    #     INITIAL_BOARD[1, 2] = 1
    #     INITIAL_BOARD[1, 3] = 1
    #     INITIAL_BOARD[1, 4] = 1
    #     INITIAL_BOARD[1, 5] = 2
    #     # INITIAL_BOARD[3, 4] = 1
    #     # INITIAL_BOARD[4, 4] = 1
    #     # INITIAL_BOARD[5, 4] = 1
    #     # INITIAL_BOARD[6, 4] = 2
        
               

    #     gomoku = project.Gomoku(state=INITIAL_BOARD)

    #     self.assertEqual(gomoku.get_threat_patterns(color=1, length=2), (0,0))


    # def test_multiple_shapes(self):
    #     BOARD_SIZE = 9
    #     INITIAL_BOARD = {}

    #     for row in range(0, BOARD_SIZE):
    #         for col in range(0, BOARD_SIZE):
    #             INITIAL_BOARD[(row, col)] = 0
            
    #     INITIAL_BOARD[1, 4] = 1

    #     INITIAL_BOARD[2, 3] = 1
    #     INITIAL_BOARD[2, 4] = 2
    #     INITIAL_BOARD[2, 5] = 2
    #     INITIAL_BOARD[2, 6] = 2
    #     INITIAL_BOARD[2, 7] = 2
    #     INITIAL_BOARD[2, 8] = 2

    #     INITIAL_BOARD[3, 2] = 1
    #     INITIAL_BOARD[3, 4] = 1
    #     INITIAL_BOARD[3, 5] = 1
    #     INITIAL_BOARD[3, 6] = 2

    #     INITIAL_BOARD[4, 1] = 2
    #     INITIAL_BOARD[4, 4] = 1
    #     INITIAL_BOARD[4, 7] = 1

    #     INITIAL_BOARD[5, 4] = 1
    #     INITIAL_BOARD[5, 5] = 1
    #     INITIAL_BOARD[5, 6] = 1

    #     INITIAL_BOARD[6, 3] = 2
    #     INITIAL_BOARD[6, 4] = 1
    #     INITIAL_BOARD[6, 6] = 2

    #     INITIAL_BOARD[7, 1] = 1
    #     INITIAL_BOARD[7, 2] = 1
    #     INITIAL_BOARD[7, 3] = 1

        

    #     gomoku = project.Gomoku(state=INITIAL_BOARD)

    #     [black_open_two, black_half_two] = gomoku.get_threat_patterns(color=1, length=2)
    #     self.assertEqual([black_open_two, black_half_two], [2,3])

    #     [black_open_three, black_half_three] = gomoku.get_threat_patterns(color=1, length=3)
    #     self.assertEqual([black_open_three, black_half_three], [3,1])

    #     [black_open_four, black_half_four] = gomoku.get_threat_patterns(color=1, length=4)
    #     self.assertEqual([black_open_four, black_half_four], [0,1])

    #     [black_open_five, black_half_five] = gomoku.get_threat_patterns(color=1, length=5)
    #     black_five = black_open_five + black_half_five
    #     self.assertEqual(black_five, 0)

    #     [white_open_two, white_half_two] = gomoku.get_threat_patterns(color=2, length=2)
    #     self.assertEqual([white_open_two, white_half_two], [2,0])

    #     [white_open_three, white_half_three] = gomoku.get_threat_patterns(color=2, length=3)
    #     self.assertEqual([white_open_three, white_half_three], [0,0])

    #     [white_open_four, white_half_four] = gomoku.get_threat_patterns(color=2, length=4)
    #     self.assertEqual([white_open_four, white_half_four], [0,0])

    #     [white_open_five, white_half_five] = gomoku.get_threat_patterns(color=2, length=5)
    #     white_five = white_open_five + white_half_five
    #     self.assertEqual(white_five, 1)
        
    # def test_multiple_shapes2(self):
    #     BOARD_SIZE = 9
    #     INITIAL_BOARD = {}

    #     for row in range(0, BOARD_SIZE):
    #         for col in range(0, BOARD_SIZE):
    #             INITIAL_BOARD[(row, col)] = 0

    #     INITIAL_BOARD[0, 0] = 2
    #     INITIAL_BOARD[1, 0] = 2
    #     INITIAL_BOARD[2, 0] = 2

    #     INITIAL_BOARD[0, 1] = 1
    #     INITIAL_BOARD[0, 2] = 1

    #     INITIAL_BOARD[1, 1] = 1
    #     INITIAL_BOARD[1, 2] = 1
    #     INITIAL_BOARD[1, 3] = 1

    #     INITIAL_BOARD[2, 1] = 1
    #     INITIAL_BOARD[2, 2] = 1
    #     INITIAL_BOARD[2, 3] = 1
    #     INITIAL_BOARD[2, 4] = 1

    #     # Half diag

    #     INITIAL_BOARD[3, 3] = 2
    #     INITIAL_BOARD[4, 4] = 1
    #     INITIAL_BOARD[5, 5] = 1
    #     INITIAL_BOARD[6, 6] = 1
    #     INITIAL_BOARD[7, 7] = 1


    #     INITIAL_BOARD[3, 6] = 2
    #     INITIAL_BOARD[4, 5] = 1
    #     INITIAL_BOARD[5, 4] = 1
    #     INITIAL_BOARD[6, 3] = 1

    #     INITIAL_BOARD[1, 5] = 1
    #     INITIAL_BOARD[6, 5] = 1
    #     INITIAL_BOARD[6, 4] = 1
    #     INITIAL_BOARD[5, 3] = 1

    #     INITIAL_BOARD[7, 4] = 1

    #     INITIAL_BOARD[1, 7] = 1


    #     INITIAL_BOARD[7, 6] = 1
    #     INITIAL_BOARD[3, 1] = 1
    #     INITIAL_BOARD[7, 3] = 1
    #     INITIAL_BOARD[4, 6] = 1

    #     INITIAL_BOARD[5, 1] = 2
    #     INITIAL_BOARD[6, 1] = 2
    #     INITIAL_BOARD[7, 1] = 2

    #     INITIAL_BOARD[1, 7] = 2
    #     INITIAL_BOARD[0, 7] = 2

    #     INITIAL_BOARD[0, 8] = 2
    #     INITIAL_BOARD[1, 8] = 2
    #     INITIAL_BOARD[2, 8] = 2
    #     INITIAL_BOARD[3, 8] = 2

    #     INITIAL_BOARD[6, 8] = 2
    #     INITIAL_BOARD[5, 8] = 2

    #     gomoku = project.Gomoku(state=INITIAL_BOARD)

    #     [black_open_two, black_half_two] = gomoku.get_threat_patterns(color=1, length=2)
    #     self.assertEqual([black_open_two, black_half_two], [8,3])

    #     [black_open_three, black_half_three] = gomoku.get_threat_patterns(color=1, length=3)
    #     self.assertEqual([black_open_three, black_half_three], [6,5])

    #     [black_open_four, black_half_four] = gomoku.get_threat_patterns(color=1, length=4)
    #     self.assertEqual([black_open_four, black_half_four], [3,3])

    #     [black_open_five, black_half_five] = gomoku.get_threat_patterns(color=1, length=5)
    #     black_five = black_open_five + black_half_five
    #     self.assertEqual(black_five, 0)



    #     [white_open_two, white_half_two] = gomoku.get_threat_patterns(color=2, length=2)
    #     self.assertEqual([white_open_two, white_half_two], [1,5])

    #     [white_open_three, white_half_three] = gomoku.get_threat_patterns(color=2, length=3)
    #     self.assertEqual([white_open_three, white_half_three], [1,1])

    #     [white_open_four, white_half_four] = gomoku.get_threat_patterns(color=2, length=4)
    #     self.assertEqual([white_open_four, white_half_four], [0,1])

    #     [white_open_five, white_half_five] = gomoku.get_threat_patterns(color=2, length=5)
    #     white_five = white_open_five + white_half_five
    #     self.assertEqual(white_five, 0)

    # def test_possible_moves(self):
    #     BOARD_SIZE = 9
    #     INITIAL_BOARD = {}

    #     for row in range(0, BOARD_SIZE):
    #         for col in range(0, BOARD_SIZE):
    #             INITIAL_BOARD[(row, col)] = 0
            

    #     INITIAL_BOARD[2, 3] = 1
    #     INITIAL_BOARD[3, 3] = 1
    #     INITIAL_BOARD[4, 3] = 1
    #     INITIAL_BOARD[5, 3] = 1

    #     gomoku = project.Gomoku(state=INITIAL_BOARD)

    #     self.assertEqual(len(gomoku.get_possible_moves()), 14)

    
    def test_minimax(self):
        BOARD_SIZE = 9
        INITIAL_BOARD = {}

        for row in range(0, BOARD_SIZE):
            for col in range(0, BOARD_SIZE):
                INITIAL_BOARD[(row, col)] = 0
            

        INITIAL_BOARD[1, 2] = 1
        INITIAL_BOARD[1, 3] = 1
        INITIAL_BOARD[1, 4] = 1
        INITIAL_BOARD[1, 5] = 1
        INITIAL_BOARD[0, 2] = 2
        INITIAL_BOARD[0, 4] = 2
        INITIAL_BOARD[2, 2] = 2
        INITIAL_BOARD[2, 4] = 2

        gomoku = project.Gomoku(state=INITIAL_BOARD)
        # print(gomoku.get_threat_patterns(1, 5))
        # print(gomoku.get_threat_patterns(1, 4))
        # print(gomoku.get_threat_patterns(1, 3))
        # print(gomoku.get_threat_patterns(1, 2))
        # print(gomoku.get_threat_patterns(2, 5))
        # print(gomoku.get_threat_patterns(2, 4))
        # print(gomoku.get_threat_patterns(2, 3))
        # print(gomoku.get_threat_patterns(2, 2))

        print(gomoku.minimax(maximizing=True))

        INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 0)
        INITIAL_BOARD[4, 4] = 0
        INITIAL_BOARD[3, 3] = 1
        gomoku = project.Gomoku(state=INITIAL_BOARD)
        print(gomoku.minimax(maximizing=True))

        # INITIAL_BOARD = dict.fromkeys(INITIAL_BOARD, 0)
        # INITIAL_BOARD[4, 4] = 0
        # gomoku = project.Gomoku(state=INITIAL_BOARD)
        # print(gomoku.minimax(maximizing=False))

        # self.assertEqual(gomoku.get_threat_patterns(color=1, length=2), (0,0))


if __name__ == '__main__':
    unittest.main(argv=sys.argv[:1])
