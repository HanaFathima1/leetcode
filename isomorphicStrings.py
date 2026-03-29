"""
    
LC: 205. Isomorphic Strings

Easy

Topics:
Hash Table
String 

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""

class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        map_s_to_t = {}
        map_t_to_s = {}
        for char_s,char_t in zip(s,t):
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                if char_t in map_t_to_s:
                    return False
                map_s_to_t[char_s] = char_t
                map_t_to_s[char_t] = char_s
        return True
sol = Solution()
print(sol.isIsomorphic(s = "egg", t = "add"))
print(sol.isIsomorphic( s = "foo", t = "bar"))
print(sol.isIsomorphic(s = "paper", t = "title"))


# ----------------------------------------------------------

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap, tmap = {}, {}
        for i in range(len(s)):
            if (s[i] in smap and smap[s[i]] != t[i]) or (s[i] not in smap and t[i] in tmap):
                return False
            smap[s[i]] = t[i]
            tmap[t[i]] = s[i]
        return True