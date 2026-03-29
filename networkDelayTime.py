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
                
                
    