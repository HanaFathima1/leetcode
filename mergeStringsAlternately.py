"""

1768. Merge Strings Alternately

Easy

Topics
Two Pointers
String
Weekly Contest 229
icon

Hint
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,843,143/2.2M
Acceptance Rate
82.1%

Hint 1
Use two pointers, one pointer for each string. Alternately choose the character from each pointer, and move the pointer upwards.

"""

from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1:str, word2:str) -> str:
        res = ""
        for ptr1, ptr2 in zip_longest(word1, word2, fillvalue=""):
            res += ptr1+ptr2
        return res
sol = Solution()
print(sol.mergeAlternately(word1 = "abc", word2 = "pqr"))
print(sol.mergeAlternately(word1 = "ab", word2 = "pqrs"))
print(sol.mergeAlternately(word1 = "abcd", word2 = "pq"))

#------------------------------OR-------------------------------
class Solution:
    def mergeAlternately(self, word1:str, word2:str) -> str:
        ans=''
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                ans += word1[i]
            if i < len(word2):
                ans += word2[i]
        return ans
sol = Solution()
print(sol.mergeAlternately(word1 = "abc", word2 = "pqr"))
print(sol.mergeAlternately(word1 = "ab", word2 = "pqrs"))
print(sol.mergeAlternately(word1 = "abcd", word2 = "pq"))
