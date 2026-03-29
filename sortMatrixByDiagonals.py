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
                
            
        