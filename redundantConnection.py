"""

LC: 684. Redundant Connection

https://leetcode.com/problems/redundant-connection/

Medium

Topics
Depth-First Search
Breadth-First Search
Union Find
Graph

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
610,110/909.7K
Acceptance Rate
67.1%

"""

class Solution:
    def findRedundantConnection(self,edges:list[list[int]])->list[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        size=[1]*(n+1)
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(a,b):
            pa,pb=find(a),find(b)
            if pa==pb:
                return False
            if size[pa]<size[pb]:
                parent[pa]=pb
                size[pb]+=size[pa]
            else:
                parent[pb]=pa
                size[pa]+=size[pb]
            return True
        for u,v in edges:
            if not union(u,v):
                return [u,v]
sol=Solution()
print(sol.findRedundantConnection(edges = [[1,2],[1,3],[2,3]]))
print(sol.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))