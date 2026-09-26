"""

LC: 3446. Sort Matrix by Diagonals

Medium

Topics
Array
Sorting
Matrix
Weekly Contest 436

Hint
You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.
 

Example 1:

Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

Output: [[8,2,3],[9,6,7],[4,5,1]]

Explanation:



The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

[1, 8, 6] becomes [8, 6, 1].
[9, 5] and [4] remain unchanged.
The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

[7, 2] becomes [2, 7].
[3] remains unchanged.
Example 2:

Input: grid = [[0,1],[1,2]]

Output: [[2,1],[1,0]]

Explanation:



The diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0]. The other diagonals are already in the correct order.

Example 3:

Input: grid = [[1]]

Output: [[1]]

Explanation:

Diagonals with exactly one element are already in order, so no changes are needed.

 

Constraints:

grid.length == grid[i].length == n
1 <= n <= 10
-105 <= grid[i][j] <= 105
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
81,855/99.5K
Acceptance Rate
82.3%

Hint 1
Use a data structure to store all values in each diagonal.
Hint 2
Sort and replace them in the matrix.

"""

class Solution: 
    def sortMatrix(self, grid:list[list[int]]) -> list[list[int]]:
        n = len(grid)
        for i in range(n):
            tmp = [grid[j+i][j] for j in range(n-i)]
            tmp.sort(reverse=True)
            for j in range(n-i):
                grid[i+j][j] = tmp[j]
            
        for i in range(1,n):
            tmp = [grid[j][i+j] for j in range(n-i)]
            tmp.sort()
            for j in range(n-i):
                grid[j][i+j] = tmp[j]
        
        return grid

sol = Solution()
print(sol.sortMatrix([[1,7,3],[9,8,2],[4,5,6]]))  
print(sol.sortMatrix([[0,1],[1,2]]))   
print(sol.sortMatrix([[1]]))                 
                

#====another solution======         
def sortMatrix(grid):
    n=len(grid)
    diagonal=[]
    for start_row in range(n):
        diagonal=[]
        row=start_row
        col=0
        while row<n and col<n:
            diagonal.append(grid[row][col])
            row+=1
            col+=1
        diagonal.sort(reverse=True)
        row=start_row
        col=0
        for value in diagonal:
            grid[row][col]=value
            row+=1
            col+=1
    for start_col in range(1,n):
        diagonal=[]
        row=0
        col=start_col
        while row<n and col<n:
            diagonal.append(grid[row][col])
            row+=1
            col+=1
        diagonal.sort()
        row=0
        col=start_col
        for value in diagonal:
            grid[row][col]=value
            row+=1
            col+=1
    return grid
print(sortMatrix([[1,7,3],[9,8,2],[4,5,6]]))
        



#explanation:
def sortMatrix(grid):

    n = len(grid)  
    # n = number of rows/columns
    # The matrix is n × n


    # -----------------------------------------
    # PART 1:
    # Bottom-left triangle + main diagonal
    # These diagonals must be sorted DESCENDING
    # -----------------------------------------

    for start_row in range(n):
        # We start each diagonal from the FIRST COLUMN
        #
        # start_row will be:
        # 0 → diagonal starting at (0,0)
        # 1 → diagonal starting at (1,0)
        # 2 → diagonal starting at (2,0)
        # ...


        diagonal = []
        # Empty list to store all elements
        # belonging to the current diagonal


        row = start_row
        col = 0
        # Starting position of this diagonal
        #
        # col = 0 because we are starting
        # from the first column


        while row < n and col < n:
            # Continue while row and column
            # are inside the matrix

            diagonal.append(grid[row][col])
            # Take the current element
            # and put it into our diagonal list

            row += 1
            col += 1
            # Move diagonally ↘
            #
            # Example:
            # (0,0) → (1,1) → (2,2)


        diagonal.sort(reverse=True)
        # Sort this diagonal in DESCENDING order
        #
        # Example:
        # [1, 8, 6]
        #
        # becomes:
        # [8, 6, 1]


        row = start_row
        col = 0
        # Go back to the START of the diagonal
        #
        # We need to put the sorted values
        # back into the matrix


        for value in diagonal:
            # Take each sorted value one by one

            grid[row][col] = value
            # Put the sorted value back
            # into its diagonal position

            row += 1
            col += 1
            # Move diagonally ↘ again


    # -----------------------------------------
    # PART 2:
    # Top-right triangle
    # These diagonals must be sorted ASCENDING
    # -----------------------------------------

    for start_col in range(1, n):
        # Start from the TOP ROW
        #
        # range(1,n) starts from column 1
        # because column 0 was already processed
        #
        # Example:
        # (0,1), (0,2), ...


        diagonal = []
        # Empty list for the current diagonal


        row = 0
        col = start_col
        # Start from the top row
        # at the current column


        while row < n and col < n:
            # Continue while inside matrix

            diagonal.append(grid[row][col])
            # Store current diagonal element

            row += 1
            col += 1
            # Move diagonally ↘


        diagonal.sort()
        # Sort in ASCENDING order
        #
        # Example:
        # [7, 2]
        #
        # becomes:
        # [2, 7]


        row = 0
        col = start_col
        # Return to the beginning of this diagonal
        # so we can put the sorted values back


        for value in diagonal:
            # Take each sorted value

            grid[row][col] = value
            # Put it back into the matrix

            row += 1
            col += 1
            # Move to the next position
            # of the diagonal


    return grid
    # Return the completely sorted matrix      