"""

LC: 58. Length of last word

Easy

Topics
String

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
3,349,285/5.7M
Acceptance Rate
58.5%

"""

class Solution:
    def lengthOfLastWord(self, s:str) -> int:
        length = 0
        i = len(s)-1
        while i>=0 and s[i]==' ':
            i-=1
        while i>=0 and s[i]!=' ':
            length+=1
            i-=1
        return length  

sol = Solution()
print(sol.lengthOfLastWord("a big  cat  "))      