"""

LC: 9. Palindrome Number

Easy

Topics
Math

Hint
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
6,922,237/11.6M
Acceptance Rate
59.6%

Hint 1
Beware of overflow when you reverse the integer. 

"""


def isPalindrome(s):
    if s == s[::-1]:
        print("Its a palindrome")
    else:
        print("Its not a palindrome")
        
    #return s == s[::-1]
        
print(isPalindrome("hello")) 

#Given an integer x, return true if x is a palindrome, and false otherwise.

def num_is_palindrome(num):
    return str(num) == str(num)[::-1]

print(num_is_palindrome(-121))