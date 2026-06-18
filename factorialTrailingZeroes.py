"""

LC: 172. Factorial Trailing Zeroes

Medium

Topics
Math

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
 

Follow up: Could you write a solution that works in logarithmic time complexity?

 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
681,495/1.5M
Acceptance Rate
46.9%

"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        
        count = 0
        while fact % 10 ==0:
            count+=1
            fact //= 10
            
        return count
sol = Solution()
print(sol.trailingZeroes(n = 3))
print(sol.trailingZeroes(n = 5))
print(sol.trailingZeroes(n = 0))

"""

Dry Run (n = 5)
fact = 120

120 % 10 == 0  -> count = 1
fact = 12

12 % 10 != 0

return 1

"""

# Optimal solution (asked in interviews)

# A trailing zero is produced by:

# 2 × 5 = 10

# There are always more 2s than 5s in a factorial.

# So we only count how many 5s appear.

class Solution:
    def trailingZeroes(self, n: int) -> int:

        count = 0

        while n:
            n //= 5
            count += n

        return count
sol = Solution()
print(sol.trailingZeroes(n=3))
print(sol.trailingZeroes(n=5))
print(sol.trailingZeroes(n=0))
    
"""

==============EXPLANATION==============
class Solution:
    def trailingZeroes(self, n: int) -> int:

        # A trailing zero is formed by 2 × 5 = 10.
        # In a factorial, there are always more 2s than 5s.
        # Therefore, we only need to count the number of 5s.

        count = 0

        while n:

            # Count multiples of 5:
            # n//5 gives how many numbers contribute
            # at least one factor of 5.
            n //= 5

            # Add these factors of 5 to the answer.
            count += n

        return count

"""

"""    
Dry Run (n = 25)
count = 0

n = 25
count += 25//5 = 5

n = 5
count += 5//5 = 1

n = 1
count += 1//5 = 0

Answer = 6

Why 6?

25! contains:

5,10,15,20,25  -> 5 factors of 5
25 itself gives one extra 5

Total = 6
"""


"""

==================Complexity=================
Brute Force
Time: O(n)
Space: O(size of n!)

Not practical for large n.

Optimal
Time: O(log₅ n)
Space: O(1)

"""