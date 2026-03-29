"""

LC: 399. Evaluate Division

Medium

Topics:
Array
String
Depth-First Search
Breadth-First Search
Union-Find
Graph Theory
Shortest Path

Hint
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
679,954/1.1M
Acceptance Rate
63.9%

Hint 1
Do you recognize this as a graph problem?

"""

from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # Step 1: Build graph
        # graph[a] = [(b, value), ...]
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))        # a -> b = val
            graph[b].append((a, 1 / val))    # b -> a = 1/val

        # Step 2: DFS function to find path value
        def dfs(src, dst, visited):
            # If variable not in graph, cannot evaluate
            if src not in graph:
                return -1.0

            # If source equals destination, ratio is 1
            if src == dst:
                return 1.0

            visited.add(src)

            # Try all neighbors
            for nei, weight in graph[src]:
                if nei not in visited:
                    res = dfs(nei, dst, visited)
                    if res != -1.0:
                        return weight * res   # multiply along the path

            return -1.0

        # Step 3: Process queries
        results = []

        for src, dst in queries:
            results.append(dfs(src, dst, set()))

        return results
