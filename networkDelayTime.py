"""

LC: 743. Network Delay Time

Medium

Topics
Senior
Depth-First Search
Breadth-First Search
Graph Theory
Heap (Priority Queue)
Shortest Path
Weekly Contest 62

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
946,827/1.5M
Acceptance Rate
61.2%

Hint 1
We visit each node at some time, and if that time is better than the fastest time we've reached this node, we travel along outgoing edges in sorted order. Alternatively, we could use Dijkstra's algorithm.

"""


import heapq
from collections import defaultdict

class Solution:
    def networkDwelayTime(self,times,n,k):
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        dist = [float('inf')]*(n+1)
        dist[k]=0
        heap=[(0,k)]
        while heap:
            time,node=heapq.heappop(heap)
            if time>dist[node]:
                continue
            for nei,wt in graph[node]:
                if dist[node]+wt<dist[nei]:
                    dist[nei]=dist[node]+wt
                    heapq.heappush(heap,(dist[nei],nei))
        max_dist=max(dist[1:])
        return max_dist if max_dist!=float('inf') else -1
sol=Solution()
print(sol.networkDwelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
                
                
    