"""

LC: 704. Binary Search

Easy

Topics
Array
Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
4,017,085/6.6M
Acceptance Rate
61.0%

"""
 

class Solution:
    def binarySearch(self, nums:list[int], target:int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high- low) // 2 #OR  mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
sol = Solution()
print(sol.binarySearch([-1,0,3,5,9,12],2))
print(sol.binarySearch([-1,0,3,5,9,12],9))

"""
========DRY RUN=======
Dry Run for target = 9

| low | high | mid | nums[mid] |
| --- | ---- | --- | --------- |
| 0   | 5    | 2   | 3         |
| 3   | 5    | 4   | 9         |

nums[4] == 9, so return 4.

========COMPLEXITY=========
Time Complexity: O(log n)
Space Complexity: O(1)

"""