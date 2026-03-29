"""

LC: 1684. Count the Number of Consistent Strings

Easy

Topics
Array
Hash Table
String
Bit Manipulation
Counting
Biweekly Contest 41

Hint
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 

Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
424,574/480.3K
Acceptance Rate
88.4%

Hint 1
A string is incorrect if it contains a character that is not allowed
Hint 2
Constraints are small enough for brute force

"""

class Solution:
    def countConsistentStrings(self,allowed:str, words:list[str])->int:
        allowed_set=set(allowed)
        count=0
        for word in words:
            is_consistent=True
            for ch in word:
                if ch not in allowed_set:
                    is_consistent=False
                    break
            if is_consistent:
                count+=1
        return count
sol=Solution()
print(sol.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
print(sol.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
print(sol.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))

#-------------

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=allowed.strip()
        l=[]
        n=len(words)
        for i in words:
            for ch in i:
                if ch not in s:
                    l.append("F")
                    break
        return n-len(l)
           
#---------------------

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(all(ch in allowed for ch in word) for word in words)
