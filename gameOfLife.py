"""

LC: 289. Game of Life

Medium

Topics
Array
Matrix
Simulation

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
646,649/889.4K
Acceptance Rate
72.7%

"""

"""
What does the question ask?

You are given a grid where:

1 = Live cell
0 = Dead cell

For each cell, count its 8 neighbors (horizontal, vertical, diagonal).

Apply these rules:

Live cell with fewer than 2 live neighbors → dies
Live cell with 2 or 3 live neighbors → survives
Live cell with more than 3 live neighbors → dies
Dead cell with exactly 3 live neighbors → becomes alive
Easy Approach (Using Extra Board)
Idea
Create a copy of the board.
For every cell:
Count live neighbors.
Apply the rules.
Store result in the copy.
Copy the result back to the original board.
"""

class Solution:
    def gameOfLife(self, board):
        
        rows = len(board)
        cols = len(board[0])

        # All 8 possible neighbor directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # ---------- First Pass ----------
        # Decide the future state of each cell
        # and mark the changes using special values

        for r in range(rows):
            for c in range(cols):

                live_neighbors = 0

                # Count live neighbors
                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    # Check if neighbor is inside the board
                    if 0 <= nr < rows and 0 <= nc < cols:

                        # Count cells that were originally alive
                        # 1  = alive and stays alive
                        # -1 = alive but will die
                        if board[nr][nc] == 1 or board[nr][nc] == -1:
                            live_neighbors += 1

                # Current cell is alive
                if board[r][c] == 1:

                    # Rule 1:
                    # Live cell with fewer than 2 live neighbors dies

                    # Rule 3:
                    # Live cell with more than 3 live neighbors dies

                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1   # alive -> dead

                # Current cell is dead
                else:

                    # Rule 4:
                    # Dead cell with exactly 3 live neighbors becomes alive

                    if live_neighbors == 3:
                        board[r][c] = 2    # dead -> alive

        # ---------- Second Pass ----------
        # Convert temporary markers to final values

        for r in range(rows):
            for c in range(cols):

                # Cell was alive and is now dead
                if board[r][c] == -1:
                    board[r][c] = 0

                # Cell was dead and is now alive
                elif board[r][c] == 2:
                    board[r][c] = 1
        return board
sol=Solution()
print(sol.gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
print(sol.gameOfLife(board = [[1,1],[1,0]]))


"""

Input
|       | 0 | 1 | 2 |
| ----- | - | - | - |
| **0** | 0 | 1 | 0 |
| **1** | 0 | 0 | 1 |
| **2** | 1 | 1 | 1 |
| **3** | 0 | 0 | 0 |

First Pass (Mark Changes)
Cell-by-Cell Analysis
| Cell  | Current Value | Live Neighbors | Rule Applied                      | New Mark |
| ----- | ------------- | -------------- | --------------------------------- | -------- |
| (0,0) | 0             | 1              | Dead, not 3 neighbors             | 0        |
| (0,1) | 1             | 1              | Alive, < 2 neighbors → dies       | -1       |
| (0,2) | 0             | 2              | Dead, not 3 neighbors             | 0        |
| (1,0) | 0             | 3              | Dead, exactly 3 neighbors → alive | 2        |
| (1,1) | 0             | 5              | Dead, not 3 neighbors             | 0        |
| (1,2) | 1             | 3              | Alive, survives                   | 1        |
| (2,0) | 1             | 1              | Alive, < 2 neighbors → dies       | -1       |
| (2,1) | 1             | 3              | Alive, survives                   | 1        |
| (2,2) | 1             | 2              | Alive, survives                   | 1        |
| (3,0) | 0             | 2              | Dead, not 3 neighbors             | 0        |
| (3,1) | 0             | 3              | Dead, exactly 3 neighbors → alive | 2        |
| (3,2) | 0             | 2              | Dead, not 3 neighbors             | 0        |

Board After First Pass
|       | 0  | 1  | 2 |
| ----- | -- | -- | - |
| **0** | 0  | -1 | 0 |
| **1** | 2  | 0  | 1 |
| **2** | -1 | 1  | 1 |
| **3** | 0  | 2  | 0 |


Remember:

| Value | Meaning      |
| ----- | ------------ |
| -1    | Alive → Dead |
| 2     | Dead → Alive |

Second Pass (Convert Markers)
Conversion Table
| Marker | Final Value |
| ------ | ----------- |
| -1     | 0           |
| 2      | 1           |

Final Board
|       | 0 | 1 | 2 |
| ----- | - | - | - |
| **0** | 0 | 0 | 0 |
| **1** | 1 | 0 | 1 |
| **2** | 0 | 1 | 1 |
| **3** | 0 | 1 | 0 |

Visualization
Original
0 1 0
0 0 1
1 1 1
0 0 0

↓

After Marking
0 -1 0
2  0 1
-1 1 1
0  2 0

↓

Final Answer
0 0 0
1 0 1
0 1 1
0 1 0
Complexity
| Operation   | Complexity |
| ----------- | ---------- |
| First Pass  | O(m × n)   |
| Second Pass | O(m × n)   |
| Space       | O(1)       |


"""