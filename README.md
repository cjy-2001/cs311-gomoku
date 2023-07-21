# CS311 Final Project - Gomoku Algorithm

![Tests](https://img.shields.io/badge/Tests-Passing-green) 
[![Coverage Status](https://coveralls.io/repos/github/cjy-2001/cs311-gomoku/badge.svg?branch=main)](https://coveralls.io/github/cjy-2001/cs311-gomoku?branch=main) [![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](https://github.com/cjy-2001/cs311-gomoku/blob/main/CS%20311%20Final%20Project%20Report.pdf)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> An AI algorithm for the abstract strategy board game, Gomoku.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Test](#test)
- [Method](#method)
- [References](#references)

## Background

Gomoku, or five in a row, is an abstract strategy board game where two players place a stone—either black or white—on a 15x15 board. The winner is the first to form an unbroken chain of five stones horizontally, vertically, or diagonally. Minimax algorithm is widely used in board games involving two-player competition such as Tic-Tac-Toe [1]. In 1992, Vardi [2] added expected values and utility into the minimax algorithm, making it possible to use evaluation functions to predict and calculates the possible scenarios. However, due to minimax’s O(b^d) time complexity, researchers have implemented various methods to improve its search performance especially in more complex games such as Gomoku. Typical methods include alpha-beta pruning that eliminates unpromising nodes [3], Monte Carlo Search Trees that adds randomization [4], and various heuristic functions [3]-[5]. 

We intend to implement the minimax algorithm with alpha-beta pruning and heuristic functions in Gomoku. We also explore how limiting relevant moves and different depth limits affect algorithm performance based on both search time and wining chances. 

![CS 311 Final Project Poster](https://github.com/cjy-2001/cs311-gomoku/blob/main/CS%20311%20Final%20Project%20Poster%20(PNG).png)

For our final report, please refer to [CS 311 Final Project Report](https://github.com/cjy-2001/cs311-gomoku/blob/main/CS%20311%20Final%20Project%20Report.pdf) and [CS 311 Final Project Poster](https://github.com/cjy-2001/cs311-gomoku/blob/main/CS%20311%20Final%20Project%20Poster.pdf).

## Install

```bash
git clone https://github.com/cjy-2001/cs311-gomoku.git
cd cs311-gomoku
```

## Usage

To use this project, you can run the `project.py` script providing a single argument that represents the current state of a Gomoku board. This board should be a minimum size of 5x5, but can be larger, such as 7x7 or 9x9. The board state should be provided as a list of integers (each being 0, 1, or 2), where 0 signifies an empty cell, 1 indicates a cell occupied by Player 1's stone, and 2 points to a cell occupied by Player 2's stone. The turn should be Player 1's.

For instance, consider the following 5x5 Gomoku board:

|   | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 |   |   |   |   |   |
| 1 |   | 2 | 2 | 1 |   |
| 2 |   | 2 | 1 |   |   |
| 3 |   | 1 | 2 |   |   |
| 4 | 1 |   |   |   |   |

To determine the optimal move for Player 1, you can execute:

```bash
python project.py "[0,0,0,0,0, 0,2,2,1,0, 0,2,1,0,0, 0,1,2,0,0, 1,0,0,0,0]" 5
```

The script will output a coordinate pair like (0, 4), implying that the best move for Player 1 would be to place their stone in cell (0, 4).

## Test

We have also included multiple tests to evaluate our code and resulted performance.
You can run the tests by executing the `project_test.py` file as a program, e.g. `python project_test.py`

```bash
python project_test.py
.........
----------------------------------------------------------------------
Ran 9 tests in 0.068s

OK
```

## Method

To tackle the computational challenges inherent in solving Gomoku, we adopt a strategy that combines efficient game state representation, focused search, and heuristic evaluation. We start by implementing a small board size and limit the depth and breadth of the search tree to manage the problem's complexity.

The game state is represented using a dictionary, which maps cell indices to the stones placed by players. This approach is akin to a Sudoku representation where we can use 0, 1, and 2 to denote unoccupied, player 1's move, and player 2's move respectively. For instance, an initial board would be represented as a sequence of 0s. As players take their turns, the game state is updated accordingly.

To limit the breadth of the search tree, we consider only the cells adjacent to the already occupied ones for potential moves. This approach reduces the number of nodes to be explored, thereby making the search process more efficient.

The choice of move is determined using the minimax algorithm, a recursive decision-making algorithm widely used in two-player games. We enhance the efficiency of the minimax algorithm with alpha-beta pruning, which prunes away branches in the game tree that do not need to be searched because there already exists a better move available.

We also employ a heuristic evaluation function that estimates the worth of a game state. This heuristic, which is used when the search depth limit is reached or a terminal state is encountered, is based on counting the number of open and half-open sequences of a specified length for a given player. This approach allows the AI to prioritize moves that will lead to a winning position or prevent the opponent from reaching such a position.

By combining these techniques, our implementation provides a robust and efficient solution to the Gomoku game, enabling the AI to make intelligent decisions even with limited computational resources.

## References

[1] Y. PIRILDAK, “Mastering Tic-Tac-Toe with Minimax Algorithm,” Medium, May 13, 2020. https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f (accessed Dec. 10, 2022).<br />
[2] A. Vardi, “New minimax algorithm,” J Optim Theory Appl, vol. 75, no. 3, pp. 613–634, Dec. 1992, doi: 10.1007/BF00940496.<br />
[3] E. Nygren, “Design Specifications for an Interactive Teaching Tool for Game AI using Gomoku”.<br />
[4] Yu. (2019). AI Agent for Playing Gomoku. Retrieved December 9, 2022. https://stanford-cs221.github.io/autumn2019-extra/posters/14.pdf<br />
[5] H. Liao, “New heuristic algorithm to improve the Minimax for Gomoku artificial intelligence”.<br />
[6] “Minimax Improvements.” https://blog.theofekfoundation.org/artificial-intelligence/2015/12/18/minimax-improvements/ (accessed Dec. 17, 2022).<br />
