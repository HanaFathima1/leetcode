"""

LC: 207. Course Schedule

Medium

Topics
Depth-First Search
Breadth-First Search
Graph
Topological Sort

Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,394,828/4.7M
Acceptance Rate
50.5%

Hint 1
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Hint 2
Topological Sort via DFS - A great tutorial explaining the basic concepts of Topological Sort.
Hint 3
Topological sort could also be done via BFS.

"""

from typing import List
from collections import deque,defaultdict

class Solution:
    def canFinish(self, numCourses:int, prerequisites:List[List[int]])->bool:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        q=deque([i for i in range(numCourses) if indegree[i]==0])
        topo=[]
        while q:
            node=q.popleft()
            topo.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return len(topo)==numCourses
sol=Solution()
print(sol.canFinish(numCourses = 2, prerequisites = [[1,0]]))
print(sol.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))   
        