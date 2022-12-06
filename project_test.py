import sys, unittest

import project

class Tests(unittest.TestCase):
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

        self.assertEqual(project.get_threat_patterns(INITIAL_BOARD), [1,0])
    
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


    # def test_expand_count(self):
    #     # Expected expansions for 'blank' at corresponding index
    #     for idx, exps in enumerate([2, 3, 2, 3, 4, 3, 2, 3, 2]):
    #         board = list(range(1,9))
    #         board.insert(idx, 0)
            
    #         node = project.Node(board)
    #         self.assertEqual(len(node.expand()), exps, f"'Blank' at index {idx} should have {exps} expansions")

    # def test_expanded_down_right(self):
    #     root_node = project.Node([0,1,2,3,4,5,6,7,8])
    #     self.assertIsNone(root_node.parent)
    #     self.assertEqual(root_node.cost, 0)


if __name__ == '__main__':
    unittest.main(argv=sys.argv[:1])
