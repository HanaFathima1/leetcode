"""

LC: 62. Unique Paths

Medium

Topics
Math
Dynamic Programming
Combinatorics

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
2,879,496/4.3M
Acceptance Rate
66.9%

"""

# Tabulation Code
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * n for _ in range(m)]

        # Destination
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):

            for j in range(n-1, -1, -1):

                if i == m-1 and j == n-1:
                    continue

                down = 0
                right = 0

                if i + 1 < m:
                    down = dp[i+1][j]

                if j + 1 < n:
                    right = dp[i][j+1]

                dp[i][j] = down + right

        return dp[0][0]
sol = Solution()
print(sol.uniquePaths(m = 3, n = 7))
print(sol.uniquePaths(m = 3, n = 2))


# Code With Comments
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp[i][j]
        #
        # Number of ways to reach destination
        # from cell (i,j)
        #
        dp = [[0] * n for _ in range(m)]

        # Base Case
        #
        # Destination cell
        #
        # There is exactly one way
        # to stay at destination.
        #
        dp[m-1][n-1] = 1

        # Fill from bottom-right
        #
        for i in range(m-1, -1, -1):

            for j in range(n-1, -1, -1):

                # Skip destination cell
                if i == m-1 and j == n-1:
                    continue

                down = 0
                right = 0

                # Move down
                if i + 1 < m:
                    down = dp[i+1][j]

                # Move right
                if j + 1 < n:
                    right = dp[i][j+1]

                # Total ways
                dp[i][j] = down + right

        return dp[0][0]

"""
Easy Dry Run:

Input:

m = 3
n = 3

Grid:

? ? ?
? ? ?
? ? 1

Destination:

dp[2][2] = 1
Row 2
? ? 1

Cell:

(2,1)

Can only go right.

dp[2][1] = 1

Cell:

(2,0)
dp[2][0] = 1

Grid:

? ? ?
? ? ?
1 1 1
Row 1

Cell:

(1,2)

Can only go down.

dp[1][2] = 1

Grid:

? ? ?
? ? 1
1 1 1

Cell:

(1,1)
dp[1][1]
=
dp[2][1]
+
dp[1][2]
=
1 + 1
=
2

Grid:

? ? ?
? 2 1
1 1 1

Cell:

(1,0)
=
1 + 2
=
3

Grid:

? ? ?
3 2 1
1 1 1
Row 0

Cell:

dp[0][2]
=
1

Cell:

dp[0][1]
=
2 + 1
=
3

Cell:

dp[0][0]
=
3 + 3
=
6

Final:

6 3 1
3 2 1
1 1 1

# Complexity
Time Complexity  : O(m × n)

Space Complexity : O(m × n)

"""