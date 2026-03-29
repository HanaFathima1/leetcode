"""

LC: 917. Reverse Only Letters

Easy

Topics
Two Pointers
String
Weekly Contest 105

Hint
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
284,964/424.3K
Acceptance Rate
67.2%

Hint 1
This problem is exactly like reversing a normal string except that there are certain characters that we have to simply skip. That should be easy enough to do if you know how to reverse a string using the two-pointer approach.

"""

class Solution:
    def reverseOnlyString(self, s:str) -> str:
        s = list(s)
        left = 0
        right = len(s)-1
        while left<right:
            if not s[left].isalpha():
                left+=1
                continue
            if not s[right].isalpha():
                right-=1
                continue
            s[left], s[right] = s[right],s[left]
            left+=1
            right-=1
        return ''.join(s)
sol = Solution()
print(sol.reverseOnlyString("ab-cd"))
print(sol.reverseOnlyString("a-bC-dEf-ghIj"))
print(sol.reverseOnlyString("Test1ng-Leet=code-Q!"))
print(sol.reverseOnlyString("7_28]"))
        