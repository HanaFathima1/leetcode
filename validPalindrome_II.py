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
        
  
"""

                                    #dry run with complexity 


✅ Input
s = "abca"
🚀 Initial Setup
left = 0
right = 3   # len("abca") - 1

String indexing:

Index:   0   1   2   3
Chars:   a   b   c   a
🔁 Main Loop Dry Run
👉 Step 1:
s[left] == s[right]
s[0] == s[3] → 'a' == 'a' ✅

👉 Move inward:

left = 1
right = 2
👉 Step 2:
s[1] != s[2] → 'b' != 'c' ❌

💥 Mismatch found!

🔥 Now the KEY LOGIC
return isPalindromeRange(s, left+1, right) OR isPalindromeRange(s, left, right-1)

👉 Two possibilities:

Skip left character (b)
Skip right character (c)
✂️ Case 1: Skip left (b)
isPalindromeRange(s, 2, 2)

Check substring:

"c"
Dry run:
left = 2, right = 2
while left < right → False

👉 Return:

True ✅
✂️ Case 2: Skip right (c)
isPalindromeRange(s, 1, 1)

Check substring:

"b"
Dry run:
left = 1, right = 1
while left < right → False

👉 Return:

True ✅
✅ Final Decision
True OR True → True
🎉 Final Output
True

⏱ Complexity
Time: O(n)
Space: O(1)   

"""  