"""

LC: 1071. Greatest Common Divisor of Strings

Easy

Topics
Math
String
Weekly Contest 139

Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
862,820/1.6M
Acceptance Rate
53.0%

Hint 1
The greatest common divisor must be a prefix of each string, so we can try all prefixes.

"""

class Solution:
    def gcdOfStrings(self, str1:str, str2:str) -> str:
        if str1+str2 != str2+str1:
            return ""
        def gcd(str1,str2):
            while str2:
                str1,str2 = str2,str1%str2
            return str1
        return str1[:gcd(len(str1),len(str2))]
    
        """str1 = "ABABAB"
        str2 = "ABAB"
        len(str1) = 6
        len(str2) = 4
        gcd(len(str1), len(str2))
        This finds the greatest common divisor (GCD) of their lengths.
        👉 For the example:
        gcd(6, 4) = 2
        This means the smallest repeating unit that could make both strings is 2 characters long.
        str1[:gcd(len(str1), len(str2))]
        The expression str1[:k] means:
        → Take the substring of str1 from index 0 up to (but not including) index k.
        So here, k = gcd(len(str1), len(str2))
        In our example:
        str1[:2]  → "AB" """
        
sol = Solution()
print(sol.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(sol.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
print(sol.gcdOfStrings(str1 = "LEET", str2 = "CODE"))