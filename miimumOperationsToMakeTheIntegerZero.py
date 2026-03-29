"""

LC: 2749. Minimum Operations to Make the Integer Zero

Medium

Topics:
Bit Manipulation
Brainteaser
Enumeration
Weekly Contest 351

Hint
You are given two integers num1 and num2.

In one operation, you can choose integer i in the range [0, 60] and subtract 2i + num2 from num1.

Return the integer denoting the minimum number of operations needed to make num1 equal to 0.

If it is impossible to make num1 equal to 0, return -1.

 

Example 1:

Input: num1 = 3, num2 = -2
Output: 3
Explanation: We can make 3 equal to 0 with the following operations:
- We choose i = 2 and subtract 22 + (-2) from 3, 3 - (4 + (-2)) = 1.
- We choose i = 2 and subtract 22 + (-2) from 1, 1 - (4 + (-2)) = -1.
- We choose i = 0 and subtract 20 + (-2) from -1, (-1) - (1 + (-2)) = 0.
It can be proven, that 3 is the minimum number of operations that we need to perform.
Example 2:

Input: num1 = 5, num2 = 7
Output: -1
Explanation: It can be proven, that it is impossible to make 5 equal to 0 with the given operation.
 

Constraints:

1 <= num1 <= 109
-109 <= num2 <= 109
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
41,736/83.7K
Acceptance Rate
49.9%

Hint 1
If we want to make integer n equal to 0 by only subtracting powers of 2 from n, in how many operations can we achieve it?
Hint 2
We need at least - the number of bits in the binary representation of n, and at most - n.
Hint 3
Notice that, if it is possible to make num1 equal to 0, then we need at most 60 operations.
Hint 4
Iterate on the number of operations.

"""

class Solution:
    def makeTheIntegerZero(self, num1:int, num2:int) -> int:
        # we are looking for the smallest k>=1 such that
        # x = num1-k*num2
        # is representable as a sum of k powers of 2.
        # this is possible if and only if:
        #     1.  x>=k since 2**0=1 is the smallest power of 2
        #     2.  x.bit_count() <= k the minimum number of    powers of 2 needed
        k = 1
        while True:
            x = num1 - k * num2
            # if x becomes smaller than k, it's impossible to satisfy
            # both conditions going forward, as k increases and x decreases.
            if x < k:
                return -1
            # check 2 conditions:
            if x.bit_count() <= k:
                return k
            k+=1
sol = Solution()
print(sol.makeTheIntegerZero(num1 = 3, num2 = -2))
print(sol.makeTheIntegerZero(num1 = 5, num2 = 7))