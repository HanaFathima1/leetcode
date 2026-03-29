"""

LC: 867. Transpose Matrix

Easy

Topics
Array
Matrix
Simulation
Weekly Contest 92

Hint
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, 
switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
516,235/690.6K
Acceptance Rate
74.7%

Hint 1
We don't need any special algorithms to do this. You just need to know what the transpose of a matrix looks like. Rows become columns and vice versa!

"""

class Solution:
    def transpose(self, matrix:list[list[int]]) -> list[list[int]]:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
sol = Solution()
print(sol.transpose([[1,2,3],[4,5,6]]))
print(sol.transpose([[1,2,3],[4,5,6],[7,8,9]]))