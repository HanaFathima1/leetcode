"""

LC: 137. Single Number II

Medium

Topics
Array
Bit Manipulation

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
905,081/1.3M
Acceptance Rate
67.2%

"""

class Solution:
    def singleNumber(self, nums:list[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones^num) & ~twos
            twos = (twos^num) & ~ones
        return ones
sol = Solution()
print(sol.singleNumber(nums = [2,2,3,2]))
print(sol.singleNumber(nums = [0,1,0,1,0,1,99]))