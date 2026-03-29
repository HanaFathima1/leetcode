"""

LC: 415. Add Strings

Easy

Topics
Math
String
Simulation

Given two non-negative integers, num1 and num2 represented as string,
return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for 
handling large integers (such as BigInteger). You must also not 
convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
840,854/1.6M
Acceptance Rate
51.9%

"""

class Solution:
    def addStrings(self, nums1:str, nums2:str) -> str:
        i=len(nums1)-1
        j=len(nums2)-1
        carry=0
        result=[]
        while i>=0 or j>=0 or carry:
            digit1=int(nums1[i]) if i>=0 else 0
            digit2 = int(nums2[j]) if j>=0 else 0
            total=digit1+digit2+carry
            carry=total//10
            result.append(str(total%10))
            i-=1
            j-=1
        return ''.join(reversed(result))
sol = Solution()
print(sol.addStrings(nums1 = "11", nums2 = "123"))
print(sol.addStrings(nums1 = "456", nums2 = "77"))
print(sol.addStrings(nums1 = "0", nums2 = "0"))
            