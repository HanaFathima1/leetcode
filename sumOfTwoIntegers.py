"""

LC:371. Sum of Two Integers

Medium

Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000

"""
class Solution:
    def getSum(self, a:int, b:int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b!=0:
            carry = (a&b)&MASK
            a = (a^b)&MASK
            b = (carry<<1)&MASK
        return a if a<=MAX_INT else ~(a^MASK)
sol = Solution()
print(sol.getSum(a = 1, b = 2))
print(sol.getSum(a = 2, b = 3))