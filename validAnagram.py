"""

LC: 242. Valid Anagram

Easy

Topics
Hash Table
String
Sorting

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
6,217,372/9.1M
Acceptance Rate
68.1%

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
        # if sorted(s)==sorted(t):
        #     return True
        # return False
sol = Solution()
print(sol.isAnagram("anagram","nagaram"))
print(sol.isAnagram("rat","cat"))

#------------------------------------------------------

def validAnagram(s,t):
    s_freq={}
    t_freq={}
    for char in s:
        if char in s_freq:
            s_freq[char]+=1
        else:
            s_freq[char]=1
    for char in t:
        if char in t_freq:
            t_freq[char]+=1
        else:
            t_freq[char]=1
    return s_freq==t_freq
print(validAnagram("rat","cat"))