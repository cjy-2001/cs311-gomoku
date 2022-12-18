# CS311 Final Project - Gomoku Algorithm

Gomoku, or five in a row, is an abstract strategy board game where two players place a stone—either black or white—on a 15x15 board. The winner is the first to form an unbroken chain of five stones horizontally, vertically, or diagonally. Minimax algorithm is widely used in board games involving two-player competition such as Tic-Tac-Toe [1]. In 1992, Vardi [2] added expected values and utility into the minimax algorithm, making it possible to use evaluation functions to predict and calculates the possible scenarios. However, due to minimax’s O(b^d) time complexity, researchers have implemented various methods to improve its search performance especially in more complex games such as Gomoku. Typical methods include alpha-beta pruning that eliminates unpromising nodes [3], Monte Carlo Search Trees that adds randomization [4], and various heuristic functions [3]-[5]. 

We intend to implement the minimax algorithm with alpha-beta pruning and heuristic functions in Gomoku. We also explore how limiting relevant moves and different depth limits affect algorithm performance based on both search time and wining chances. 

For our final report, please refer to "CS 311 Final Project Poster.pdf".

## Method

To resolve computational difficulties, we’ll start by a small board size and try limiting the depth and breadth of the tree by, for example, restricting the set of unassigned grids to those adjacent to the assigned ones only or by limiting the depth of the evaluation function. 

Several sample codes are available as references for our project, in which the game is a class with functions that initialize the board, determine the game termination, calculate the agent's optimal move, and optimize the minimax via alpha-beta pruning. Our board initialization, meanwhile, will be similar to that of a sudoku in PA2 where we use a dictionary storing the cell indices and its corresponding stones when filled by a player.  For example, in the initial board, all cells will be marked as 0. Then we can use 1 and 2 to denote two players’ moves. Thus the board below would be represented as:
 [0, 0, 0, 0, 0, 
  0, 0, 1, 2, 0,
  0, 0, 1, 0, 0, 
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0]


## Unit testing

We have also included multiple tests to evaluate our code and resulted performance.
You can run the tests by executing the `project_test.py` file as a program, e.g. `python3 project_test.py`

```
$ python3 project_test.py
.........
----------------------------------------------------------------------
Ran 9 tests in 0.068s

OK
```

## References

[1] Y. PIRILDAK, “Mastering Tic-Tac-Toe with Minimax Algorithm,” Medium, May 13, 2020. https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f (accessed Dec. 10, 2022).__
[2] A. Vardi, “New minimax algorithm,” J Optim Theory Appl, vol. 75, no. 3, pp. 613–634, Dec. 1992, doi: 10.1007/BF00940496.__
[3] E. Nygren, “Design Specifications for an Interactive Teaching Tool for Game AI using Gomoku”.__
[4] Yu. (2019). AI Agent for Playing Gomoku. Retrieved December 9, 2022. https://stanford-cs221.github.io/autumn2019-extra/posters/14.pdf__
[5] H. Liao, “New heuristic algorithm to improve the Minimax for Gomoku artificial intelligence”.__
[6] “Minimax Improvements.” https://blog.theofekfoundation.org/artificial-intelligence/2015/12/18/minimax-improvements/ (accessed Dec. 17, 2022).__
