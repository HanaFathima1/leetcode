"""

LC: 17. Letter Combinations of a Phone Number

Medium

Topics
Hash Table
String
Backtracking

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,925,917/4.5M
Acceptance Rate
65.5%

"""

class Solution:
    def letterCombinations(self,digits:str)->list[str]:
        if not digits:
            return []
        phone={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res=[]
        def backtrack(index,path):
            if index==len(digits):
                res.append(path)
                return
            letters=phone[digits[index]]
            for letter in letters:
                backtrack(index+1,path+letter)
        backtrack(0,"")
        return res
sol=Solution()
print(sol.letterCombinations(digits = "23"))
print(sol.letterCombinations(digits = "2"))