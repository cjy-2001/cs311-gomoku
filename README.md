# CS311 Final Project - Gomoku Algorithm

Gomoku, or five in a row, is an abstract strategy board game where two players place a
stone of their color on a 15x15 empty intersection. The winner is the first whose stones form an unbroken chain of five horizontally, vertically, or diagonally.
 
Our goal is to design an agent that plays with a human player in real time. We intend to optimize both search efficiency and the chances of winning by implementing a minimax tree model and to explore how pruning or heuristic functions may improve the model performance. Some ways to evaluate the model performance include: if the agent will always win given a mistake firstly made by the human player, the number of steps it takes to beat the opponent, and the duration of each search.

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

