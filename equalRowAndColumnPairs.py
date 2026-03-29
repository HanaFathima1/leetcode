"""

LC: 2352. Equal Row and Column Pairs

Medium

Topics
Array
Hash Table
Matrix
Simulation
Weekly Contest 303

Hint
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
371,663/525.5K
Acceptance Rate
70.7%

Hint 1
We can use nested loops to compare every row against every column.
Hint 2
Another loop is necessary to compare the row and column element by element.
Hint 3
It is also possible to hash the arrays and compare the hashed values instead.

"""

class Solution:
    def equalPairs(self,grid:list[list[int]]) -> int:
        n=len(grid)
        rows = [tuple(r) for r in grid]
        cols = [tuple(grid[r][c] for r in range(n)) for c in range(n)]
        return sum(cols.count(r) for r in rows)
sol = Solution()
print(sol.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]))
print(sol.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))

#-----------------

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        rows = Counter(map(tuple, grid))
        return sum(rows[col] for col in zip(*grid))