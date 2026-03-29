"""

LC: 1281. Subtract the Product and Sum of Digits of an Integer

Easy

Topics
Math
Weekly Contest 166

Hint
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5
Seen this question in a real interview before?
1/5
Yes
No
Accepted
590,585/681.9K
Acceptance Rate
86.6%

Hint 1
How to compute all digits of the number ?
Hint 2
Use modulus operator (%) to compute the last digit.
Hint 3
Generalise modulus operator idea to compute all digits.

"""

class Solution:
    def subtractProductAndSum(self, n:int) -> int:
        product = 1
        sums = 0
        while n>0:
            digit = n%10
            product*=digit
            sums+=digit
            n//=10
        return product-sums
sol = Solution()
print(sol.subtractProductAndSum(234))
print(sol.subtractProductAndSum(4421))

