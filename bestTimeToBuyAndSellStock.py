"""

LC: 121. Best Time to Buy and Sell Stock

Easy

Topics
Array
Dynamic Programming

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
8,100,249/14.2M
Acceptance Rate
56.9%

"""

#brute Force
class Solution:
    def bestTimeToBuyAndSellStock(self, prices:list[int]) -> int:
        n=len(prices)
        max_profit=0
        for i  in range(n-1):
            for j in range(i+1,n):
                profit = prices[j]-prices[i]
                if profit>max_profit:
                    max_profit=profit
        return max_profit

sol = Solution()
print(sol.bestTimeToBuyAndSellStock([7,1,5,3,6,4]))

#Two Pointers
class Solution:
    def maxProfit(self, prices):
        l, r = 0, 1    #l-buy r-sell
        maxP = 0
        while r<(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))