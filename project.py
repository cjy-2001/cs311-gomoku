"""
CS311 Final Project

Full Name(s): Jiayi Chen, Siyuan Niu

"""

import argparse, itertools, random
from heapq import heapify, heappush, heappop
from typing import Callable, List, Optional, Sequence, Tuple


# Problem constants. The goal is a "blank" (0) in bottom right corner
BOARD_SIZE = 9
INITIAL_BOARD = {}

for row in range(0, BOARD_SIZE):
    for col in range(0, BOARD_SIZE):
        INITIAL_BOARD[(row, col)] = 0
    

INITIAL_BOARD[2, 3] = 1
INITIAL_BOARD[3, 3] = 1
INITIAL_BOARD[4, 3] = 1
INITIAL_BOARD[5, 3] = 1

class Gomoku:
    def __init__(self, state: dict[(int, int): int], parent: "Gomoku" = None, score=0):
        """Create Node to track particular state and associated parent and cost

        Args:
            state (Sequence[int]): State for this node, typically a list, e.g. [0, 1, 2, 3, 4, 5, 6, 7, 8]
            parent (Node, optional): Parent node, None indicates the root node. Defaults to None.
            cost (int, optional): Cost in moves to reach this node. Defaults to 0.
        """
        self.state = state  # To facilitate "hashable" make state immutable
        self.parent = parent
        self.score = score
    

    def is_end(self) -> bool:
        """Return True if Node has goal state"""
        pass 
    
    def best_move(self) -> tuple:
        """Return the agent's next move"""
        pass 
    

    def get_possible_moves(self) -> List["Gomoku"]:
        """Find the neighbors of all filled cells as all possible moves next,
            Return the child Gomoku objects with as if each neighbor is filled
        """
        lst = []

        filled = [x for x in self.state if self.state[x] > 0]

        move_coordinates = set()
        
        
        for (row, col) in filled:
            neighbors = [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
                (row + 1, col - 1),
                (row - 1, col + 1),
                (row + 1, col + 1),
                (row - 1, col - 1)]
                
            for n in neighbors:
                if n[0] < 0 or n[1] < 0 or n[0] > BOARD_SIZE - 1 or n[1] > BOARD_SIZE - 1 :
                    continue
                move_coordinates.add(n)
                
            
        for m in move_coordinates:
            state_copy = self.state
            state_copy[m] = 1
            if state_copy != self.state
                lst.append(Gomoku(state_copy, self.state,self.score))
        return lst

            

    

def get_threat_patterns(board) -> List[int]:

    blacks = []
    whites = []

    for (key, value) in board.items():
        if value == 1:
            blacks.append(key)
        else:
            whites.append(key)

    black_half_two = 0
    black_half_three = 0
    black_half_four = 0
    black_open_two = 0
    black_open_three = 0
    black_open_four = 0
    
    white_half_two = 0
    white_half_three = 0
    white_half_four = 0
    white_open_two = 0
    white_open_three = 0
    white_open_four = 0

    possible_col_seqs = []

    for black in blacks:
        row_num = black[0]
        col_num = black[1]
        
        possible_col_coordinate = []
        for x in range(0, BOARD_SIZE):
            if abs(x - row_num) <= 4:
                possible_col_coordinate.append((x, col_num))
        
        while len(possible_col_coordinate) >= 4:
            possible_col_seqs.append(possible_col_coordinate[0:4])
            possible_col_coordinate.pop(0)
        
    #remove duplicate sequences
    possible_col_seqs.sort()
    possible_col_seqs = list(possible_col_seqs for possible_col_seqs,_ in itertools.groupby(possible_col_seqs))

    for possible_col_seq in possible_col_seqs:
        num_black = 0
        for coordinate in possible_col_seq:
            if board[coordinate] == 1:
                num_black += 1
        if num_black == 4:
            head = possible_col_seq[0]
            tail = possible_col_seq[-1]

            if head[0] != 0 and tail[0] != BOARD_SIZE-1:
                if board[(head[0]-1, head[1])] == 0 and board[(tail[0]+1, head[1])] == 0:
                    black_open_four += 1
            
            if head[0] == 0:
                if board[tail[0]+1, head[1]] == 0:
                    black_half_four += 1
            elif tail[0] == BOARD_SIZE-1:
                if board[head[0]-1, head[1]] == 0:
                    black_half_four += 1
            else:
                num_block = 0
                if board[(head[0]-1, head[1])] == 2: 
                    num_block += 1
                if board[(tail[0]+1, head[1])] == 2:
                    num_block += 1
                
                if num_block == 1:
                    black_half_four += 1
    
    return [black_open_four, black_half_four]


def minimax(node: Gomoku) -> int:
    """Compute manhattan distance f(node), i.e., g(node) + h(node)"""

    pass

if __name__ == "__main__":

    # You should not need to modify any of this code
    parser = argparse.ArgumentParser(
        description="Run search algorithms in random inputs"
    )
    parser.add_argument(
        "-a",
        "--algo",
        default="bfs",
        help="Algorithm (one of bfs, astar, astar_custom)",
    )
    parser.add_argument(
        "-i",
        "--iter",
        type=int,
        default=1000,
        help="Number of iterations",
    )
    parser.add_argument(
        "-s",
        "--state",
        type=str,
        default=None,
        help="Execute a single iteration using this board configuration specified as a string, e.g., 123456780",
    )

    args = parser.parse_args()

    num_solutions = 0
    num_cost = 0
    num_nodes = 0
