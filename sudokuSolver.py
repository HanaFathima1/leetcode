"""

LC: 37. Sudoku Solver

Hard

Topics
Array
Hash Table
Backtracking
Matrix

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
880,851/1.4M
Acceptance Rate
65.0%

"""

class Solution:
    def solveSudoku(self, board:list[list[int]]) -> bool:
        def isValid(r,c,ch):
            #check row
            for j in range(9):
                if board[r][j] == ch:
                    return False
            #check col
            for i in range(9):
                if board[i][c] == ch:
                    return False
            #check box
            br, bc = (r//3)*3, (c//3)*3
            for i in range(3):
                for j in range(3):
                    if board[br+i][bc+j] == ch:
                        return False
            return True
        
        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for ch in "123456789":
                            if isValid(r,c,ch):
                                board[r][c] = ch
                                if backtrack():
                                    return True
                                board[r][c] = "."
                        return False
            return True
        backtrack()
        return board
sol = Solution()
print(sol.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
                         
                         
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Fill the sets with existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    ch = board[r][c]
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[(r // 3) * 3 + (c // 3)].add(ch)

        def backtrack(r=0, c=0):
            if r == 9:  # solved all rows
                return True
            if c == 9:  # go to next row
                return backtrack(r + 1, 0)
            if board[r][c] != ".":
                return backtrack(r, c + 1)

            for ch in "123456789":
                box_idx = (r // 3) * 3 + (c // 3)
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_idx]:
                    # place number
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_idx].add(ch)

                    if backtrack(r, c + 1):
                        return True

                    # undo choice
                    board[r][c] = "."
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_idx].remove(ch)

            return False

        backtrack()                                   
                                
                                