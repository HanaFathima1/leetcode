"""

LC: 67. Add Binary

Easy

Topics
Math
String
Bit Manipulation
Simulation

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

Seen this question in a real interview before?
1/6
Yes
No
Accepted
2,375,012/4.1M
Acceptance Rate
58.1%

"""

class Solution:
    def addBinary(self, a:str, b:str) -> str:
        result=[]
        i,j=len(a)-1,len(b)-1
        carry=0
        while i>=0 or j>=0 or carry:
            total=carry
            if i>=0:
                total+=int(a[i])
                i-=1
            if j>=0:
                total+=int(b[j])
                j-=1
            result.append(str(total%2))
            carry=total//2
        return ''.join(reversed(result))
sol=Solution()
print(sol.addBinary("11","1"))

"""

=================DRY RUN=================

a = "11"
b = "1"
Initial State
i = 1          # points to last digit of "11"
j = 0          # points to last digit of "1"
carry = 0
result = []
Iteration 1
total = carry = 0
Add a[i]
a[1] = '1'
total = 0 + 1 = 1
i = 0
Add b[j]
b[0] = '1'
total = 1 + 1 = 2
j = -1
Store bit
result.append(str(2 % 2))
result.append("0")
Update carry
carry = 2 // 2 = 1

Current state:

result = ['0']
carry = 1
i = 0
j = -1
Iteration 2

Condition:

i >= 0 or j >= 0 or carry
0 >= 0 ✓
Start
total = carry = 1
Add a[i]
a[0] = '1'
total = 1 + 1 = 2
i = -1
j is already -1

Skip.

Store bit
result.append(str(2 % 2))
result.append("0")
Update carry
carry = 2 // 2 = 1

Current state:

result = ['0', '0']
carry = 1
i = -1
j = -1
Iteration 3

Condition:

carry = 1

so loop runs again.

Start
total = carry = 1

No digits left in a or b.

Store bit
result.append(str(1 % 2))
result.append("1")
Update carry
carry = 1 // 2 = 0

Current state:

result = ['0', '0', '1']
carry = 0
Loop Ends
result = ['0', '0', '1']

Currently digits are in reverse order because we added from right to left.

reversed(result)
= ['1', '0', '0']

Join them:

''.join(reversed(result))
= "100"


| Iteration | total | Bit Added (`total%2`) | Carry (`total//2`) | result        |
| --------- | ----- | --------------------- | ------------------ | ------------- |
| 1         | 2     | 0                     | 1                  | ['0']         |
| 2         | 2     | 0                     | 1                  | ['0','0']     |
| 3         | 1     | 1                     | 0                  | ['0','0','1'] |


Trick to Remember

This problem is exactly like manual binary addition:

   1 1
 +   1
 -----
 1 0 0

At every step:

total = bit1 + bit2 + carry

answer bit = total % 2
new carry = total // 2

"""