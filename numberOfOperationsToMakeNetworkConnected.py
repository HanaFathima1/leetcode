"""

LC: 1319. Number of Operations to Make Network Connected
Medium
Topics
premium lock icon
Companies
Hint
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
 

Constraints:

1 <= n <= 105
1 <= connections.length <= min(n * (n - 1) / 2, 105)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
336,922/511.4K
Acceptance Rate
65.9%

Hint 1
As long as there are at least (n - 1) connections, there is definitely a way to connect all computers.
Hint 2
Use DFS to determine the number of isolated computer clusters.

"""

class Solution:
    def makeConnected(self,n:int,connections:list[list[int]])->list[int]:
        if len(connections) < n-1:
            return -1
        parent=[i for i in range(n)]
        size=[1]*n
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(a,b):
            pa,pb=find(a),find(b)
            if pa==pb:
                return
            if size[pa]<size[pb]:
                parent[pa]=pb
                size[pb]+=size[pa]
            else:
                parent[pb]=pa
                size[pa]+=size[pb]
        for u,v in connections:
            union(u,v)
        components=0
        for i in range(n):
            if find(i)==i:
                components+=1
        return components-1
sol=Solution()
print(sol.makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]]))
print(sol.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]))
print(sol.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]))
            
        
    