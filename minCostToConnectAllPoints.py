"""

LC: 1584. Min Cost to Connect All Points

Medium

Topics
Array
Union Find
Graph
Minimum Spanning Tree
Weekly Contest 206

Hint
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
435,720/621.9K
Acceptance Rate
70.1%

Hint 1
Connect each pair of points with a weighted edge, the weight being the manhattan distance between those points.
Hint 2
The problem is now the cost of minimum spanning tree in graph with above edges.

"""

class Solution:
    def minCostConnectPoints(self,points:list[list[int]])->int:
        n=len(points)
        edges=[]
        for i in range(n):
            for j in range(i+1,n):
                x1,y1=points[i]
                x2,y2=points[j]
                cost=abs(x1-x2)+abs(y1-y2)
                edges.append((cost,i,j))
        edges.sort()
        parent=[i for i in range(n)]
        size=[1]*n
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
                size[pb]+=size[pb]
            else:
                parent[pb]=pa
                size[pa]+=size[pb]
            return True
        mst_weighed=0
        edges_used=0
        for cost,u,v in edges:
            if union(u,v):
                mst_weighed+=cost
                edges_used+=1
                if edges_used==n-1:
                    break
        return mst_weighed
sol=Solution()
print(sol.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(sol.minCostConnectPoints(points = [[3,12],[-2,5],[-4,1]]))


"""
DRY RUN:
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Index mapping (VERY IMPORTANT):

scss
Copy code
0 → (0,0)
1 → (2,2)
2 → (3,10)
3 → (5,2)
4 → (7,0)
🔹 Step 1: Build all edges (Manhattan distance)
Formula:

Copy code
|x1 - x2| + |y1 - y2|
Compute pairwise edges:

Edge (i,j)	Distance
(0,1)	
(0,2)	
(0,3)	
(0,4)	
(1,2)	
(1,3)	
(1,4)	
(2,3)	
(2,4)	
(3,4)	

Edges list:

scss
Copy code
(cost, u, v)
🔹 Step 2: Sort edges by cost
After sorting:

scss
Copy code
(3, 1, 3)
(4, 0, 1)
(4, 3, 4)
(7, 0, 3)
(7, 0, 4)
(7, 1, 4)
(9, 1, 2)
(10,2, 3)
(13,0, 2)
(14,2, 4)
🔹 Step 3: Initialize DSU
ini
Copy code
parent = [0,1,2,3,4]
size   = [1,1,1,1,1]
Each node is its own component.

🔹 Step 4: Process edges (Kruskal)
✅ Edge (1,3) cost = 3
lua
Copy code
find(1)=1, find(3)=3 → different
Union them.

ini
Copy code
parent = [0,1,2,1,4]
size   = [1,2,1,1,1]
MST cost = 3
Edges used = 1

✅ Edge (0,1) cost = 4
lua
Copy code
find(0)=0, find(1)=1 → different
Union.

ini
Copy code
parent = [1,1,2,1,4]
size   = [1,3,1,1,1]
MST cost = 3 + 4 = 7
Edges used = 2

✅ Edge (3,4) cost = 4
scss
Copy code
find(3) → find(1) → 1
find(4) → 4 → different
Union.

ini
Copy code
parent = [1,1,2,1,1]
size   = [1,4,1,1,1]
MST cost = 7 + 4 = 11
Edges used = 3

❌ Edge (0,3) cost = 7
scss
Copy code
find(0) → 1
find(3) → 1
Same parent → cycle → SKIP

❌ Edge (0,4) cost = 7
lua
Copy code
find(0)=1, find(4)=1
Cycle → SKIP

❌ Edge (1,4) cost = 7
lua
Copy code
find(1)=1, find(4)=1
Cycle → SKIP

✅ Edge (1,2) cost = 9
lua
Copy code
find(1)=1, find(2)=2 → different
Union.

ini
Copy code
parent = [1,1,1,1,1]
size   = [1,5,1,1,1]
MST cost = 11 + 9 = 20
Edges used = 4 = n-1

STOP 🎯

✅ Final Answer
java
Copy code
Minimum cost = 20
"""

#–----------OR------------
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        sm=0
        visited=set()
        pq=[(0,0)]

        while len(visited)<n:
            cost, u= heapq.heappop(pq)
            if u in visited:continue
            visited.add(u)
            sm+=cost
            x1, y1 = points[u]
            for v in range(n):
                if v not in visited:
                    x2, y2 = points[v]
                    newCost = abs(x2-x1)+ abs(y2-y1)
                    heapq.heappush(pq, (newCost, v))
        return sm