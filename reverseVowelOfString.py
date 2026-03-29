"""

LC:345. Reverse Vowels of a String

Easy

Topics
Two Pointers
String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,345,601/2.3M
Acceptance Rate
58.8%

"""

class Solution:
    def reverseVowels(self, s:str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left = 0
        right = len(s_list)-1
        while left<right:
            if s_list[left] not in vowels:
                left+=1
            elif s_list[right] not in vowels:
                right-=1
            else:
                s_list[left], s_list[right] = s_list[right],s_list[left]
                left+=1
                right-=1
        return ''.join(s_list)
sol = Solution()
print(sol.reverseVowels(s = "IceCreAm"))
print(sol.reverseVowels( s = "leetcode"))
            
        
    