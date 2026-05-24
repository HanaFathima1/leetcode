"""

LC: 746. Min Cost Climbing Stairs

Easy

Topics
Mid Level
Array
Dynamic Programming
Weekly Contest 63

Hint
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,764,509/2.6M
Acceptance Rate
68.3%

Hint 1
Build an array dp where dp[i] is the minimum cost to climb to the top starting from the ith staircase.
Hint 2
Assuming we have n staircase labeled from 0 to n - 1 and assuming the top is n, then dp[n] = 0, marking that if you are at the top, the cost is 0.
Hint 3
Now, looping from n - 1 to 0, the dp[i] = cost[i] + min(dp[i + 1], dp[i + 2]). The answer will be the minimum of dp[0] and dp[1]

"""

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        # Find total number of stairs
        n = len(cost)

        # Create a DP array of size n
        # Initially fill it with 0
        # dp[i] will store:
        # minimum cost required to reach stair i
        dp = [0] * n

        # Base Case:
        # Minimum cost to reach first stair
        # is the cost of first stair itself
        dp[0] = cost[0]

        # Base Case:
        # Minimum cost to reach second stair
        # is the cost of second stair itself
        dp[1] = cost[1]

        # Start loop from stair index 2
        # because first two values are already initialized
        for i in range(2, n):

            # To reach current stair i,
            # we can come either from:
            #   1. previous stair (i-1)
            #   2. two stairs before (i-2)
            #
            # Choose the minimum cost path
            # and add current stair cost
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        # Final answer:
        # We can reach the TOP either from:
        #   last stair (n-1)
        #   OR second last stair (n-2)
        #
        # So return the minimum of both
        return min(dp[n-1], dp[n-2])
    
sol = Solution()
print(sol.minCostClimbingStairs(cost = [10,15,20]))
print(sol.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))