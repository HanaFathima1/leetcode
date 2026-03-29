"""

LC:258. Add Digits

Easy

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
 

Follow up: Could you do it without any loop/recursion in O(1) runtime?

"""

#brute force
class Solution:
    def addDigits(self, num:int) -> int:
        while num>=10:
            sum_digits=0
            while num>0:
                sum_digits+=num%10
                num//=10
            num=sum_digits
        return num
sol=Solution()
print(sol.addDigits(38))
print(sol.addDigits(0))

#digital root
class Solution:
    def addDigits(self, num:int) -> int:
        if num==0:
            return 0
        elif num%9==0:
            return 9
        return num%9
sol=Solution()
print(sol.addDigits(38))
print(sol.addDigits(0))

    
