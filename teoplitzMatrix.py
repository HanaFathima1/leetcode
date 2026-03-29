"""

LC: 766. Toeplitz Matrix

Easy

Topics
Array
Matrix
Weekly Contest 68

Hint
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99
 

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
416,296/599.8K
Acceptance Rate
69.4%

Hint 1
Check whether each value is equal to the value of it's top-left neighbor.

"""

class Solution:
    def isToeplitzMatrix(self, matrix:list[list[int]]) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        for i in range(1,R):
            for j in range(1,C):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True
sol = Solution()
print(sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(sol.isToeplitzMatrix([[1,2],[2,2]]))