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
        
        
        