"""

LC: 210. Course Schedule II

Solved

Medium

Topics
Depth-First Search
Breadth-First Search
Graph
Topological Sort

Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,583,688/2.9M
Acceptance Rate
54.7%

Hint 1
This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Hint 2
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Hint 3
Topological sort could also be done via BFS.

"""

from typing import List
from collections import deque,defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        q=deque([i for i in range(numCourses) if indegree[i]==0])
        topo=[]
        while q:
            node=q.popleft()
            topo.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(topo)!=numCourses:
            return []
        return topo
    
sol=Solution()
print(sol.findOrder(numCourses = 2, prerequisites = [[1,0]]))
print(sol.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
print(sol.findOrder(numCourses = 1, prerequisites = []))