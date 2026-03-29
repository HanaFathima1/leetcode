"""

LC: 3100. Water Bottles II

(see question in leet code)

Medium

Topics
Math
Simulation
Weekly Contest 391

Hint
You are given two integers numBottles and numExchange.

numBottles represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:

Drink any number of full water bottles turning them into empty bottles.
Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.
Note that you cannot exchange multiple batches of empty bottles for the same value of numExchange. For example, if numBottles == 3 and numExchange == 1, you cannot exchange 3 empty water bottles for 3 full bottles.

Return the maximum number of water bottles you can drink.

 

Example 1:


Input: numBottles = 13, numExchange = 6
Output: 15
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
Example 2:


Input: numBottles = 10, numExchange = 3
Output: 13
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
 

Constraints:

1 <= numBottles <= 100 
1 <= numExchange <= 100
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
105,778/141K
Acceptance Rate
75.0%

Hint 1
Simulate the process step by step. At each step, drink numExchange bottles of water then exchange them for a full bottle. Keep repeating this step until you cannot exchange bottles anymore.

"""

class Solution:
    def maxBottlesDrunk(self, numBottles:int, numExchange:int) -> int:
        ans = numBottles
        empty = numBottles
        exchange = numExchange
        while empty >= exchange:
            empty = empty - exchange + 1
            ans += 1
            exchange += 1 
        return ans
sol = Solution()
print(sol.maxBottlesDrunk(numBottles = 13, numExchange = 6))
print(sol.maxBottlesDrunk(numBottles = 10, numExchange = 3))
            

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange - 1
            total += 1
            numExchange += 1

        return total      