"""
CS311 Final Project

Full Name(s): Jiayi Chen, Siyuan Niu

"""

import argparse, itertools, random
from heapq import heapify, heappush, heappop
from typing import Callable, List, Optional, Sequence, Tuple


# Problem constants. 
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
    def __init__(self, state: dict[(int, int): int], parent: "Gomoku" = None, score=0, moves=0):
        """Create Node to track particular state and associated parent and cost

        Args:

            state (dict[(int, int): int]): current distribution of stones on the board; 
                                            key as the coordinate (row, col) of the cell and value as the stone (0-empty, 1-black, 2-white);
                                            all values are initialized as 0's
            parent: parent Gomoku, None indicates the root node. Defaults to None.
            score:(int) score indicating optimality as the result of the evaluation function
            gameStatus: (int or string)  = 1 if black wins, = 2 if white wins, = 0 if a draw, otherwise "game_on"
            curr_depth: depth of the Gomoku node in the expectiminimax tree
        """
        self.state = state  # To facilitate "hashable" make state immutable
        self.parent = parent
        self.score = score
        self.gameStatus = "game_on" 
        self.curr_depth = moves

        blacks = []
        whites = []

        for (key, value) in state.items():
            if value == 1:
                blacks.append(key)
            else:
                whites.append(key)

        self.blacks = blacks
        self.whites = whites

    
    def is_terminal(self) -> bool:
        """Return True if game terminates"""
        
        board = self.state
        
        # get coordinates of all black and white stones
        # blacks = []
        # whites = []

        # for (key, value) in board.items():
        #     if value == 1:
        #         blacks.append(key)
        #     else:
        #         whites.append(key)

        black_five = 0
        white_five = 0

        # Initialize lists of the combinations of coordinates (sequences) on each direction that make black the winner
        possible_col_seqs = []
        possible_row_seqs = []
        possible_diag1_seqs = []
        possible_diag2_seqs = []

        for black in self.blacks:
            row_num = black[0]
            col_num = black[1]
            
            # Find all possible coordinates that makes black the winner
            possible_col_coordinates = []
            possible_row_coordinates = []
            possible_diag1_coordinates = []
            possible_diag2_coordinates = []

            # Coordinates in the same row or the same column
            for x in range(0, BOARD_SIZE):
                if abs(x - row_num) < 5:
                    possible_col_coordinates.append((x, col_num))
                if abs(x - col_num) < 5:
                    possible_row_coordinates.append((row_num, x))

            # Append the sequence if the coordinates make five-in-a-row or five-in-a-column
            while len(possible_col_coordinates) >= 5:
                possible_col_seqs.append(possible_col_coordinates[0:5])
                possible_col_coordinates.pop(0)
            while len(possible_row_coordinates) >= 5:
                possible_row_seqs.append(possible_row_coordinates[0:5])
                possible_row_coordinates.pop(0)


            # Coordinates in the diagonal 1
            # Upper-left corner coordinates
            row_index = row_num
            col_index = col_num
            while (row_index > -1) and (col_index > -1):
                possible_diag1_coordinates.insert(0, (row_index, col_index))
                row_index -= 1
                col_index -= 1
            
            # Lower-right corner coordinates
            row_index = row_num
            col_index = col_num
            while (row_index + 1 < BOARD_SIZE) and (col_index + 1 < BOARD_SIZE):
                possible_diag1_coordinates.append((row_index + 1, col_index + 1))
                row_index += 1
                col_index += 1
            
            # Append the sequence if the coordinates make five-in-a-diagonal
            while len(possible_diag1_coordinates) >= 5:
                possible_diag1_seqs.append(possible_diag1_coordinates[0:5])
                possible_diag1_coordinates.pop(0)

            
            # Coordinates in the diagonal 2
            # Upper-right corner coordinates
            row_index = row_num
            col_index = col_num
            while (row_index > -1) and (col_index < BOARD_SIZE):
                possible_diag2_coordinates.insert(0, (row_index, col_index))
                row_index -= 1
                col_index += 1
            
            # Lower-left corner coordinates
            row_index = row_num
            col_index = col_num
            while (row_index + 1 < BOARD_SIZE) and (col_index + 1 > -1) and (col_index + 1 < BOARD_SIZE):
                possible_diag2_coordinates.append((row_index + 1, col_index + 1))
                row_index += 1
                col_index -= 1
            
            # Append the sequence if the coordinates make five-in-a-diagonal
            while len(possible_diag2_coordinates) >= 5:
                possible_diag2_seqs.append(possible_diag2_coordinates[0:5])
                possible_diag2_coordinates.pop(0)

        # print(possible_col_seqs)
            
        # Remove duplicate sequences
        possible_col_seqs.sort()
        possible_col_seqs = list(possible_col_seqs for possible_col_seqs,_ in itertools.groupby(possible_col_seqs))
        possible_row_seqs.sort()
        possible_row_seqs = list(possible_row_seqs for possible_row_seqs,_ in itertools.groupby(possible_row_seqs))
        # possible_diag2_seqs.sort()
        # possible_diag2_seqs = list(possible_diag2_seqs for possible_diag2_seqs,_ in itertools.groupby(possible_diag2_seqs))
        # possible_diag1_seqs.sort()
        # possible_diag1_seqs = list(possible_diag1_seqs for possible_diag1_seqs,_ in itertools.groupby(possible_diag1_seqs))
        possible_diag1_seqs_set = set(tuple(x) for x in possible_diag1_seqs)
        possible_diag1_seqs = [ list(x) for x in possible_diag1_seqs_set ]
        possible_diag2_seqs_set = set(tuple(x) for x in possible_diag2_seqs)
        possible_diag2_seqs = [ list(x) for x in possible_diag2_seqs_set ]
        
        # print(possible_col_seqs)

        # Count how many 5 consecutive coordinates - sequences -  in a row, col, or diag
        for possible_col_seq in possible_col_seqs:
            num_black = 0
            for coordinate in possible_col_seq:
                if board[coordinate] == 1:
                    num_black += 1
            if num_black == 5:
                black_five += 1

        for possible_row_seq in possible_row_seqs:
            num_black = 0
            for coordinate in possible_row_seq:
                if board[coordinate] == 1:
                    num_black += 1
            if num_black == 5:
                black_five += 1
        
        #print(possible_diag1_seqs)
        for possible_diag1_seq in possible_diag1_seqs:
            num_black = 0
            for coordinate in possible_diag1_seq:
                if board[coordinate] == 1:
                    num_black += 1
            if num_black == 5:
                black_five += 1
        
        #print(possible_diag2_seqs)
        for possible_diag2_seq in possible_diag2_seqs:
            num_black = 0
            for coordinate in possible_diag2_seq:
                if board[coordinate] == 1:
                    num_black += 1
            if num_black == 5:
                black_five += 1

        

        # Repeat for white as the winner
        possible_col_seqs = []
        possible_row_seqs = []
        possible_diag1_seqs = []
        possible_diag2_seqs = []

        for white in self.whites:
            row_num = white[0]
            col_num = white[1]
            
            #look for possible row, col, and diag sequence of 5 stones
            possible_col_coordinates = []
            possible_row_coordinates = []
            possible_diag1_coordinates = []
            possible_diag2_coordinates = []
            
            for x in range(0, BOARD_SIZE):
                if abs(x - row_num) <= 5:
                    possible_col_coordinates.append((x, col_num))
                if abs(x - col_num) <= 5:
                    possible_row_coordinates.append((row_num, x))
            
            while len(possible_col_coordinates) >= 5:
                possible_col_seqs.append(possible_col_coordinates[0:5])
                possible_col_coordinates.pop(0)

            while len(possible_row_coordinates) >= 5:
                possible_row_seqs.append(possible_row_coordinates[0:5])
                possible_row_coordinates.pop(0)


            #diag1s
            #upper left corner
            row_index = row_num
            col_index = col_num
            while (row_index > -1) and (col_index > -1):
                possible_diag1_coordinates.insert(0, (row_index, col_index))
                row_index -= 1
                col_index -= 1
            
            #lower right corner
            row_index = row_num
            col_index = col_num
            while (row_index + 1 < BOARD_SIZE) and (col_index + 1 < BOARD_SIZE):
                possible_diag1_coordinates.append((row_index + 1, col_index + 1))
                row_index += 1
                col_index += 1
            
            while len(possible_diag1_coordinates) >= 5:
                possible_diag1_seqs.append(possible_diag1_coordinates[0:5])
                possible_diag1_coordinates.pop(0)

            #diag2s
            #upper right corner
            row_index = row_num
            col_index = col_num
            while (row_index > -1) and (col_index < BOARD_SIZE):
                possible_diag2_coordinates.insert(0, (row_index, col_index))
                row_index -= 1
                col_index += 1
            
            #lower left corner
            row_index = row_num
            col_index = col_num
            while (row_index + 1 < BOARD_SIZE) and (col_index + 1 > -1) and (col_index + 1 < BOARD_SIZE):
                possible_diag2_coordinates.append((row_index + 1, col_index + 1))
                row_index += 1
                col_index -= 1
            
            while len(possible_diag2_coordinates) >= 5:
                possible_diag2_seqs.append(possible_diag2_coordinates[0:5])
                possible_diag2_coordinates.pop(0)
            
        #remove duplicate sequences
        possible_col_seqs.sort()
        possible_col_seqs = list(possible_col_seqs for possible_col_seqs,_ in itertools.groupby(possible_col_seqs))
        possible_row_seqs.sort()
        possible_row_seqs = list(possible_row_seqs for possible_row_seqs,_ in itertools.groupby(possible_row_seqs))
        # possible_diag2_seqs.sort()
        # possible_diag2_seqs = list(possible_diag2_seqs for possible_diag2_seqs,_ in itertools.groupby(possible_diag2_seqs))
        # possible_diag1_seqs.sort()
        # possible_diag1_seqs = list(possible_diag1_seqs for possible_diag1_seqs,_ in itertools.groupby(possible_diag1_seqs))
        possible_diag1_seqs_set = set(tuple(x) for x in possible_diag1_seqs)
        possible_diag1_seqs = [ list(x) for x in possible_diag1_seqs_set ]
        possible_diag2_seqs_set = set(tuple(x) for x in possible_diag2_seqs)
        possible_diag2_seqs = [ list(x) for x in possible_diag2_seqs_set ]

        #count how many 5 in a row, seq, or diag
        for possible_col_seq in possible_col_seqs:
            num_white = 0
            for coordinate in possible_col_seq:
                if board[coordinate] == 2:
                    num_white += 1
            if num_white == 5:
                white_five += 1

        for possible_row_seq in possible_row_seqs:
            num_white = 0
            for coordinate in possible_row_seq:
                if board[coordinate] == 2:
                    num_white += 1
            if num_white == 5:
                white_five += 1

        for possible_diag1_seq in possible_diag1_seqs:
            num_white = 0
            for coordinate in possible_diag1_seq:
                if board[coordinate] == 2:
                    num_white += 1
            if num_white == 5:
                white_five += 1
        
        for possible_diag2_seq in possible_diag2_seqs:
            num_white = 0
            for coordinate in possible_diag2_seq:
                if board[coordinate] == 2:
                    num_white += 1
            if num_white == 5:
                white_five += 1


        #if we have 5 stones of either black or white?        
        if black_five > 0:
            self.gameStatus = 1
            return True

        if white_five > 0:
            self.gameStatus = 2
            return True

        if list(board.values()).count(0) == 0:
            self.gameStatus = 0
            return True

        return False

    def get_threat_patterns(self, color: int, length: int) -> tuple([int, int]):
        """Return the numbers of open and  half open consecutive stones - threat patterns - in a tuple given a player and a pattern size.
         
         Open threat pattern: patterns without opponent stones on both sides

         Half open threat pattern: patterns with an opponent stone on either side

         The size range of a threat pattern is 2 to 4. 
    
         """
         
        board = self.state
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
            
            #look for possible row, col, and diag sequence of 5 stones
            possible_col_coordinates = []
            possible_row_coordinates = []
            possible_diag1_coordinates = []
            possible_diag2_coordinates = []

            for x in range(0, BOARD_SIZE):
                if abs(x - row_num) < length:
                    possible_col_coordinates.append((x, col_num))
                if abs(x - col_num) < length:
                    possible_row_coordinates.append((row_num, x))
            
            # print(possible_row_coordinates)
            while len(possible_col_coordinates) >= length:
                possible_col_seqs.append(possible_col_coordinates[0:length])
                possible_col_coordinates.pop(0)
            while len(possible_row_coordinates) >= length:
                possible_row_seqs.append(possible_row_coordinates[0:length])
                possible_row_coordinates.pop(0)

            # print(possible_row_seqs)

            # Coordinates in the diagonal 1
            # Upper-left corner coordinates
            row_index = row_num
            col_index = col_num
            while (row_index > -1) and (col_index > -1):
                possible_diag1_coordinates.insert(0, (row_index, col_index))
                row_index -= 1
                col_index -= 1
            
            # Lower-right corner coordinates
            row_index = row_num
            col_index = col_num
            while (row_index + 1 < BOARD_SIZE) and (col_index + 1 < BOARD_SIZE):
                possible_diag1_coordinates.append((row_index + 1, col_index + 1))
                row_index += 1
                col_index += 1
            
            # Append the sequence if the coordinates make five-in-a-diagonal
            while len(possible_diag1_coordinates) >= length:
                possible_diag1_seqs.append(possible_diag1_coordinates[0:length])
                possible_diag1_coordinates.pop(0)


            # Coordinates in the diagonal 2
            # Upper-right corner coordinates
            row_index = row_num
            col_index = col_num
            while (row_index > -1) and (col_index < BOARD_SIZE):
                possible_diag2_coordinates.insert(0, (row_index, col_index))
                row_index -= 1
                col_index += 1
            
            # Lower-left corner coordinates
            row_index = row_num
            col_index = col_num
            while (row_index + 1 < BOARD_SIZE) and (col_index + 1 > -1) and (col_index + 1 < BOARD_SIZE):
                possible_diag2_coordinates.append((row_index + 1, col_index + 1))
                row_index += 1
                col_index -= 1
            
            # Append the sequence if the coordinates make five-in-a-diagonal
            while len(possible_diag2_coordinates) >= length:
                possible_diag2_seqs.append(possible_diag2_coordinates[0:length])
                possible_diag2_coordinates.pop(0)

        
        #remove duplicate sequences
        possible_col_seqs.sort()
        possible_col_seqs = list(possible_col_seqs for possible_col_seqs,_ in itertools.groupby(possible_col_seqs))
        possible_row_seqs.sort()
        possible_row_seqs = list(possible_row_seqs for possible_row_seqs,_ in itertools.groupby(possible_row_seqs))
        possible_diag1_seqs.sort()
        # possible_diag2_seqs.sort()
        # possible_diag2_seqs = list(possible_diag2_seqs for possible_diag2_seqs,_ in itertools.groupby(possible_diag2_seqs))
        # possible_diag1_seqs.sort()
        # possible_diag1_seqs = list(possible_diag1_seqs for possible_diag1_seqs,_ in itertools.groupby(possible_diag1_seqs))
        possible_diag1_seqs_set = set(tuple(x) for x in possible_diag1_seqs)
        possible_diag1_seqs = [ list(x) for x in possible_diag1_seqs_set ]
        possible_diag2_seqs_set = set(tuple(x) for x in possible_diag2_seqs)
        possible_diag2_seqs = [ list(x) for x in possible_diag2_seqs_set ]

        
        #start to count
        #col
        for possible_col_seq in possible_col_seqs:
            num_stone = 0
            for coordinate in possible_col_seq:
                if board[coordinate] == color:
                    num_stone += 1
            if num_stone == length:
                head = possible_col_seq[0]
                tail = possible_col_seq[-1]

                if head[0] != 0 and tail[0] != BOARD_SIZE-1:
                    if board[(head[0]-1, head[1])] == 0 and board[(tail[0]+1, head[1])] == 0:
                        open += 1
                        print(possible_col_seq)
                
                if head[0] == 0:
                    if board[tail[0]+1, head[1]] == 0:
                        half += 1
                elif tail[0] == BOARD_SIZE-1:
                    if board[head[0]-1, head[1]] == 0:
                        half += 1
                else:
                    if board[(head[0]-1, head[1])] == opponent: 
                        if board[(tail[0]+1, head[1])] == 0:
                            half += 1
                    if board[(tail[0]+1, head[1])] == opponent:
                        if board[(head[0]-1, head[1])] == 0:
                            half += 1
        
        #row
        for possible_row_seq in possible_row_seqs:
            num_stone = 0
            for coordinate in possible_row_seq:
                if board[coordinate] == color:
                    num_stone += 1
            if num_stone == length:
                head = possible_row_seq[0]
                tail = possible_row_seq[-1]

                if head[1] != 0 and tail[1] != BOARD_SIZE-1:
                    if board[(head[0], head[1]-1)] == 0 and board[(head[0], tail[1]+1)] == 0:
                        open += 1
                        # print(possible_row_seq)
                
                if head[1] == 0:
                    if board[head[0], tail[1]+1] == 0:
                        half += 1
                elif tail[1] == BOARD_SIZE-1:
                    if board[head[0], head[1]-1] == 0:
                        half += 1
                else:
                    if board[(head[0], head[1]-1)] == opponent: 
                        if board[(head[0], tail[1]+1)] == 0:
                            half += 1
                            # print(possible_row_seq)

                    if board[(head[0], tail[1]+1)] == opponent:
                        if board[(head[0], head[1]-1)] == 0:
                            half += 1
                            print(possible_row_seq)

        # #diag1
        # for possible_diag1_seq in possible_diag1_seqs:
        #     num_stone = 0
        #     for coordinate in possible_diag1_seq:
        #         if board[coordinate] == color:
        #             num_stone += 1
        #     if num_stone == length:
        #         head = possible_diag1_seq[0]
        #         tail = possible_diag1_seq[-1]

        #         if head[0] != 0 and head[1] != 0 and tail[0] != BOARD_SIZE-1 and tail[1] != BOARD_SIZE-1:
        #             if board[(head[0]-1, head[1]-1)] == 0 and board[(tail[0]+1, tail[1]+1)] == 0:
        #                 open += 1

        #         if (head[0] == 0 or head[1] == 0) and (tail[0] != BOARD_SIZE-1 and tail[1] != BOARD_SIZE-1):
        #             if board[tail[0]+1, tail[1]+1] == 0:
        #                 half += 1
        #         elif (tail[0] == BOARD_SIZE-1 or tail[1] == BOARD_SIZE-1) and (head[0] != 0 and head[1] != 0):
        #             if board[head[0]-1, head[1]-1] == 0:
        #                 half += 1
        #         else:
        #             if head[0] != 0 and head[1] != 0 and tail[0] != BOARD_SIZE-1 and tail[1] != BOARD_SIZE-1:
        #                 if board[(head[0]-1, head[1]+1)] == opponent: 
        #                     if board[(tail[0]+1, tail[1]-1)] == 0:
        #                         half += 1
        #                 if board[(tail[0]+1, tail[1]-1)] == opponent:
        #                     if board[(head[0]-1, head[1]+1)] == 0:
        #                         half += 1
                    


        #diag2
        for possible_diag2_seq in possible_diag2_seqs:
            num_stone = 0
            for coordinate in possible_diag2_seq:
                if board[coordinate] == color:
                    num_stone += 1
            if num_stone == length:
                head = possible_diag2_seq[0]
                tail = possible_diag2_seq[-1]

                if head[0] != 0 and head[1] != BOARD_SIZE-1 and tail[0] != BOARD_SIZE-1 and tail[1] != 0:
                    if board[(head[0]-1, head[1]+1)] == 0 and board[(tail[0]+1, tail[1]-1)] == 0:
                        open += 1

                if (head[0] == 0 or head[1] == BOARD_SIZE-1) and (tail[0] != BOARD_SIZE-1 and tail[1] != 0):
                    if board[tail[0]+1, tail[1]-1] == 0:
                        half += 1
                elif (tail[0] == BOARD_SIZE-1 or tail[1] == 0) and (head[0] != 0 and head[1] != BOARD_SIZE-1):
                    if board[head[0]-1, head[1]+1] == 0:
                        half += 1
                else:
                    if head[0] != 0 and head[1] != BOARD_SIZE-1 and tail[0] != BOARD_SIZE-1 and tail[1] != 0:
                        if board[(head[0]-1, head[1]-1)] == opponent: 
                            if board[(tail[0]+1, tail[1]+1)] == 0:
                                half += 1
                        if board[(tail[0]+1, tail[1]+1)] == opponent:
                            if board[(head[0]-1, head[1]-1)] == 0:
                                half += 1

        
        return open, half
    
    def best_move(self) -> tuple:
        """Return the agent's next move"""
        pass 
    

    def get_possible_moves(self) -> List["Gomoku"]:
        """Find the neighbors of all filled cells as all next possible moves,
            return a list of child Gomoku objects with each neighbor filled
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
            # print(move_coordinates)
                
            
        for m in move_coordinates:
            state_copy = self.state
            if self.state[m] == 0:
                state_copy[m] = 1
                lst.append(Gomoku(state_copy, self.state,self.score))
                
        return lst

    def minimax(self, maximizing: bool, node: "Gomoku") -> int:
        """Return the score of min or max depending on the perspective"""
    
        #black 5 in a row +10000000
        #black open 4 in a row +999999
        #black half 4 in a row +400000
        if self.is_terminal() or self.curr_depth > 5:
            
            #count black patterns
            [black_open_two, black_half_two] = self.get_threat_patterns(color=1, length=2)
            [black_open_three, black_half_three] = self.get_threat_patterns(color=1, length=3)
            [black_open_four, black_half_four] = self.get_threat_patterns(color=1, length=4)
            [black_open_five, black_half_five] = self.get_threat_patterns(color=1, length=5)
            black_five = black_open_five + black_half_five


            #count white patterns
            [white_open_two, white_half_two] = self.get_threat_patterns(color=2, length=2)
            [white_open_three, white_half_three] = self.get_threat_patterns(color=2, length=3)
            [white_open_four, white_half_four] = self.get_threat_patterns(color=2, length=4)
            [white_open_five, white_half_five] = self.get_threat_patterns(color=2, length=5)
            white_five = white_open_five + white_half_five

            return black_open_four * 4800 + black_half_four * 500

            
        scores = []
        for move in self.get_possible_moves():
            scores.append(self.minimax(not maximizing, move))

        if maximizing:
            return max(scores)
        else:
            return min(scores)


if __name__ == "__main__":
    pass
