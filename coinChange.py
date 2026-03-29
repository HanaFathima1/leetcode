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
    
#
    
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[i] will be storing the minimum number of coins required for amount i
        # amount + 1 is a placeholder for infinity
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1
    

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
