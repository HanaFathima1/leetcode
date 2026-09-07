"""

LC: 518. Coin Change II

Medium

Topics
Array
Dynamic Programming
Knapsack Problem
Complete Knapsack

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The final answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,093,274/1.8M
Acceptance Rate
59.2%

"""

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]+=dp[i-coin]
        return dp[amount] 
sol=Solution()
print(sol.change(amount = 5, coins = [1,2,5]))


#explanation
class Solution:

    def change(self, amount: int, coins: List[int]) -> int:

        # dp[i] = number of ways to make amount i
        dp = [0] * (amount + 1)

        # There is exactly 1 way to make amount 0:
        # choose no coins
        dp[0] = 1

        # Consider each coin one by one
        for coin in coins:

            # Try to make every amount from coin to amount
            for i in range(coin, amount + 1):

                # Add the number of ways to make
                # (i - coin), because adding this coin
                # gives a way to make i
                dp[i] += dp[i - coin]

        # Number of combinations to make the target amount
        return dp[amount]
    
    
"""
Example Dry Run

Let's take the common example:

amount = 5
coins = [1, 2, 5]

We want to find:

How many different combinations can make 5?

The combinations are:

5
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

So the answer should be:

4
Step 1: Initial DP array
dp = [0] * 6

So:

Index:  0  1  2  3  4  5
dp:    [0, 0, 0, 0, 0, 0]

Then:

dp[0] = 1

becomes:

Index:  0  1  2  3  4  5
dp:    [1, 0, 0, 0, 0, 0]
Why dp[0] = 1?

Because there is one way to make 0:

choose nothing

This is important because it gives us the starting point for building combinations.

3. First Coin = 1
coin = 1

The loop is:

for i in range(1, 6):
i = 1
dp[1] += dp[1 - 1]
dp[1] += dp[0]

Currently:

dp[0] = 1

Therefore:

dp[1] = 1

Array:

[1, 1, 0, 0, 0, 0]

Meaning:

1 → [1]

One way.

i = 2
dp[2] += dp[2 - 1]
dp[2] += dp[1]

dp[1] = 1

Therefore:

dp[2] = 1
[1, 1, 1, 0, 0, 0]

One way:

1 + 1
i = 3
dp[3] += dp[2]

dp[2] = 1

So:

dp[3] = 1
[1, 1, 1, 1, 0, 0]
i = 4
dp[4] += dp[3]

So:

dp[4] = 1
[1, 1, 1, 1, 1, 0]
i = 5
dp[5] += dp[4]

So:

dp[5] = 1

Now:

[1, 1, 1, 1, 1, 1]

So far, using only coin 1, there is exactly one combination for every amount:

5 = 1+1+1+1+1
4. Second Coin = 2

Now:

coin = 2

Current:

[1, 1, 1, 1, 1, 1]

The loop starts from 2:

for i in range(2, 6):
i = 2
dp[2] += dp[2 - 2]
dp[2] += dp[0]
dp[2] = 1 + 1
      = 2

Array:

[1, 1, 2, 1, 1, 1]

The two combinations for 2:

1 + 1
2
i = 3
dp[3] += dp[3 - 2]
dp[3] += dp[1]
dp[3] = 1 + 1
      = 2
[1, 1, 2, 2, 1, 1]

Ways:

1 + 1 + 1
2 + 1
i = 4
dp[4] += dp[4 - 2]
dp[4] += dp[2]

dp[2] = 2

Therefore:

dp[4] = 1 + 2
      = 3
[1, 1, 2, 2, 3, 1]

Ways:

1+1+1+1
2+1+1
2+2
i = 5
dp[5] += dp[5 - 2]
dp[5] += dp[3]

dp[3] = 2

Therefore:

dp[5] = 1 + 2
      = 3
[1, 1, 2, 2, 3, 3]

Ways:

1+1+1+1+1
2+1+1+1
2+2+1
5. Third Coin = 5

Now:

coin = 5

Current:

[1, 1, 2, 2, 3, 3]

The loop:

for i in range(5, 6):

Only i = 5.

dp[5] += dp[5 - 5]

Therefore:

dp[5] += dp[0]
dp[5] = 3 + 1
dp[5] = 4

Final:

[1, 1, 2, 2, 3, 4]

Therefore:

return dp[5]

returns:

4


======Difference=====

|                         | Coin Change 1                  | Coin Change 2                        |
| ----------------------- | ------------------------------ | ------------------------------------ |
| Goal                    | Minimum coins                  | Number of combinations               |
| `dp[i]` means           | Minimum coins required for `i` | Number of ways to make `i`           |
| Initial value           | `∞`                            | `0`                                  |
| `dp[0]`                 | `0`                            | `1`                                  |
| Main operation          | `min()`                        | `+`                                  |
| Answer for `[1,2,5], 5` | `1`                            | `4`                                  |
| Order matters?          | Not relevant to minimum        | **No**                               |
| Example                 | `5`                            | `5`, `2+2+1`, `2+1+1+1`, `1+1+1+1+1` |

"""