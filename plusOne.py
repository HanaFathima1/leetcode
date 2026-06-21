"""

LC: 66. Plus One

Easy

Topics
Array
Math

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
3,804,813/7.6M
Acceptance Rate
50.1%

"""


from typing import List

class Solution:
    def plusOne(self, digits:List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num+=1
        return list(map(int, str(num)))
    
sol = Solution()
print(sol.plusOne([1,2,3]))
print(sol.plusOne([9,9,9]))


"""

==================DRY RUN===================

Dry Run 1: digits = [1,2,3]
Step 1: Convert each digit to string
map(str, digits)
Digit	String
1	"1"
2	"2"
3	"3"

Result:

["1", "2", "3"]
Step 2: Join the strings
"".join(["1","2","3"])

Result:

"123"
Step 3: Convert string to integer
int("123")

Result:

num = 123
Step 4: Add 1
num += 1

Result:

num = 124
Step 5: Convert integer back to string
str(124)

Result:

"124"
Step 6: Convert each character to integer
map(int, "124")
Character	Integer
'1'	1
'2'	2
'4'	4

Result:

[1,2,4]
Final Output
[1,2,4]
Dry Run 2: digits = [9,9,9]
Step 1: Convert digits to strings
map(str, digits)

Result:

["9","9","9"]
Step 2: Join strings
"".join(["9","9","9"])

Result:

"999"
Step 3: Convert to integer
int("999")

Result:

num = 999
Step 4: Add 1
num += 1

Result:

num = 1000
Step 5: Convert back to string
str(1000)

Result:

"1000"
Step 6: Convert each character to integer
map(int, "1000")
Character	Integer
'1'	1
'0'	0
'0'	0
'0'	0

Result:

[1,0,0,0]
Final Output
[1,0,0,0]

"""