"""

LC: 1091. Shortest Path in Binary Matrix

Medium

Topics
Array
Breadth-First Search
Matrix
Weekly Contest 141

Hint
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
792,705/1.6M
Acceptance Rate
50.9%

Hint 1
Do a breadth first search to find the shortest path.

"""

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self,grid:list[list[int]])->int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        q=deque()
        q.append((0,0,1))
        grid[0][0]=1
        while q:
            r,c,dist=q.popleft()
            if r==n-1 and c==n-1:
                return dist
            for dr, dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:
                    grid[nr][nc]=1
                    q.append((nr,nc,dist+1))
        return -1
sol=Solution()
print(sol.shortestPathBinaryMatrix(grid = [[0,1],[1,0]]))
print(sol.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]))
print(sol.shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]]))
        