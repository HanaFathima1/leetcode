"""

LC: 778. Swim in Rising Water

Hard

Topics
Array
Binary Search
Depth-First Search
Breadth-First Search
Union Find
Heap (Priority Queue)
Matrix
Weekly Contest 70

Hint
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

Example 1:


Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:


Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n2
Each value grid[i][j] is unique.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
285,939/437.7K
Acceptance Rate
65.3%

Hint 1
Use either Dijkstra's, or binary search for the best time T for which you can reach the end if you only step on squares at most T.

"""
import heapq
class Solution:
    def swimInRisingWater(self, grid:list[list[int]]) -> int:
        N = len(grid)
        visit = set() #visit is an empty set that will store visited coordinates (r, c) to prevent revisiting the same cell more than once (reduces duplicate pushes to the heap).
        minH = [[grid[0][0],0,0]]
        directions = [[0,1],[0,-1],[1,0],[-1,0]] #Defines the four 4-directional offsets: right, left, down, up. Used to generate neighbor coordinates.
        visit.add((0,0)) #Marks the start cell (0,0) as visited immediately so it won’t be pushed again.
        while minH: #Loop while there are entries in the heap. Each iteration processes the cell with the currently smallest required time.
            t,r,c = heapq.heappop(minH) #Pops the heap element with smallest time value and unpacks it into t (the time required to reach this cell), r (row), c (col).t represents the minimum possible water level required to have a path from start to this cell (according to already considered paths).
            if r==N-1 and c==N-1: #If the popped cell is the destination (N-1, N-1), return t. Why this is correct: because we always pop cells in increasing t order, the first time we pop the target we have the minimum possible t needed to reach it — same reasoning as Dijkstra’s correctness.
                return t
            for dr, dc in directions: #Iterate over the four possible neighbor direction offsets.
                neiR, neiC = r+dr, c+dc #Compute the neighbor coordinates (neiR, neiC).
                if (neiR<0 or neiC<0 or neiR==N or neiC==N or (neiR,neiC) in visit):
                    continue
                    # Boundary and visited checks:

                    # neiR<0 or neiC<0 — neighbor is outside the grid on the top/left.

                    # neiR==N or neiC==N — neighbor is outside on bottom/right (since valid indices are 0..N-1). (Using == N is fine because neiR can only end up at N at most; >= N would be equally correct.)

                    # (neiR,neiC) in visit — skip neighbors already discovered/pushed earlier.

                    # If any of these are true, continue to the next neighbor.
                visit.add((neiR,neiC))
                heapq.heappush(minH, [max(t,grid[neiR][neiC]),neiR,neiC]) #So this line computes the time it would take to move from the current cell (r, c) to its neighbor (neiR, neiC).
#Why we use max(t, grid[neiR][neiC])

# This is the key logic of the problem.

# Remember:

# Water level rises with time.

# You can only step into a cell if the water level ≥ that cell’s elevation.

# So when you are currently at time t:

# The water level has already reached height t.

# If the next cell’s elevation grid[neiR][neiC] is higher than t,
# you must wait longer — until water rises up to that elevation.

# Therefore, the earliest time you can reach that neighbor is:

# max(t, grid[neiR][neiC])


# If the next cell is lower or equal to your current water level, you can move immediately (so time stays t).
# If it’s higher, you must wait until the water rises high enough.
sol = Solution()
print(sol.swimInRisingWater(grid = [[0,2],[1,3]]))
print(sol.swimInRisingWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))