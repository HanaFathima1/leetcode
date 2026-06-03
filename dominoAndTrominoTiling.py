"""

LC: 790. Domino and Tromino Tiling

Medium

Topics
Staff
Dynamic Programming
Weekly Contest 73

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are shown above.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 1000
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
283,848/552.8K
Acceptance Rate
51.3%

"""
#-----------------------------------------------------------------------#
"""

LeetCode 790 asks:

How many different ways can you completely fill a 2 × n rectangle using 2 × 1 dominoes and L-shaped trominoes without leaving any empty spaces?

"""

class Solution:
    def numTilings(selff, n:int) -> int:
        MOD = 10**9 + 7
        if n==1:
            return 1
        if n==2:
            return 2
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=(2 * dp[i-1] + dp[i-3]) % MOD
        return dp[n]
sol=Solution()
print(sol.numTilings(n = 3))
print(sol.numTilings(n = 1))


#---------------------------EXPLANATION----------------------------------------

class Solution:
    def numTilings(self, n: int) -> int:

        # The answer can become very large.
        # LeetCode asks us to return the answer modulo (10^9 + 7).
        MOD = 10**9 + 7

        # Base Case:
        # For a 2 x 1 board:
        #
        # □
        # □
        #
        # Only one vertical domino can be placed.
        #
        # Ways = 1
        if n == 1:
            return 1

        # Base Case:
        # For a 2 x 2 board:
        #
        # Way 1:
        # ■ ■
        # ■ ■
        # (two vertical dominoes)
        #
        # Way 2:
        # ■■
        # ■■
        # (two horizontal dominoes)
        #
        # Ways = 2
        if n == 2:
            return 2

        # dp[i]
        #
        # Meaning:
        # Number of ways to completely tile
        # a 2 x i board.
        #
        # Example:
        #
        # dp[3]
        # = ways to tile a 2 x 3 board
        #
        dp = [0] * (n + 1)

        # Base Cases

        # dp[0]
        #
        # Empty board.
        #
        # There is exactly one way:
        # Do nothing.
        #
        # This is a common DP base case.
        dp[0] = 1

        # 2 x 1 board
        #
        # One vertical domino.
        #
        # Ways = 1
        dp[1] = 1

        # 2 x 2 board
        #
        # Two ways:
        # 1. Two vertical dominoes
        # 2. Two horizontal dominoes
        #
        # Ways = 2
        dp[2] = 2

        # Fill DP table from left to right.
        #
        # Why?
        #
        # dp[i] depends on:
        # dp[i-1]
        # dp[i-3]
        #
        # So smaller answers must already exist.
        for i in range(3, n + 1):

            # Recurrence Relation:
            #
            # dp[i]
            # =
            # 2 * dp[i-1]
            # +
            # dp[i-3]
            #
            # This formula comes from analyzing
            # all possible domino and tromino placements.
            #
            # dp[i-1]
            #
            # Represents extending arrangements
            # of a smaller board.
            #
            # The factor 2 appears because
            # tromino configurations create
            # additional symmetric possibilities.
            #
            # dp[i-3]
            #
            # Represents configurations that
            # consume three columns using trominoes.
            #
            # Apply modulo to keep numbers small.
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        # dp[n]
        #
        # Means:
        # Number of ways to tile the entire
        # 2 x n board.
        #
        # This is exactly what the problem asks.
        return dp[n]
   
"""

Dry Run (n = 5)
Initial DP
dp = [1, 1, 2, 0, 0, 0]
i = 3
dp[3] = 2 * dp[2] + dp[0]
dp[3] = 2 * 2 + 1
dp[3] = 5

DP:

[1, 1, 2, 5, 0, 0]
i = 4
dp[4] = 2 * dp[3] + dp[1]
dp[4] = 2 * 5 + 1
dp[4] = 11

DP:

[1, 1, 2, 5, 11, 0]
i = 5
dp[5] = 2 * dp[4] + dp[2]
dp[5] = 2 * 11 + 2
dp[5] = 24

DP:

[1, 1, 2, 5, 11, 24]
Return
return dp[5]

Answer:

24

"""

#-------------------------------------------------------------------


"""

HOW TO FORM EQUATIONS?


This is the most important DP skill.

Most students try to memorize equations like:

dp[i] = dp[i-1] + dp[i-2]

or

dp[i] = min(dp[i], 1 + dp[i-coin])

But interviewers want to know:

How did you derive the recurrence relation?

The Universal DP Formula Derivation Method

Whenever you see a DP problem:

Step 1: Define the State

Ask:

What does dp[i] mean?

Example: Coin Change

dp[i]

means:

Minimum coins needed to make amount i

Example: Climbing Stairs

dp[i]

means:

Ways to reach stair i

Without a proper state definition, you cannot derive the equation.

Step 2: Stand at the Current State

Imagine you're trying to calculate:

dp[i]

Ask:

How can I reach this state?

This is the secret.

Example 1: Climbing Stairs

State:

dp[i]

Meaning:

Ways to reach stair i

How can I reach stair i?

Only two ways:

From stair i-1
From stair i-2

Therefore:

dp[i] = dp[i-1] + dp[i-2]

Because all ways from both sources contribute.

Example 2: Coin Change

State:

dp[i]

Meaning:

Minimum coins needed for amount i

Suppose:

i = 11

How can I make 11?

Take:

coin 1
coin 2
coin 5

If I take coin 5:

Remaining:

11 - 5 = 6

Answer:

1 + dp[6]

If I take coin 2:

1 + dp[9]

If I take coin 1:

1 + dp[10]

Take minimum:

dp[i]=min(1+dp[i−coin])

Notice:

We didn't memorize.

We asked:

How can I make amount i?
Example 3: Decode Ways

State:

dp[i]

Meaning:

Ways to decode from index i

Current string:

226
^
i

Choices:

Take 1 digit
Take 2 digits

Take 1 digit:

dp[i+1]

Take 2 digits:

dp[i+2]

Total ways:

dp[i]=dp[i+1]+dp[i+2]

Again:

We asked:

What choices do I have?
The General DP Recipe

Every recurrence comes from:

State
+
Choices
=
Recurrence
For Minimum Problems

Examples:

Coin Change
Min Cost Climbing Stairs

Use:

Take minimum choice

Template:

dp[state] = min(all possible choices)
For Maximum Problems

Examples:

House Robber
Knapsack

Template:

dp[state] = max(all possible choices)
For Count Ways Problems

Examples:

Climbing Stairs
Decode Ways
Unique Paths

Template:

dp[state] = sum(all possible choices)
Now About 790

You asked specifically about:

dp[i]=2dp[i−1]+dp[i−3]

This equation is NOT obvious.

In fact, most people cannot derive it directly.

The actual derivation starts with two states:

full[i]

and

gap[i]

Where:

full[i]

means:

Fully tiled 2 × i board

And:

gap[i]

means:

Board with one missing corner cell

From board analysis, we get:

gap[i]=gap[i−1]+full[i−2]

and

full[i]=full[i−1]+full[i−2]+2⋅gap[i−1]

Then mathematicians simplify those two equations and eliminate gap.

The final result becomes:

dp[i]=2dp[i−1]+dp[i−3]

So for LeetCode 790:

❌ Don't try to derive the final equation directly.

✅ First derive the states and transitions.

The final equation is just an optimization.

The DP Equation Derivation Checklist

Whenever you face a new DP problem:

1. What does dp[state] mean?

2. What choices do I have at this state?

3. What smaller states do those choices lead to?

4. Am I finding:
   - Minimum?
   - Maximum?
   - Count of ways?

5. Combine the choices:
   - min(...)
   - max(...)
   - sum(...)

"""