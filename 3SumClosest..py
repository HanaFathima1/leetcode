"""

LC: 16. 3Sum Closest

Medium

Topics:
Array
Two Pointers
Sorting

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,585,407/3.4M
Acceptance Rate
47.2%

"""

from typing import List
class Solution:
    def threeSumClosest(self, nums:List[int], target:int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')
        for i in range(n-2):
            j,k = i+1,n-1
            while j<k:
                curr_sum = nums[i]+nums[j]+nums[k]
                if abs(target-curr_sum) < abs(target-closest):
                    closest = curr_sum
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    j += 1
                else:
                    k -= 1
        return closest
sol = Solution()
print(sol.threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(sol.threeSumClosest(nums = [0,0,0], target = 1))



                