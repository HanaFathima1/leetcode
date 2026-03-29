"""

LC: 771. Jewels and Stones

Easy

Topics
Hash Table
String
Weekly Contest 69

Hint
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,270,652/1.4M
Acceptance Rate
89.3%

Hint 1
For each stone, check if it is a jewel.

"""

class Solution:
    def numJewelsInStones(self, jewels:str, stones:str) -> int:
        count = 0
        for ch in stones:
            if ch in jewels:
                count+=1
        return count
sol = Solution()
print(sol.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(sol.numJewelsInStones(jewels = "z", stones = "ZZ"))