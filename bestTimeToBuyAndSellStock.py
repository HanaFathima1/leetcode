

#brute Force
# class Solution:
#     def bestTimeToBuyAndSellStock(self, prices:list[int]) -> int:
#         n=len(prices)
#         max_profit=0
#         for i  in range(n-1):
#             for j in range(i+1,n):
#                 profit = prices[j]-prices[i]
#                 if profit>max_profit:
#                     max_profit=profit
#         return max_profit

# sol = Solution()
# print(sol.bestTimeToBuyAndSellStock([7,1,5,3,6,4]))

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