"""LC-69: Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

"""

class Solution:
    def mySqrt(self, x:int) -> int:
        if x<2:
            return x
        left, right = 1, x//2
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                left=mid+1
            else:
                right=mid-1
        return right
sol=Solution()
print(sol.mySqrt(8))

"""

======dry run====

Let's do a dry run for x = 8.

Initial Values
x = 8

left = 1
right = x // 2 = 4
Dry Run Table
| Iteration | left | right | mid = (left+right)//2 | mid*mid | Action                              |
| --------- | ---- | ----- | --------------------- | ------- | ----------------------------------- |
| 1         | 1    | 4     | 2                     | 4       | 4 < 8, search right half → left = 3 |
| 2         | 3    | 4     | 3                     | 9       | 9 > 8, search left half → right = 2 |

Iteration 1
left = 1
right = 4

mid = (1 + 4) // 2
    = 2

mid * mid = 4

Check:

4 == 8 ? No
4 < 8 ? Yes

Move to the right side:

left = mid + 1
     = 3

Now:

left = 3
right = 4
Iteration 2
mid = (3 + 4) // 2
    = 3

mid * mid = 9

Check:

9 == 8 ? No
9 < 8 ? No

So:

right = mid - 1
      = 2

Now:

left = 3
right = 2
Loop Condition
while left <= right

Check:

3 <= 2 ? False

Loop stops.

Return Statement
return right

Current value:

right = 2

Output:

2
Why return right?

When the loop ends:

left = 3
right = 2

We know:

2² = 4  ≤ 8
3² = 9  > 8

So the integer square root of 8 is:

⌊√8⌋ = 2

right always ends up pointing to the largest number whose square is ≤ x, so we return right.

Visualization
Numbers: 1  2  3  4
Squares: 1  4  9 16

For x = 8:

4 <= 8
9 > 8

Answer = 2
Complexity
Time Complexity  : O(log x)
Space Complexity : O(1)

"""