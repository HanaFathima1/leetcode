"""

LC: 1318. Minimum Flips to Make a OR b Equal to c

Medium

Topics
Bit Manipulation
Weekly Contest 171

Hint
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

Example 1:



Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0
 

Constraints:

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
184,247/256.4K
Acceptance Rate
71.9%

Hint 1
Check the bits one by one whether they need to be flipped.

"""

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        # process until all numbers are zero
        while a > 0 or b > 0 or c > 0:
            ai = a & 1
            bi = b & 1
            ci = c & 1

            if ci == 1:
                # need at least one of ai or bi to be 1
                if ai == 0 and bi == 0:
                    flips += 1
            else:
                # ci == 0 -> both ai and bi must be 0
                flips += ai + bi  # adds 1 if one is 1, 2 if both are 1, 0 if neither

            # shift right to check next bit
            a >>= 1
            b >>= 1
            c >>= 1

        return flips

sol = Solution()
print(sol.minFlips(a = 2, b = 6, c = 5))
print(sol.minFlips(a = 4, b = 2, c = 7))
print(sol.minFlips(a = 1, b = 2, c = 3))

                    