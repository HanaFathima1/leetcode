"""

LC: 844. Backspace String Compare

Easy

Topics
Two Pointers
String
Stack
Simulation
Weekly Contest 87

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?

 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
976,922/2M
Acceptance Rate
49.6%

"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack=[]
            for ch in string:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return "".join(stack)
        return build(s) == build(t)
sol = Solution()
print(sol.backspaceCompare(s = "ab#c", t = "ad#c"))
print(sol.backspaceCompare( s = "ab##", t = "c#d#"))
print(sol.backspaceCompare( s = "a#c", t = "b"))