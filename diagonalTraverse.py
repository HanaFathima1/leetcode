"""

LC: 498. Diagonal Traverse

Medium

Topics
Principal
Array
Matrix
Simulation

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
579,513/858.8K
Acceptance Rate
67.5%

"""

class Solution:
    def findDiagonalOrder(self, matrix: list[list[int]]) -> list[int]:
        # If matrix is empty
        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        result = []

        # Total number of diagonals
        for d in range(rows + cols - 1):

            diagonal = []

            # Find all elements belonging to this diagonal
            for row in range(rows):

                col = d - row

                # Check whether the column is valid
                if 0 <= col < cols:
                    diagonal.append(matrix[row][col])

            # Reverse even-numbered diagonals
            if d % 2 == 0:
                diagonal.reverse()

            # Add diagonal to answer
            result.extend(diagonal)

        return result
sol=Solution()
print(sol.findDiagonalOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
        


"""
Let's dry run it

Matrix:

1  2  3
4  5  6
7  8  9
d = 0

We calculate:

row = 0
col = 0 - 0 = 0

So:

[1]

Since d is even:

diagonal.reverse()

Still:

[1]

Result:

[1]
d = 1
row = 0
col = 1 - 0 = 1

→ 2

row = 1
col = 1 - 1 = 0

→ 4

So:

diagonal = [2,4]

d is odd, so don't reverse.

Result:

[1,2,4]
d = 2
row = 0
col = 2

→ 3

row = 1
col = 1

→ 5

row = 2
col = 0

→ 7

So initially:

[3,5,7]

But d = 2 is even.

Reverse:

[7,5,3]

Result:

[1,2,4,7,5,3]
d = 3

Valid cells:

row = 1, col = 2 → 6
row = 2, col = 1 → 8

So:

[6,8]

Result:

[1,2,4,7,5,3,6,8]
d = 4

Only:

row = 2
col = 2

→ 9

Final:

[1,2,4,7,5,3,6,8,9]
"""