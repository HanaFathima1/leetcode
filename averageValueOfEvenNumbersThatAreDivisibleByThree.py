"""

LC: 2455. Average Value of Even Numbers That Are Divisible by Three

Solved

Easy

Topics:
Array
Math
Weekly Contest 317

Hint
Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

 

Example 1:

Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
Example 2:

Input: nums = [1,2,4,7,10]
Output: 0
Explanation: There is no single number that satisfies the requirement, so return 0.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
83,447/134.1K
Acceptance Rate
62.2%

Hint 1
What is the property of a number if it is divisible by both 2 and 3 at the same time?
Hint 2
It is equivalent to finding all the numbers that are divisible by 6. 

"""

from typing import List
class Solution:
    def avaerageValue(self, nums:List[int]) -> int:
        total = 0
        avg = 0
        res = [x for x in nums if x%6==0]
        n = len(res)
        for x in res:
            total+=x
        if n>0:
            avg = total//n
        return avg
sol = Solution()
print(sol.avaerageValue([1,3,6,10,12,15]))
print(sol.avaerageValue([1,2,4,7,10]))            
        