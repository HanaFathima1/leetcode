"""

LC: 20. Valid Parentheses

Easy

Topics:
String
Stack

Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
6,542,859/15.3M
Acceptance Rate
42.8%

Hint 1
Use a stack of characters.
Hint 2
When you encounter an opening bracket, push it to the top of the stack.
Hint 3
When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.

"""
 

class Solution :
    def isValid(self, s:str) -> bool:
        stack=[]
        closeToOpen = { ")":"(", "]":"[", "}":"{" }
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

sol=Solution()        
print(sol.isValid("(({}))"))
    