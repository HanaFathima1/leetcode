class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
        # if sorted(s)==sorted(t):
        #     return True
        # return False
sol = Solution()
print(sol.isAnagram("anagram","nagaram"))
print(sol.isAnagram("rat","cat"))

def validAnagram(s,t):
    s_freq={}
    t_freq={}
    if char in s:
        s_freq[char]+=1
    else:
        t_freq[char]=1
    return s_freq==t_freq
print(validAnagram("rat","cat"))