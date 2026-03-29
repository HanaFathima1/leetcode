"""

LC: 392. Is Subsequence

Attempted

Easy

Topics
Two Pointers
String
Dynamic Programming

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,264,223/4.7M
Acceptance Rate
48.6%

"""

class Solution:
    def isSubsequence(self, s:str, t:str) -> bool:
        i,j = 0,0
        while i<len(s) and j<len(t):  #This while loop continues as long as i hasn’t reached the end of s, and j hasn’t reached the end of t.
            if s[i] == t[j]:  #Checks if the current character in s (pointed by i) matches the current character in t (pointed by j).
                i+=1    #When a match is found: Move the pointer i to the next character in s.
            j+=1     #Regardless of whether a match was found or not, we always move j.
        return i == len(s)   #When the loop ends, this condition checks if we matched all characters in s.
sol = Solution()
print(sol.isSubsequence(s = "abc", t = "ahbgdc"))
print(sol.isSubsequence(s = "axc", t = "ahbgdc"))
print(sol.isSubsequence(s = "", t = "ahbgdc"))