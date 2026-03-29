"""

LC: 5. Longest Palindromic Substring

Medium

Topics
Two Pointers
String
Dynamic Programming

Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
4,141,974/11.4M
Acceptance Rate
36.4%

Hint 1
How can we reuse a previously computed palindrome to compute a larger palindrome?
Hint 2
If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
Hint 3
Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

"""

def longest_palindrome(s:str) -> str:
    def is_palindrome_from_center(left:int, right:int) -> str:
        while left>=0 and right<len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    longest=""
    for i in range(len(s)):
        p1=is_palindrome_from_center(i,i)
        p2=is_palindrome_from_center(i,i+1)
        if len(p1)>len(longest):
            longest = p1
        if len(p2)>len(longest):
            longest = p2
    return longest
print(longest_palindrome("babad"))


#-----------------using expand around the center algorithm--------------

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        resLen = 0

        for i in range(len(s)):

            # odd length palindrome
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                l -= 1
                r += 1

            # even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                l -= 1
                r += 1

        return 
    
"""

🔹 Example Input
s = "babad"
🔹 Initial State
res = ""
resLen = 0
🔁 Iteration by iteration
👉 i = 0 (character = 'b')
🔹 Odd length palindrome (center = 0)
l = 0, r = 0 → "b"
palindrome ✅
length = 1 > resLen(0)

👉 Update:

res = "b"
resLen = 1

Expand:

l = -1, r = 1 → stop
🔹 Even length palindrome (center = 0,1)
l = 0, r = 1 → "ba"
not palindrome ❌
👉 i = 1 (character = 'a')
🔹 Odd length palindrome
l = 1, r = 1 → "a"
length = 1 (not > resLen)

Expand:

l = 0, r = 2 → "bab"
palindrome ✅
length = 3 > resLen(1)

👉 Update:

res = "bab"
resLen = 3

Expand again:

l = -1, r = 3 → stop
🔹 Even length palindrome
l = 1, r = 2 → "ab"
not palindrome ❌
👉 i = 2 (character = 'b')
🔹 Odd length palindrome
l = 2, r = 2 → "b"

Expand:

l = 1, r = 3 → "aba"
palindrome ✅
length = 3 == resLen → no update (code updates only if >)

Expand:

l = 0, r = 4 → "babad"
not palindrome ❌
🔹 Even length palindrome
l = 2, r = 3 → "ba"
not palindrome ❌
👉 i = 3 (character = 'a')
🔹 Odd length palindrome
l = 3, r = 3 → "a"

Expand:

l = 2, r = 4 → "bad"
not palindrome ❌
🔹 Even length palindrome
l = 3, r = 4 → "ad"
not palindrome ❌
👉 i = 4 (character = 'd')
🔹 Odd length palindrome
l = 4, r = 4 → "d"

Expand:

l = 3, r = 5 → stop
🔹 Even length palindrome
l = 4, r = 5 → stop
✅ Final Result
res = "bab"
🔥 Key Insight (VERY IMPORTANT)
At each index i, we expand from center
Two cases:
Odd → center at i
Even → center between i and i+1

Keep expanding while:

s[l] == s[r]

Update result only when:

(r - l + 1) > resLen
🧠 Memory Trick

👉 “Every index is a center → expand left & right”

"""