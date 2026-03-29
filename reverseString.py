"""

LC:344. Reverse String

Solved

Easy

Topics
Two Pointers
String

Hint
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
3,326,025/4.2M
Acceptance Rate
80.0%

Hint 1
The entire logic for reversing a string is based on using the opposite directional two-pointer approach!

"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left<right:
            s[left], s[right]=s[right],s[left]
            left+=1
            right-=1
        return s
    
sol = Solution()
print(sol.reverseString(s = ["h","e","l","l","o"]))
print(sol.reverseString(s = ["H","a","n","n","a","h"]))