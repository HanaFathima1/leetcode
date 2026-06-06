"""

LC: 714. Best Time to Buy and Sell Stock with Transaction Fee

Medium

Topics
Staff
Array
Dynamic Programming
Greedy

Hint
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 

Constraints:

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
584,906/811.8K
Acceptance Rate
72.0%

Hint 1
Consider the first K stock prices. At the end, the only legal states are that you don't own a share of stock, or that you do. Calculate the most profit you could have under each of these two cases.

"""

#-------------CODE2----------------
class Solution:
    def maxProfit(self, prices:list[int], fee:int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            # Can Buy State
            dp[i][1] = max(
                -prices[i] + dp[i + 1][0],
                dp[i + 1][1]
            )

            # Holding State
            dp[i][0] = max(
                prices[i] - fee + dp[i + 1][1],
                dp[i + 1][0]
            )

        return dp[0][1]
    
    
#EXPLANATION

class Solution:
    def maxProfit(self, prices, fee):

        # Number of days
        n = len(prices)

        # Create DP table
        #
        # dp[i][1]
        # = Maximum profit from day i onwards
        #   when we CAN BUY a stock
        #
        # dp[i][0]
        # = Maximum profit from day i onwards
        #   when we are HOLDING a stock
        #
        # n+1 rows because we need a base case
        # after the last day.
        #
        dp = [[0] * 2 for _ in range(n + 1)]

        # Start from the last day and move backwards
        #
        # Why?
        #
        # dp[i] depends on dp[i+1]
        #
        # Therefore future states must already
        # be calculated.
        #
        for i in range(n - 1, -1, -1):

            # ==================================
            # CAN BUY STATE
            # ==================================
            #
            # We currently do NOT own a stock.
            #
            # We have 2 choices:
            #
            # Choice 1:
            # Buy stock today
            #
            # Cost = prices[i]
            #
            # After buying,
            # we move to HOLDING state.
            #
            # Profit:
            #
            # -prices[i]
            # +
            # future profit
            #
            dp[i][1] = max(

                # Buy today
                -prices[i] + dp[i + 1][0],

                # Skip today
                dp[i + 1][1]
            )

            # ==================================
            # HOLDING STATE
            # ==================================
            #
            # We already own a stock.
            #
            # We have 2 choices:
            #
            # Choice 1:
            # Sell stock today
            #
            # We gain:
            #
            # prices[i]
            #
            # But we must pay transaction fee.
            #
            # After selling,
            # we move back to CAN BUY state.
            #
            dp[i][0] = max(

                # Sell today
                prices[i] - fee + dp[i + 1][1],

                # Continue holding stock
                dp[i + 1][0]
            )

        # Start at:
        #
        # Day 0
        #
        # Initially:
        #
        # We do NOT own a stock.
        #
        # Therefore we are in
        # CAN BUY state.
        #
        return dp[0][1]
    
#-------------CODE2-------------------

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        buy, profit = prices[0] + fee, 0
        for price in prices[1:]:
            if price + fee < buy:
                buy = price + fee
            elif price > buy:
                profit += (price - buy)
                buy = price

        return profit
    
#EXPLANATION
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        # Number of days
        n = len(prices)

        # buy:
        # Effective buying cost
        #
        # We include the transaction fee while buying.
        #
        # Example:
        # price = 1
        # fee = 2
        #
        # Effective cost = 1 + 2 = 3
        #
        buy = prices[0] + fee

        # Total profit earned so far
        profit = 0

        # Start from the second price
        #
        # We already used prices[0]
        # to initialize buy.
        #
        for price in prices[1:]:

            # --------------------------------
            # CASE 1:
            # Found a cheaper buying opportunity
            # --------------------------------
            #
            # Example:
            #
            # Current buy cost = 8
            #
            # New price = 4
            # fee = 2
            #
            # New effective cost:
            #
            # 4 + 2 = 6
            #
            # Since 6 < 8,
            # it is better to buy here.
            #
            if price + fee < buy:

                # Update the minimum effective cost
                buy = price + fee

            # --------------------------------
            # CASE 2:
            # Selling is profitable
            # --------------------------------
            #
            # Example:
            #
            # buy = 3
            # price = 8
            #
            # Profit = 8 - 3 = 5
            #
            elif price > buy:

                # Add profit earned from selling
                profit += (price - buy)

                # Important trick:
                #
                # After selling,
                # set buy = current price
                #
                # This simulates:
                #
                # "selling and immediately buying again"
                #
                # It prevents paying the fee twice
                # when prices continue rising.
                #
                buy = price

        # Return total profit
        return profit
    
"""
Dry Run Table

For:

prices = [1,3,2,8,4,9]
fee = 2

Initial:

buy = 3
profit = 0
Price	Condition	Action	Buy	Profit
3	none	skip	3	0
2	none	skip	3	0
8	8 > 3	sell	8	5
4	4+2 < 8	cheaper buy	6	5
9	9 > 6	sell	9	8

Final:

Profit = 8
Complexity
Time

Loop runs once:

O(n)
Space

Only two variables:

O(1)

"""