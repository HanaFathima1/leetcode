"""

LC: 547. Number of Provinces

Medium

Topics
Depth-First Search
Breadth-First Search
Union Find
Graph

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,377,074/2M
Acceptance Rate
69.5%

"""

from collections import deque
class Solution:
    def findCircleNum(self,isConnected:list[list[int]])->int:
        n=len(isConnected)
        visited=set()
        provinces=0
        for i in range(n):
            if i not in visited:
                provinces+=1
                queue=deque([i])
                while queue:
                    city=queue.popleft()
                    for neighbor in range(n):
                        if isConnected[city][neighbor]==1 and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        return provinces
sol = Solution()
print(sol.findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))
print(sol.findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]))


#-----------OR----------

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n   # 0 means not visited
        count = 0           # number of provinces

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = 1
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1   # after exploring one full province
        return count
