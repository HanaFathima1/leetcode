"""

LC: 3. Longest Substring Without Repeating Characters

Medium

Topics
Staff
Hash Table
String
Sliding Window

Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
9,577,124/24.5M
Acceptance Rate
39.1%

Hint 1
There are less than 100 unique characters. We can check all substrings with length at most 100 for example. This is a good enough approximation.


"""

class Solution:
    def longestSubstring(self, s:str) -> int:
        char_set = set()
        left = 0 
        right = 0 
        max_len = 0
        
        while right<len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                max_len = max(max_len, right-left+1)
                right+=1
            else:
                char_set.remove(s[left])
                left+=1
        return max_len
    
sol = Solution()
print(sol.longestSubstring("abcabcbbdcdcea"))