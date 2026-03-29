"""

LC: 407. Trapping Rain Water II

Hard

Topics
Array
Breadth-First Search
Heap (Priority Queue)
Matrix

Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

(fig)

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
240,529/380.6K
Acceptance Rate
63.2%

"""

import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []  # min-heap to process lowest boundary first

        # Add all boundary cells to the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        trapped = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        maxHeight = 0

        while heap:
            h, x, y = heapq.heappop(heap)
            maxHeight = max(maxHeight, h)

            # check all 4 neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # If neighbor is lower, water can be trapped
                    if heightMap[nx][ny] < maxHeight:
                        trapped += maxHeight - heightMap[nx][ny]
                    # Push neighbor into heap with its height
                    heapq.heappush(heap, (heightMap[nx][ny], nx, ny))

        return trapped
