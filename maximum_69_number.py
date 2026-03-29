"""

LC: 1323. Maximum 69 Number

Easy

Topics
Math
Greedy
Weekly Contest 172

Hint
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).


Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
 

Constraints:

1 <= num <= 104
num consists of only 6 and 9 digits.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
401,616/478.9K
Acceptance Rate
83.9%

Hint 1
Convert the number in an array of its digits.
Hint 2
Brute force on every digit to get the maximum number.

"""

class Solution:
    def maximum69Number(self, num:int) -> int:
        num_list=list(str(num))
        for i in range(len(num_list)):
            if num_list[i]=='6':
                num_list[i]='9'
                break
        return int("".join(num_list))
    
# or

#       return int(str(num).replace('6','9',1))

sol=Solution()
print(sol.maximum69Number(9669))
print(sol.maximum69Number(9996))
print(sol.maximum69Number(9999))

