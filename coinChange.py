"""

LC: 322. Coin Change

Medium

Topics
Array
Dynamic Programming
Breadth-First Search

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
2,883,656/5.9M
Acceptance Rate
48.5%

"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        
        min_count = float('inf')
        
        for coin in coins:
            res = self.coinChange(coins, amount - coin)
            if res != -1:
                min_count = min(min_count, 1 + res)
                
        return min_count if min_count != float('inf') else -1
  
  
#-------------------------------#  
def solve(coins,amount,dn):
    if amount==0:
        return(1)
    if dn==0:
        return(0)
    if coins[dn-1]>amount:
        return (coins,amount,dn-1)
    return solve(coins, amount-coins[dn-1],dn)+solve(coins,amount,dn-1)
coins=[1,2,3]
amount=10
print(solve(coins,amount,len(coins)))
   
   
#------------------------------------# 
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[i] will be storing the minimum number of coins required for amount i
        # amount + 1 is a placeholder for infinity
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    
        return dp[amount] if dp[amount] != float('inf') else -1


#explanation of above code:

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        # dp[i]
        #
        # Meaning:
        # Minimum number of coins needed to make amount i.
        #
        # Example:
        #
        # dp[7]
        # =
        # Minimum coins required to make amount 7.
        #
        # Initially, we don't know the answer for any amount.
        #
        # So we fill the entire DP array with infinity.
        #
        # Why infinity?
        #
        # Because we are looking for a MINIMUM.
        #
        # Any valid answer will be smaller than infinity.
        dp = [float('inf')] * (amount + 1)

        # Base Case:
        #
        # Amount = 0
        #
        # To make amount 0,
        # we need 0 coins.
        #
        # Example:
        #
        # Amount = 0
        # Coins needed = 0
        dp[0] = 0

        # Build answers from smaller amounts to larger amounts.
        #
        # i represents the current amount we are trying to form.
        #
        # Example:
        #
        # i = 1
        # i = 2
        # i = 3
        # ...
        # i = amount
        for i in range(1, amount + 1):

            # Try every coin for the current amount.
            #
            # Example:
            #
            # coins = [1,2,5]
            #
            # For amount 11:
            #
            # Try coin 1
            # Try coin 2
            # Try coin 5
            for coin in coins:

                # Check whether the coin can be used.
                #
                # Example:
                #
                # amount = 3
                # coin = 5
                #
                # 3 - 5 = -2
                #
                # Negative amount is impossible.
                #
                # So we only proceed when:
                #
                # remaining amount >= 0
                if i - coin >= 0:

                    # Transition:
                    #
                    # Suppose:
                    #
                    # Current amount = i
                    #
                    # We decide to use this coin.
                    #
                    # Then:
                    #
                    # Remaining amount
                    # =
                    # i - coin
                    #
                    # Example:
                    #
                    # i = 11
                    # coin = 5
                    #
                    # Remaining amount = 6
                    #
                    # If dp[6] already tells us the minimum
                    # coins needed for amount 6,
                    # then:
                    #
                    # 1 (current coin)
                    # +
                    # dp[6]
                    #
                    # gives one possible answer for amount 11.
                    #
                    # We compare it with the current best answer
                    # stored in dp[i].
                    #
                    # Formula:
                    #
                    # dp[i]
                    # =
                    # min(
                    #     current best answer,
                    #     1 + answer of remaining amount
                    # )
                    #
                    dp[i] = min(
                        dp[i],                  # current best answer
                        1 + dp[i - coin]        # use current coin
                    )

        # After filling the DP table:
        #
        # dp[amount]
        #
        # stores the minimum number of coins needed
        # for the target amount.
        #
        # Example:
        #
        # coins = [1,2,5]
        # amount = 11
        #
        # dp[11] = 3
        #
        # because:
        #
        # 11 = 5 + 5 + 1
        #
        # If amount cannot be formed,
        # dp[amount] remains infinity.
        #
        # In that case return -1.
        #
        # NOTE:
        # Since this code uses float('inf'),
        # a safer check is:
        #
        # if dp[amount] == float('inf'):
        #     return -1
        #
        return dp[amount] if dp[amount] != float('inf') else -1