"""

LC: 22. Generate Parentheses

Medium

Topics
String
Dynamic Programming
Backtracking
Bracket Sequences

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
3,116,620/3.9M
Acceptance Rate
79.2%

"""

def generateParentheses(n):
    res=[]
    def generate(s):
        if len(s)==2*n:
            if isValid(s):
                res.append(s)
            return
        generate(s+"(")
        generate(s+")")
    def isValid(s):
        count=0
        for ch in s:
            if ch=="(":
                count+=1
            else:
                count-=1
            if count<0:
                return False
        return count==0
    generate("")
    return res
print(generateParentheses(3))


#or

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        def backtrack(s,open,close):
            if len(s)==2*n:
                res.append(s)
                return
            if open<n:
                backtrack(s+"(",open+1,close)
            if close<open:
                backtrack(s+")",open,close+1)
        backtrack("",0,0)
        return res
sol=Solution()
print(sol.generateParenthesis(n=3))