"""
CS311 Final Project

Full Name(s): Jiayi Chen, Siyuan Niu

"""

import random
import itertools
import argparse
import json
from typing import List, Dict

# def draw_board(dic, size):
#     """
#     Helper function to draw the current board (debug purpose).

#     Args:
#     - dic: current board
#     - size: size of the bard
#     """
    
#     lst = list(dic.values())
#     for i in range(len(lst)):
#         if (i+1)% size ==0:
#             print(lst[i])
#         else:
#             print(lst[i], end = " ")


class Gomoku:
    """
    Class representing the Gomoku game.
    """

    # Problem constants
    BOARD_SIZE = 9
    
    def __init__(self, state: Dict = None, board_size: int = BOARD_SIZE, curr_depth: int = 0):
        """
        Initializes a Gomoku object.

        Args:
        - state: A dictionary representing the current game state. Keys are tuples of (row, col), values are 1 for black, 2 for white, and 0 for empty.
        - curr_depth: The current depth of the game tree in the Minimax search.
        """

        self.board_size = board_size

        if state is None:
            self.state = {}
            for i in range(self.board_size):
                for j in range(self.board_size):
                    self.state[(i, j)] = 0
        else:
            # If a state is provided, use it as the current game state.
            self.state = state

        self.gameStatus = 0
        self.curr_depth = curr_depth

        self.blacks = [coordinate for coordinate, value in self.state.items() if value == 1]
        self.whites = [coordinate for coordinate, value in self.state.items() if value == 2]

    
    def is_terminal(self) -> int:
        """
        Checks if the game is in a terminal state (someone has won or it's a draw).

        Returns:
        - 1 if Black wins
        - 2 if White wins
        - 3 if it's a draw
        - 0 if the game is still in progress
        """

        # Check rows, columns, and diagonals for a five-in-a-row
        for color in [1, 2]: 
            open, half = self.get_threat_patterns(color, 5)
            if open > 0 or half > 0:
                self.gameStatus = color
                return color

        # Check if the board is full (it's a draw)
        if len(self.blacks) + len(self.whites) == self.board_size ** 2:
            self.gameStatus = 3
            return 3

        # Game is still in progress
        return 0


    def get_threat_patterns(self, color: int, length: int) -> tuple([int, int]):
        """
        Identifies specific configurations of stones on the board. 

        Args:
        - color: 1 for black, 2 for white.
        - length: The length of the sequence to look for.

        Returns: 
        - A list of two integers representing the number of open and half-open sequences of the specified length for the given color.
        """
         
        board = self.state

        # Initialize counts for open and half-open sequences.
        open = 0
        half = 0
        
        possible_col_seqs = []
        possible_row_seqs = []
        possible_diag1_seqs = []
        possible_diag2_seqs = []

        if color == 1:
            stones = self.blacks
            opponent = 2
        else:
            stones = self.whites
            opponent = 1
            
        for stone in stones:
            row_num = stone[0]
            col_num = stone[1]
            
            # Look for possible row, col, and diag sequence of 5 stones
            possible_col_coordinates = []
            possible_row_coordinates = []
            possible_diag1_coordinates = []
            possible_diag2_coordinates = []

            for x in range(0, self.board_size):
                if abs(x - row_num) < length:
                    possible_col_coordinates.append((x, col_num))
                if abs(x - col_num) < length:
                    possible_row_coordinates.append((row_num, x))
            
            while len(possible_col_coordinates) >= length:
                possible_col_seqs.append(possible_col_coordinates[0:length])
                possible_col_coordinates.pop(0)
            while len(possible_row_coordinates) >= length:
                possible_row_seqs.append(possible_row_coordinates[0:length])
                possible_row_coordinates.pop(0)

            # Diagonal 1
            # Upper-left corner coordinates
            row_index = row_num
            col_index = col_num
            while (row_index > -1) and (col_index > -1):
                if (abs(row_index - row_num) + abs(col_index - col_num)) < length * 2:
                    possible_diag1_coordinates.insert(0, (row_index, col_index))
                row_index -= 1
                col_index -= 1
            
            # Lower-right corner coordinates
            row_index = row_num
            col_index = col_num
            while (row_index + 1 < self.board_size) and (col_index + 1 < self.board_size):
                if (abs(row_index - row_num) + abs(col_index - col_num)) < length * 2:
                    possible_diag1_coordinates.append((row_index + 1, col_index + 1))
                row_index += 1
                col_index += 1
            
            # Append the sequence if the coordinates make five-in-a-diagonal
            while len(possible_diag1_coordinates) >= length:
                possible_diag1_seqs.append(possible_diag1_coordinates[0:length])
                possible_diag1_coordinates.pop(0)

            # Diagonal 2
            # Upper-right corner coordinates
            row_index = row_num
            col_index = col_num
            while (row_index > -1) and (col_index < self.board_size):
                if (abs(row_index - row_num) + abs(col_index - col_num)) < length * 2:
                    possible_diag2_coordinates.insert(0, (row_index, col_index))
                row_index -= 1
                col_index += 1
            
            # Lower-left corner coordinates
            row_index = row_num
            col_index = col_num
            while (row_index + 1 < self.board_size) and (col_index - 1 > -1) and (col_index + 1 < self.board_size):
                if (abs(row_index - row_num) + abs(col_index - col_num)) < length * 2:
                    possible_diag2_coordinates.append((row_index + 1, col_index - 1))
                row_index += 1
                col_index -= 1
            
            
            # Append the sequence if the coordinates make five-in-a-diagonal
            while len(possible_diag2_coordinates) >= length:
                possible_diag2_seqs.append(possible_diag2_coordinates[0:length])
                possible_diag2_coordinates.pop(0)

        # Remove duplicate sequences
        possible_col_seqs.sort()
        possible_col_seqs = list(possible_col_seqs for possible_col_seqs,_ in itertools.groupby(possible_col_seqs))
        possible_row_seqs.sort()
        possible_row_seqs = list(possible_row_seqs for possible_row_seqs,_ in itertools.groupby(possible_row_seqs))
        possible_diag1_seqs.sort()
        possible_diag1_seqs_set = set(tuple(x) for x in possible_diag1_seqs)
        possible_diag1_seqs = [ list(x) for x in possible_diag1_seqs_set ]
        possible_diag2_seqs_set = set(tuple(x) for x in possible_diag2_seqs)
        possible_diag2_seqs = [ list(x) for x in possible_diag2_seqs_set ]

        # Start to count
        # Col
        for possible_col_seq in possible_col_seqs:
            num_stone = 0
            for coordinate in possible_col_seq:
                if board[coordinate] == color:
                    num_stone += 1
            if num_stone == length:
                if length == 5:
                    open += 1
                else: 
                    head = possible_col_seq[0]
                    tail = possible_col_seq[-1]

                    if head[0] != 0 and tail[0] != self.board_size-1:
                        if board[(head[0]-1, head[1])] == 0 and board[(tail[0]+1, head[1])] == 0:
                            open += 1
                    
                    if head[0] == 0:
                        if board[tail[0]+1, head[1]] == 0:
                            half += 1
                    elif tail[0] == self.board_size-1:
                        if board[head[0]-1, head[1]] == 0:
                            half += 1
                    else:
                        if board[(head[0]-1, head[1])] == opponent: 
                            if board[(tail[0]+1, head[1])] == 0:
                                half += 1
                        if board[(tail[0]+1, head[1])] == opponent:
                            if board[(head[0]-1, head[1])] == 0:
                                half += 1
        
        # Row
        for possible_row_seq in possible_row_seqs:
            num_stone = 0
            for coordinate in possible_row_seq:
                if board[coordinate] == color:
                    num_stone += 1
            if num_stone == length:
                if length == 5:
                    open += 1
                else:
                    head = possible_row_seq[0]
                    tail = possible_row_seq[-1]

                    if head[1] != 0 and tail[1] != self.board_size-1:
                        if board[(head[0], head[1]-1)] == 0 and board[(head[0], tail[1]+1)] == 0:
                            open += 1
                    
                    if head[1] == 0:
                        if board[head[0], tail[1]+1] == 0:
                            half += 1
                    elif tail[1] == self.board_size-1:
                        if board[head[0], head[1]-1] == 0:
                            half += 1
                    else:
                        if board[(head[0], head[1]-1)] == opponent: 
                            if board[(head[0], tail[1]+1)] == 0:
                                half += 1

                        if board[(head[0], tail[1]+1)] == opponent:
                            if board[(head[0], head[1]-1)] == 0:
                                half += 1

        # Diag1
        for possible_diag1_seq in possible_diag1_seqs:
            num_stone = 0
            for coordinate in possible_diag1_seq:
                if board[coordinate] == color:
                    num_stone += 1
            if num_stone == length:
                if length == 5:
                    open += 1
                else:
                    head = possible_diag1_seq[0]
                    tail = possible_diag1_seq[-1]

                    if head[0] != 0 and head[1] != 0 and tail[0] != self.board_size-1 and tail[1] != self.board_size-1:
                        if board[(head[0]-1, head[1]-1)] == 0 and board[(tail[0]+1, tail[1]+1)] == 0:
                            open += 1

                    if (head[0] == 0 or head[1] == 0) and (tail[0] != self.board_size-1 and tail[1] != self.board_size-1):
                        if board[tail[0]+1, tail[1]+1] == 0:
                            half += 1
                    elif (tail[0] == self.board_size-1 or tail[1] == self.board_size-1) and (head[0] != 0 and head[1] != 0):
                        if board[head[0]-1, head[1]-1] == 0:
                            half += 1
                    else:
                        if head[0] != 0 and head[1] != 0 and tail[0] != self.board_size-1 and tail[1] != self.board_size-1:
                            if board[(head[0]-1, head[1]-1)] == opponent: 
                                if board[(tail[0]+1, tail[1]+1)] == 0:
                                    half += 1
                            if board[(tail[0]+1, tail[1]+1)] == opponent:
                                if board[(head[0]-1, head[1]-1)] == 0:
                                    half += 1
                    
        # Diag2
        for possible_diag2_seq in possible_diag2_seqs:
            num_stone = 0
            for coordinate in possible_diag2_seq:
                if board[coordinate] == color:
                    num_stone += 1
            if num_stone == length:
                if length == 5:
                    open += 1
                else:
                    head = possible_diag2_seq[0]
                    tail = possible_diag2_seq[-1]

                    if head[0] != 0 and head[1] != self.board_size-1 and tail[0] != self.board_size-1 and tail[1] != 0:
                        if board[(head[0]-1, head[1]+1)] == 0 and board[(tail[0]+1, tail[1]-1)] == 0:
                            open += 1

                    if (head[0] == 0 or head[1] == self.board_size-1) and (tail[0] != self.board_size-1 and tail[1] != 0):
                        if board[tail[0]+1, tail[1]-1] == 0:
                            half += 1
                            
                    elif (tail[0] == self.board_size-1 or tail[1] == 0) and (head[0] != 0 and head[1] != self.board_size-1):
                        if board[head[0]-1, head[1]+1] == 0:
                            half += 1
                            
                    else:
                        if head[0] != 0 and head[1] != self.board_size-1 and tail[0] != self.board_size-1 and tail[1] != 0:
                            if board[(head[0]-1, head[1]+1)] == opponent: 
                                if board[(tail[0]+1, tail[1]-1)] == 0:
                                    half += 1
                                    
                            if board[(tail[0]+1, tail[1]-1)] == opponent:
                                if board[(head[0]-1, head[1]+1)] == 0:
                                    half += 1
                                
        return open, half
    

    def get_possible_moves(self) -> List["Gomoku"]:
        """
        Generates all possible moves for the current state of the board.

        Args:
        - color: 1 for black, 2 for white.

        Returns:
        - A list of tuples representing the coordinates of all possible moves.
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
                if n[0] < 0 or n[1] < 0 or n[0] > self.board_size - 1 or n[1] > self.board_size - 1 :
                    continue
                move_coordinates.add(n)

        for m in move_coordinates:
            state_copy = self.state.copy()
            
            if self.state[m] == 0:
                if len(self.blacks) > len(self.whites):
                    state_copy[m] = 2
                    lst.append(Gomoku(state=state_copy, board_size=self.board_size, curr_depth=self.curr_depth+1))
                else:
                    state_copy[m] = 1
                    lst.append(Gomoku(state=state_copy, board_size=self.board_size, curr_depth=self.curr_depth+1))
                
        return lst

    def minimax(self, maximizing: bool, depth: int) -> int:
        """
        The Minimax algorithm without alpha-beta pruning.

        Args:
        - maximizing: True if the current level is a maximizing level, False if it's a minimizing level.
        - depth: The current depth of the game tree.
        
        Returns:
        - The best score.
        """
        
        if self.is_terminal() or self.curr_depth > depth:
            # Count black patterns
            [black_open_two, black_half_two] = self.get_threat_patterns(color=1, length=2)
            [black_open_three, black_half_three] = self.get_threat_patterns(color=1, length=3)
            [black_open_four, black_half_four] = self.get_threat_patterns(color=1, length=4)
            [black_open_five, black_half_five] = self.get_threat_patterns(color=1, length=5)
            black_five = black_open_five + black_half_five

            # Count white patterns
            [white_open_two, white_half_two] = self.get_threat_patterns(color=2, length=2)
            [white_open_three, white_half_three] = self.get_threat_patterns(color=2, length=3)
            [white_open_four, white_half_four] = self.get_threat_patterns(color=2, length=4)
            [white_open_five, white_half_five] = self.get_threat_patterns(color=2, length=5)
            white_five = white_open_five + white_half_five

            five_diff = black_five - white_five
            four_open_diff = black_open_four - white_open_four
            four_half_diff = black_half_four - white_half_four
            three_open_diff = black_open_three - white_open_three
            three_half_diff = black_half_three - white_half_three
            two_open_diff = black_open_two - white_open_two
            two_half_diff = black_half_two - white_half_two

            # Compared with another evaluation function
            # return (6000 * five_diff + 
            # 4800 * four_open_diff + 500 * four_half_diff + 
            # 500 * three_open_diff + 200 * three_half_diff + 
            # 50 * two_open_diff + 10 * two_half_diff), self.state
            
            return (10000 * five_diff + 
            5000 * four_open_diff + 2500 * four_half_diff + 
            2000 * three_open_diff + 1000 * three_half_diff + 
            250 * two_open_diff + 50 * two_half_diff), self.state

        scores = []
        for board in self.get_possible_moves():
            scores.append(board.minimax(not maximizing, depth=depth))

        if maximizing:
            return max(scores, key=lambda item:item[0])
        else:
            return min(scores, key=lambda item:item[0])


    def new_minimax(self, maximizing: bool, depth: int, alpha=float('-inf'), beta=float('inf')) -> tuple([int, dict]):
        """
        The Minimax algorithm with alpha-beta pruning.

        Args:
        - maximizing: True if the current level is a maximizing level, False if it's a minimizing level.
        - depth: The current depth of the game tree.

        Returns:
        - The best score.
        """
        
        if self.is_terminal() or self.curr_depth > depth:
            # Count black patterns
            [black_open_two, black_half_two] = self.get_threat_patterns(color=1, length=2)
            [black_open_three, black_half_three] = self.get_threat_patterns(color=1, length=3)
            [black_open_four, black_half_four] = self.get_threat_patterns(color=1, length=4)
            [black_open_five, black_half_five] = self.get_threat_patterns(color=1, length=5)
            black_five = black_open_five + black_half_five

            # Count white patterns
            [white_open_two, white_half_two] = self.get_threat_patterns(color=2, length=2)
            [white_open_three, white_half_three] = self.get_threat_patterns(color=2, length=3)
            [white_open_four, white_half_four] = self.get_threat_patterns(color=2, length=4)
            [white_open_five, white_half_five] = self.get_threat_patterns(color=2, length=5)
            white_five = white_open_five + white_half_five

            five_diff = black_five - white_five
            four_open_diff = black_open_four - white_open_four
            four_half_diff = black_half_four - white_half_four
            three_open_diff = black_open_three - white_open_three
            three_half_diff = black_half_three - white_half_three
            two_open_diff = black_open_two - white_open_two
            two_half_diff = black_half_two - white_half_two
            
            return (10000 * five_diff + 
            5000 * four_open_diff + 2500 * four_half_diff + 
            2000 * three_open_diff + 1000 * three_half_diff + 
            250 * two_open_diff + 50 * two_half_diff), self.state


        if maximizing:
            bestValue = (float('-inf'), self.state)
            for board in self.get_possible_moves():
                value = (board.new_minimax(not maximizing, depth=depth, alpha=alpha, beta=beta))
                bestValue = max(bestValue, value, key=lambda item:item[0]) 
                alpha = max(alpha, bestValue[0])
                if beta <= alpha:
                    break

            return bestValue

        else:
            bestValue = (float('inf'), self.state)
            for board in self.get_possible_moves():
                value = (board.new_minimax(not maximizing, depth=depth, alpha=alpha, beta=beta))
                bestValue = min(bestValue, value, key=lambda item:item[0]) 
                beta = min(beta, bestValue[0])
                if beta <= alpha:
                    break

            return bestValue


    def best_move(self, depth) -> tuple([tuple([int, int]), int]):
        """
        Return the best move for black based on score calculated from minimax.

        Args:
        - depth: The current depth of the game tree.
        """

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
                if n[0] < 0 or n[1] < 0 or n[0] > self.board_size - 1 or n[1] > self.board_size - 1 :
                    continue
                if self.state[n] == 0:
                    move_coordinates.add(n)

        bestMove = None, 0

        alpha = float('-inf')
        for m in move_coordinates:
            state_copy = self.state.copy()
            state_copy[m] = 1
            gomoku = Gomoku(state=state_copy, board_size=self.board_size, curr_depth=self.curr_depth+1)
            score = gomoku.new_minimax(maximizing=False, depth=depth, alpha=alpha)[0]
            if score >= bestMove[1]:
                alpha = max(alpha, score)
                bestMove = m, score
                
        return bestMove

    
    def play(self, depth) -> int:
        """
        Played on the current board, with black uses minimax with depth and white playing randomly.

        Args:
        - depth: The current depth of the game tree.
        """

        if self.is_terminal():
            return self.is_terminal()
        
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
                if n[0] < 0 or n[1] < 0 or n[0] > self.board_size - 1 or n[1] > self.board_size - 1 :
                    continue
                if self.state[n] == 0:
                    move_coordinates.add(n)
            
            
        move_coordinates2 = list(move_coordinates)
        state_copy = self.state.copy()
        if len(self.blacks) > len(self.whites):
            coordinate = random.choice(move_coordinates2)
            state_copy[coordinate] = 2
            new_board = Gomoku(state=state_copy, board_size=self.board_size, curr_depth=self.curr_depth+1)
        else:
            coordinate = self.best_move(depth)[0]
            state_copy[coordinate] = 1
            new_board = Gomoku(state=state_copy, board_size=self.board_size, curr_depth=self.curr_depth+1)

        return new_board.play(depth)


    def play_randomly(self) -> int:
        """
        Played on the current board, with both black and white playing randomly.
        """

        if self.is_terminal():
            return self.is_terminal()
        
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
                if n[0] < 0 or n[1] < 0 or n[0] > self.board_size - 1 or n[1] > self.board_size - 1 :
                    continue
                if self.state[n] == 0:
                    move_coordinates.add(n)
            
            
        move_coordinates2 = list(move_coordinates)
        state_copy = self.state.copy()
        if len(self.blacks) > len(self.whites):
            coordinate = random.choice(move_coordinates2)
            state_copy[coordinate] = 2
            new_board = Gomoku(state=state_copy, board_size=self.board_size, curr_depth=self.curr_depth+1)
        else:
            coordinate = random.choice(move_coordinates2)
            state_copy[coordinate] = 1
            new_board = Gomoku(state=state_copy, board_size=self.board_size, curr_depth=self.curr_depth+1)

        return new_board.play_randomly()


def main():
    parser = argparse.ArgumentParser(description='Gomoku AI Agent')
    parser.add_argument('board', metavar='B', type=str, help='The current state of the game board')
    parser.add_argument('board_size', metavar='S', type=int, help='The size of the game board')

    args = parser.parse_args()

    board = json.loads(args.board)
    board_size = args.board_size

    if isinstance(board, list):
        # Convert the list to a dictionary
        board_dict = {(i//board_size, i%board_size): board[i] for i in range(len(board))}
        gomoku = Gomoku(state=board_dict, board_size=board_size)
    elif isinstance(board, dict):
        gomoku = Gomoku(state=board, board_size=board_size)
    else:
        raise TypeError("Board must be either a list or a dictionary")

    # Print the best move
    print(gomoku.best_move(3)[0])  # Assuming a depth of 3 for the minimax algorithm


if __name__ == "__main__":
    main()
