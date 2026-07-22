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
    
    
"""
s = "(({}))"
Initial State
stack = []
closeToOpen = {
    ")": "(",
    "]": "[",
    "}": "{"
}

We now iterate through every character in the string.

Iteration 1
Current character
c = "("

Is "(" in closeToOpen?

No

So execute:

stack.append("(")

Stack becomes

["("]
Iteration 2

Current character

c = "("

Again, it is an opening bracket.

Push into stack.

stack = ["(", "("]
Iteration 3

Current character

c = "{"

Not a closing bracket.

Push into stack.

stack = ["(", "(", "{"]
Iteration 4

Current character

c = "}"

Now } is in closeToOpen.

closeToOpen["}"]

returns

"{"

Now check

stack and stack[-1] == "{"

Current stack

["(", "(", "{"]

Top element

stack[-1] = "{"

Condition becomes

True and True

So execute

stack.pop()

Stack becomes

["(", "("]
Iteration 5

Current character

c = ")"

Lookup

closeToOpen[")"]

returns

"("

Current stack

["(", "("]

Top

stack[-1] = "("

Matches.

Pop.

stack = ["("]
Iteration 6

Current character

c = ")"

Again,

closeToOpen[")"] = "("

Top of stack

stack[-1] = "("

Matches.

Pop.

stack = []
End of Loop

Stack is

[]

Return statement

return True if not stack else False

Since

not stack

is

True

the function returns

True

Output

True
Dry Run Table

| Step  | Character | Action                      | Stack             |
| ----- | --------- | --------------------------- | ----------------- |
| Start | -         | Initialize                  | `[]`              |
| 1     | `(`       | Push                        | `["("]`           |
| 2     | `(`       | Push                        | `["(", "("]`      |
| 3     | `{`       | Push                        | `["(", "(", "{"]` |
| 4     | `}`       | Matches `{`, Pop            | `["(", "("]`      |
| 5     | `)`       | Matches `(`, Pop            | `["("]`           |
| 6     | `)`       | Matches `(`, Pop            | `[]`              |
| End   | -         | Stack empty → Return `True` | `[]`              |

Time Complexity
O(n) — each character is pushed and popped at most once.
Space Complexity
O(n) in the worst case (e.g., "(((([[").

"""