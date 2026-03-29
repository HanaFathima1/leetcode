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