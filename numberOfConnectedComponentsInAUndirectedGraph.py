"""

LC: 323. Number of Connected Components in an Undirected Graph

Medium 

There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2


Recommended Time & Space Complexity
You should aim for a solution as good or better than O(V + E) time and O(V + E) space, where V is the number vertices and E is the number of edges in the graph.


Hint 1
Assume there are no edges initially, so we have n components, as there are that many nodes given. Now, we should add the given edges between the nodes. Can you think of an algorithm to add the edges between the nodes? Also, after adding an edge, how do you determine the number of components left?


Hint 2
We can use the Union-Find (DSU) algorithm to add the given edges. For simplicity, we use Union-Find by size, where we merge the smaller component into the larger one. The Union-Find algorithm inserts the edge only between two nodes from different components. It does not add the edge if the nodes are from the same component. How do you find the number of components after adding the edges? For example, consider that nodes 0 and 1 are not connected, so there are initially two components. After adding an edge between these nodes, they become part of the same component, leaving us with one component.


Hint 3
We create an object of the DSU and initialize the result variable res = n, which indicates that there are n components initially. We then iterate through the given edges. For each edge, we attempt to connect the nodes using the union function of the DSU. If the union is successful, we decrement res; otherwise, we continue. Finally, we return res as the number of components.

"""

from collections import defaultdict

class Solution:
    def countComponents(self,n:int,edges:list[list[int]])->int:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        components=0
        visited=set()
        def dfs(node):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                components+=1
        return components
sol = Solution()
print(sol.countComponents(n=3,edges=[[0,1], [0,2]]))
print(sol.countComponents(n=6,edges=[[0,1], [1,2], [2,3], [4,5]]))
                
                