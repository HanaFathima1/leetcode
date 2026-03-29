"""

LC: 394. Decode String

Medium

Topics
String
Stack
Recursion

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,111,150/1.8M
Acceptance Rate
61.9%

"""

class Solution:
    def decodeString(self,s:str)->str:
        stack=[]
        res=""
        num=0
        for c in s:
            if c.isdigit():
                num=num*10+int(c)
            elif c=='[':
                stack.append((res,num))
                res,num="",0
            elif c==']':
                prev,k = stack.pop()
                res=prev+res*k
            else:
                res+=c
        return res
sol = Solution()
print(sol.decodeString(s = "3[a]2[bc]"))
print(sol.decodeString(s = "3[a2[c]]"))
print(sol.decodeString(s = "2[abc]3[cd]ef"))