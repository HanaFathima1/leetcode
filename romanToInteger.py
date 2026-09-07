"""

LC: 13. Roman to Integer

Easy

Topics:
Hash Table
Math
String

Hint
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
5,163,605/7.9M
Acceptance Rate
65.4%

Hint 1
Problem is simpler to solve by working the string from back to front and using a map.

"""

# def romanToInteger(s):
#     roman = {
#     'I' : 1,
#     'V' : 5,
#     'X' : 10,
#     'L' : 50,
#     'C' : 100,
#     'D' : 500,
#     'M' : 1000
# }
#     total = 0
#     prev_value = 0
    
#     for char in reversed(s):
#         current = roman[char]
#         if current < prev_value:
#             total -= current
#         else:
#             total += current
#             prev_value = current
#     return total

# print(romanToInteger("MCMXCIV"))

#-----------------------------------------------------------------------#

class Solution:
    def romanToInt(self, s:str) -> int:
        roman_map={
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        total = 0
        length = len(s)
        for i in range(length):
            if i<length-1 and roman_map[s[i]]<roman_map[s[i+1]]:
                total-=roman_map[s[i]]
            else:
                total+=roman_map[s[i]]
        return total 
sol = Solution()
print(sol.romanToInt("III"))             
print(sol.romanToInt("MCMXCIV"))  
        
            
"""

DRY RUN

Dry Run 1 : "III"
Initial Values
s = "III"
length = 3
total = 0

| i | s[i] | Next Character    | Condition (`current < next`) | Operation | total |
| - | ---- | ----------------- | ---------------------------- | --------- | ----: |
| 0 | I    | I                 | 1 < 1 ❌ False                | +1        |     1 |
| 1 | I    | I                 | 1 < 1 ❌ False                | +1        |     2 |
| 2 | I    | No next character | Else                         | +1        |     3 |

Final Answer
3


Dry Run 2 : "MCMXCIV"

Roman Number:

M  C  M  X  C  I  V
1000 100 1000 10 100 1 5
Initial Values
total = 0
length = 7
Iteration 1
i = 0
Current = M = 1000
Next = C = 100

Check

1000 < 100 ?

No.

total += 1000
total = 1000
Iteration 2
i = 1
Current = C =100
Next = M =1000

Check

100 < 1000 ?

Yes.

So subtract.

total = 1000 -100
      =900
Iteration 3
i =2
Current = M =1000
Next = X =10

Check

1000 <10 ?

No.

total =900+1000
      =1900
Iteration 4
i =3
Current = X =10
Next = C =100

Check

10 <100 ?

Yes.

total =1900-10
      =1890
Iteration 5
i =4
Current = C =100
Next = I =1

Check

100 <1 ?

No.

total =1890+100
      =1990
Iteration 6
i =5
Current = I =1
Next = V =5

Check

1 <5 ?

Yes.

total =1990-1
      =1989
Iteration 7
i =6
Current = V =5
No next character

So else block executes.

total =1989+5
      =1994
Final Table
| i | Current | Value | Next | Value | Action | Total |
| - | ------- | ----: | ---- | ----: | ------ | ----: |
| 0 | M       |  1000 | C    |   100 | +1000  |  1000 |
| 1 | C       |   100 | M    |  1000 | -100   |   900 |
| 2 | M       |  1000 | X    |    10 | +1000  |  1900 |
| 3 | X       |    10 | C    |   100 | -10    |  1890 |
| 4 | C       |   100 | I    |     1 | +100   |  1990 |
| 5 | I       |     1 | V    |     5 | -1     |  1989 |
| 6 | V       |     5 | -    |     - | +5     |  1994 |


Final Answer:

1994

"""