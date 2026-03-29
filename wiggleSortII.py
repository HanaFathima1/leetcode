"""

LC: 324. Wiggle Sort II

Medium

Topics
Array
Divide and Conquer
Greedy
Sorting
Quickselect

Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

 

Example 1:

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
Example 2:

Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 5000
It is guaranteed that there will be an answer for the given input nums.
 

Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
187,219/519K
Acceptance Rate
36.1%

"""

from typing import List
class Solution:
    def wiggleSort(self, nums:List[int]) -> None:
        n = len(nums)
        nums.sort()
        left = nums[:(n+1)//2][::-1]
        right = nums[(n+1)//2:][::-1]
        nums[::2] = left
        nums[1::2] = right
        return nums
sol = Solution()
print(sol.wiggleSort(nums = [1,5,1,1,6,4]))
print(sol.wiggleSort(nums = [1,3,2,2,3,1]))