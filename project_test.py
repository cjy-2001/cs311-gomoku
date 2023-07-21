import sys, unittest
from project import Gomoku

def draw_board(dic, size):
    """
    Helper function to draw the current board (debug purpose).
    """
    
    lst = list(dic.values())
    for i in range(len(lst)):
        if (i+1)% size ==0:
            print(lst[i])
        else:
            print(lst[i], end = " ")


class GomokuTest(unittest.TestCase):
    def setUp(self):
        self.BOARD_SIZE = 9
        self.board = {(i, j): 0 for i in range(self.BOARD_SIZE) for j in range(self.BOARD_SIZE)}
        self.gomoku = Gomoku(state=self.board)


    def test_is_terminal(self):
        # Testing 5-in-a-column
        self.board[1, 3] = 2
        self.board[2, 3] = 1
        self.board[3, 3] = 1
        self.board[4, 3] = 1
        self.board[5, 3] = 1
        self.board[6, 3] = 1
        self.gomoku = Gomoku(state=self.board)
        self.assertEqual(self.gomoku.is_terminal(), 1)

        # Testing 5-in-a-row
        self.setUp()

        self.board[7, 0] = 1
        self.board[7, 1] = 2
        self.board[7, 2] = 2
        self.board[7, 3] = 2
        self.board[7, 4] = 2
        self.board[7, 5] = 2
        self.gomoku = Gomoku(state=self.board)
        self.assertEqual(self.gomoku.is_terminal(), 2)

        # Testing five-in-a-diagonal (top left - bottom right)
        self.setUp()

        self.board[1, 2] = 1
        self.board[2, 3] = 2
        self.board[3, 4] = 2
        self.board[4, 5] = 2
        self.board[5, 6] = 2
        self.board[6, 7] = 2
        self.gomoku = Gomoku(state=self.board)
        self.assertEqual(self.gomoku.is_terminal(), 2)

        # Testing five-in-a-diagonal (top right - bottom left)
        self.setUp()

        self.board[7, 4] = 1
        self.board[6, 5] = 1
        self.board[5, 6] = 1
        self.board[4, 7] = 1
        self.board[3, 8] = 1
        self.gomoku = Gomoku(state=self.board)
        self.assertEqual(self.gomoku.is_terminal(), 1)

        # Testing five-in-a-diagonal (top right - bottom left)
        self.setUp()

        self.board[0, 8] = 2
        self.board[1, 7] = 2 
        self.board[2, 6] = 2
        self.board[3, 5] = 2
        self.board[4, 4] = 2
        self.gomoku = Gomoku(state=self.board)
        self.assertEqual(self.gomoku.is_terminal(), 2)

        # Testing draws
        self.setUp()

        self.board = dict.fromkeys(self.board, 2)
        for i in range(self.BOARD_SIZE):
            if i%2 ==0:
                for j in range(4):
                    self.board[(i, j)] = 1
                    self.board[(i, 8)] = 1
            
            else:
                for j in range(4,9):
        
                    self.board[(i, j)] = 1
                    self.board[(i, 8)] = 2
        self.gomoku = Gomoku(state=self.board)
        self.assertEqual(self.gomoku.is_terminal(), 3)


    def test_threat_patterns_length_4(self):
        """
        Test the get_threat_patterns method to check the number of open and half-open sequences of length 4.
        """
        # Test open four for black
        for i in range(1, 5):
            self.board[i, 3] = 1
        self.gomoku = Gomoku(state=self.board)
        open_four, half_open_four = self.gomoku.get_threat_patterns(1, 4)

        self.assertEqual(open_four, 1, "Failed on open four test for black")
        self.assertEqual(half_open_four, 0, "Failed on half-open four test for black")

        self.setUp()

        # Test half-open four for white
        for i in range(1, 5):
            self.board[i, 3] = 2
        self.board[0, 3] = 1
        self.gomoku = Gomoku(state=self.board)
        open_four, half_open_four = self.gomoku.get_threat_patterns(2, 4)

        self.assertEqual(open_four, 0, "Failed on open four test for white")
        self.assertEqual(half_open_four, 1, "Failed on half-open four test for white")


    def test_threat_patterns_length_3(self):
        """
        Test the get_threat_patterns method to check the number of open and half-open sequences of length 3.
        """

        # Test open three for black
        for i in range(2, 5):
            self.board[i, 3] = 1
        self.gomoku = Gomoku(state=self.board)
        open_three, half_open_three = self.gomoku.get_threat_patterns(1, 3)
        
        self.assertEqual(open_three, 1, "Failed on open three test for black")
        self.assertEqual(half_open_three, 0, "Failed on half-open three test for black")

        self.setUp()

        # Test half-open three for white
        for i in range(2, 5):
            self.board[i, 3] = 2
        self.board[1, 3] = 1
        self.gomoku = Gomoku(state=self.board)
        open_three, half_open_three = self.gomoku.get_threat_patterns(2, 3)

        self.assertEqual(open_three, 0, "Failed on open three test for white")
        self.assertEqual(half_open_three, 1, "Failed on half-open three test for white")


    def test_threat_patterns_length_2(self):
        """
        Test the get_threat_patterns method to check the number of open and half-open sequences of length 2.
        """
        # Test open two for black
        for i in range(3, 5):
            self.board[i, 3] = 1
        self.gomoku = Gomoku(state=self.board)
        open_two, half_open_two = self.gomoku.get_threat_patterns(1, 2)

        self.assertEqual(open_two, 1, "Failed on open two test for black")
        self.assertEqual(half_open_two, 0, "Failed on half-open two test for black")

        self.setUp()

        # Test half-open two for white
        for i in range(3, 5):
            self.board[i, 3] = 2
        self.board[2, 3] = 1
        self.gomoku = Gomoku(state=self.board)
        open_two, half_open_two = self.gomoku.get_threat_patterns(2, 2)

        self.assertEqual(open_two, 0, "Failed on open two test for white")
        self.assertEqual(half_open_two, 1, "Failed on half-open two test for white")


    def check_threat_patterns(self, color, length, expected_open, expected_half):
        """
        Helper method to test the get_threat_patterns method.
        """

        open_count, half_open_count = self.gomoku.get_threat_patterns(color, length)

        self.assertEqual(open_count, expected_open, f"Failed on open {length}s test for color {color}")
        self.assertEqual(half_open_count, expected_half, f"Failed on half-open {length}s test for color {color}")

    def test_multiple_shapes_easy(self):
        """
        Test the get_threat_patterns method with multiple shapes on the board.
        """
        # Define the initial board state
        for i in range(3, 5):
            self.board[1, i] = 2
        for i in range(5):
            self.board[2, i] = [2, 1, 1, 1, 2][i]
        for i in range(2, 4):
            self.board[3, i] = [1, 2][i-2]
        for i in range(2, 4):
            self.board[4, i] = 1
        self.gomoku = Gomoku(state=self.board)

        # Test open and half-open twos for black
        self.check_threat_patterns(color=1, length=2, expected_open=1, expected_half=1)

        # Test open and half-open threes for black
        self.check_threat_patterns(color=1, length=3, expected_open=2, expected_half=0)

        # Test open and half-open fours for black
        self.check_threat_patterns(color=1, length=4, expected_open=0, expected_half=0)

        # Test fives for black
        self.check_threat_patterns(color=1, length=5, expected_open=0, expected_half=0)

        # Test open and half-open twos for white
        self.check_threat_patterns(color=2, length=2, expected_open=3, expected_half=1)

        # Test open and half-open threes for white
        self.check_threat_patterns(color=2, length=3, expected_open=0, expected_half=0)

        # Test open and half-open fours for white
        self.check_threat_patterns(color=2, length=4, expected_open=0, expected_half=0)

        # Test fives for white
        self.check_threat_patterns(color=2, length=5, expected_open=0, expected_half=0)


    def test_multiple_shapes_intermediate(self):
        """
        Test the get_threat_patterns method with multiple shapes on the board.
        """

        # Define the initial board state
        self.board[1, 4] = 1

        self.board[2, 3] = 1
        self.board[2, 4] = 2
        self.board[2, 5] = 2
        self.board[2, 6] = 2
        self.board[2, 7] = 2
        self.board[2, 8] = 2

        self.board[3, 2] = 1
        self.board[3, 4] = 1
        self.board[3, 5] = 1
        self.board[3, 6] = 2

        self.board[4, 1] = 2
        self.board[4, 4] = 1
        self.board[4, 7] = 1

        self.board[5, 4] = 1
        self.board[5, 5] = 1
        self.board[5, 6] = 1

        self.board[6, 3] = 2
        self.board[6, 4] = 1
        self.board[6, 6] = 2

        self.board[7, 1] = 1
        self.board[7, 2] = 1
        self.board[7, 3] = 1
        self.gomoku = Gomoku(state=self.board)

        # Test open and half-open twos for black
        self.check_threat_patterns(color=1, length=2, expected_open=2, expected_half=3)

        # Test open and half-open threes for black
        self.check_threat_patterns(color=1, length=3, expected_open=3, expected_half=1)

        # Test open and half-open fours for black
        self.check_threat_patterns(color=1, length=4, expected_open=0, expected_half=1)

        # Test fives for black
        self.check_threat_patterns(color=1, length=5, expected_open=0, expected_half=0)

        # Test open and half-open twos for white
        self.check_threat_patterns(color=2, length=2, expected_open=2, expected_half=0)

        # Test open and half-open threes for white
        self.check_threat_patterns(color=2, length=3, expected_open=0, expected_half=0)

        # Test open and half-open fours for white
        self.check_threat_patterns(color=2, length=4, expected_open=0, expected_half=0)

        # Test fives for white
        self.check_threat_patterns(color=2, length=5, expected_open=1, expected_half=0)

    def test_multiple_shapes_hard(self):
        """
        Test the get_threat_patterns method with multiple shapes on the board.
        """

        # Define the initial board state
        self.board[0, 0] = 2
        self.board[0, 1] = 1
        self.board[0, 2] = 1
        self.board[0, 7] = 2
        self.board[0, 8] = 2

        self.board[1, 0] = 2
        self.board[1, 1] = 1
        self.board[1, 2] = 1
        self.board[1, 3] = 1
        self.board[1, 5] = 1
        self.board[1, 7] = 2
        self.board[1, 8] = 2

        self.board[2, 0] = 2
        self.board[2, 1] = 1
        self.board[2, 2] = 1
        self.board[2, 3] = 1
        self.board[2, 4] = 1
        self.board[2, 8] = 2

        self.board[3, 1] = 1
        self.board[3, 3] = 2
        self.board[3, 6] = 2
        self.board[3, 8] = 2

        self.board[4, 4] = 1
        self.board[4, 5] = 1
        self.board[4, 6] = 1

        self.board[5, 1] = 2
        self.board[5, 3] = 1
        self.board[5, 4] = 1
        self.board[5, 5] = 1
        self.board[5, 8] = 2

        self.board[6, 1] = 2
        self.board[6, 3] = 1
        self.board[6, 4] = 1
        self.board[6, 5] = 1
        self.board[6, 6] = 1
        self.board[6, 8] = 2

        self.board[7, 1] = 2
        self.board[7, 3] = 1
        self.board[7, 4] = 1
        self.board[7, 6] = 1
        self.board[7, 7] = 1
        self.gomoku = Gomoku(state=self.board)

        # Test open and half-open twos for black
        self.check_threat_patterns(color=1, length=2, expected_open=8, expected_half=3)

        # Test open and half-open threes for black
        self.check_threat_patterns(color=1, length=3, expected_open=6, expected_half=5)

        # Test open and half-open fours for black
        self.check_threat_patterns(color=1, length=4, expected_open=3, expected_half=3)

        # Test fives for black
        self.check_threat_patterns(color=1, length=5, expected_open=0, expected_half=0)

        # Test open and half-open twos for white
        self.check_threat_patterns(color=2, length=2, expected_open=1, expected_half=5)

        # Test open and half-open threes for white
        self.check_threat_patterns(color=2, length=3, expected_open=1, expected_half=1)

        # Test open and half-open fours for white
        self.check_threat_patterns(color=2, length=4, expected_open=0, expected_half=1)

        # Test fives for white
        self.check_threat_patterns(color=2, length=5, expected_open=0, expected_half=0)


    def test_possible_moves(self):
        """
        Test the possible_moves method.
        """

        self.board[2, 3] = 1
        self.board[3, 3] = 1
        self.board[4, 3] = 1
        self.board[5, 3] = 1
        self.gomoku = Gomoku(state=self.board)

        self.assertEqual(len(self.gomoku.get_possible_moves()), 14, "Possible moves calculation failed")

    
    def test_minimax(self):
        """
        Test both old and new minimax methods.
        """

        # Easy Case with max depth = 1
        self.board[1, 2] = 1
        self.board[1, 3] = 1
        self.board[1, 4] = 1
        self.board[1, 5] = 1
        self.board[0, 2] = 2
        self.board[0, 4] = 2
        self.board[2, 2] = 2
        self.board[2, 4] = 2
        self.gomoku = Gomoku(state=self.board)

        # Compute the score using two methods
        score, _ = self.gomoku.minimax(maximizing=True, depth=1)
        score_new, _ = self.gomoku.new_minimax(maximizing=True, depth=1)

        self.assertEqual(score, score_new, "Easy case score calculation failed")

        #Intermediate Case with max depth = 2
        # self.setUp()

        # self.board[3, 4] = 1
        # self.board[4, 4] = 2
        # self.board[4, 5] = 1
        # self.board[4, 6] = 2
        # self.board[5, 4] = 1
        # self.board[5, 5] = 1
        # self.board[6, 4] = 2
        # self.board[6, 5] = 2
        # self.gomoku = Gomoku(state=self.board)

        # # Compute the score using two methods
        # score, _ = self.gomoku.minimax(maximizing=True, depth=2)
        # score_new, _ = self.gomoku.new_minimax(maximizing=True, depth=2)

        # self.assertEqual(score, score_new, "Intermediate case score calculation failed")

        #Hard Case with max depth = 3
        # self.setUp()

        # self.board[0, 8] = 2
        # self.board[1, 6] = 2
        # self.board[1, 7] = 1
        # self.board[2, 6] = 1
        # self.board[3, 4] = 2
        # self.board[3, 5] = 1
        # self.board[4, 4] = 1
        # self.board[4, 6] = 1
        # self.board[5, 3] = 2
        # self.board[5, 6] = 2

        # self.gomoku = Gomoku(state=self.board)

        # # Compute the score using two methods
        # score, _ = self.gomoku.minimax(maximizing=True, depth=3)
        # score_new, _ = self.gomoku.new_minimax(maximizing=True, depth=3)

        # self.assertEqual(score, score_new, "Hard case score calculation failed")


    def test_best_move(self):
        """
        Test the best_move method.
        """
        
        # Easy Case with max depth=1
        self.board[1, 2] = 1
        self.board[1, 3] = 1
        self.board[1, 4] = 1
        self.board[1, 5] = 1
        self.board[0, 2] = 2
        self.board[0, 4] = 2
        self.board[2, 2] = 2
        self.board[2, 4] = 2
        self.gomoku = Gomoku(state=self.board)
        move, _ = self.gomoku.best_move(depth=1)
        
        self.assertTrue(move in [(1, 1), (1, 6)], "Best move validation failed")

    
    def test_play(self):
        """
        Test the play method.
        """
            
        # Easy Case with max depth=1
        self.board[1, 2] = 1
        self.board[1, 3] = 1
        self.board[1, 4] = 1
        self.board[1, 5] = 1
        self.board[0, 2] = 2
        self.board[0, 4] = 2
        self.board[2, 2] = 2
        self.board[2, 4] = 2
        self.gomoku = Gomoku(state=self.board)

        # Intermediate Case with max depth=5
        # self.setUp()

        # self.board[3, 4] = 1
        # self.board[4, 4] = 2
        # self.board[4, 5] = 1
        # self.board[4, 6] = 2
        # self.board[5, 4] = 1
        # self.board[5, 5] = 1
        # self.board[6, 4] = 2
        # self.board[6, 5] = 2
        # self.gomoku = Gomoku(state=self.board)

        # Hard Case with max depth=7 or 9
        # self.setUp()

        # self.board[0, 8] = 2
        # self.board[1, 6] = 2
        # self.board[1, 7] = 1
        # self.board[2, 6] = 1
        # self.board[3, 4] = 2
        # self.board[3, 5] = 1
        # self.board[4, 4] = 1
        # self.board[4, 6] = 1
        # self.board[5, 3] = 2
        # self.board[5, 6] = 2
        # self.gomoku = Gomoku(state=self.board)

        minimax_wins = 0

        for _ in range(100):
            if self.gomoku.play(depth=1) == 1:
                minimax_wins += 1
        

        random_wins = 0
        for _ in range(100):
            if self.gomoku.play_randomly() == 1:
                random_wins += 1

        self.assertGreater(minimax_wins, random_wins, f"{minimax_wins} is not greater than {random_wins}")
        # print("Num of wins if black uses the algorithm:" + str(minimax_wins))
        # print("Num of wins if black plays randomly:" + str(random_wins))


if __name__ == '__main__':
    unittest.main(argv=sys.argv[:1])
