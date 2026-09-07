"""

LC: 695. Max Area of Island

Medium

Topics
Staff
Array
Depth-First Search
Breadth-First Search
Union-Find
Matrix

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,309,834/1.8M
Acceptance Rate
74.2%

"""

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        maxArea=0
        rows=len(grid)
        cols=len(grid[0])
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==0:
                return 0
            grid[i][j]=0
            return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area=dfs(r,c)
                    maxArea=max(maxArea,area)
        return maxArea
sol=Solution()
print(sol.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                  [0,1,1,0,1,0,0,0,0,0,0,0,0],
                                  [0,1,0,0,1,1,0,0,1,0,1,0,0],
                                  [0,1,0,0,1,1,0,0,1,1,1,0,0],
                                  [0,0,0,0,0,0,0,0,0,0,1,0,0],
                                  [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                  [0,0,0,0,0,0,0,1,1,0,0,0,0]]))