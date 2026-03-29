"""

LC: 680. Valid Palindrome II

Easy

Topics
Mid Level
Two Pointers
String
Greedy

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,127,819/2.6M
Acceptance Rate
44.1%

"""

class Solution:
    def validPalindrome(self, s:str) -> bool:
        def isPalindromeRange(s, left, right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        left,right = 0,len(s)-1
        while left<right:
            if s[left] != s[right]:
                return isPalindromeRange(s,left+1,right) or isPalindromeRange(s,left,right-1)
            left+=1
            right-=1
        return True
sol=Solution()
print(sol.validPalindrome("abca"))
        
        
        