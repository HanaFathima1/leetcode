"""

LC: 1039. Minimum Score Triangulation of Polygon

Medium

Topics
Array
Dynamic Programming
Weekly Contest 135

Hint
You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.

Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles.

You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles.

Return the minimum possible score that you can achieve with some triangulation of the polygon.

 

Example 1:



Input: values = [1,2,3]

Output: 6

Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

Example 2:



Input: values = [3,7,4,5]

Output: 144

Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.

Example 3:



Input: values = [1,3,1,4,1,5]

Output: 13

Explanation: The minimum score triangulation is 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.

 

Constraints:

n == values.length
3 <= n <= 50
1 <= values[i] <= 100
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
93,312/145.5K
Acceptance Rate
64.1%

Hint 1
Without loss of generality, there is a triangle that uses adjacent vertices A[0] and A[N-1] (where N = A.length). Depending on your choice K of it, this breaks down the triangulation into two subproblems A[1:K] and A[K+1:N-1].

"""

class Solutiuon:
    def minScoreTriangulation(self, values:list[int]) -> int:
        @lru_cache(None)
        def dp(i,j):
            if j<i+2:
                return 0
            res = float('inf')
            for k in range(i+1,j):
                res=min(res,values[i]*values[j]*values[k]+dp(i,k)+dp(k,j))
            return res
        return dp(0,len(values)-1)
sol = Solutiuon()
print(sol.minScoreTriangulation(values = [1,2,3]))
print(sol.minScoreTriangulation(values = [3,7,4,5]))
print(sol.minScoreTriangulation(values = [1,3,1,4,1,5]))

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        n = len(values)
        m = n

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for length in range(3,m+1):
            for i in range(n-length+1):
                j = i+length - 1
                dp[i][j] = float('inf')
                for k in range(i+1,j):
                    dp[i][j] = min(dp[i][j], values[i]*values[k]*values[j]+dp[i][k]+dp[k][j])

        
        return dp[0][n-1]
        