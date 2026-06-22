"""

LC: 33. Search in Rotated Sorted Array

Attempted

Medium

Topics
Array
Binary Search

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
4,654,337/10.3M
Acceptance Rate
45.1%

"""

class Solution:
    def search(self, nums:list[int], target:int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
sol = Solution()
print(sol.search(nums = [4,5,6,7,0,1,2], target = 0))
print(sol.search(nums = [4,5,6,7,0,1,2], target = 3))
print(sol.search(nums = [1], target = 0))


#EXPLANATION:
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Start with the entire array as our search space
        low, high = 0, len(nums) - 1

        # Continue searching while there are elements left
        while low <= high:

            # Find the middle index
            mid = (low + high) // 2

            # If we found the target, return its index
            if nums[mid] == target:
                return mid

            # Check if the LEFT HALF is sorted
            # Example:
            # [4,5,6,7,0,1,2]
            #  low     mid
            #
            # Since 4 <= 7, the left half is sorted
            if nums[low] <= nums[mid]:

                # Check if the target lies inside the sorted left half
                if nums[low] <= target < nums[mid]:

                    # Search only in the left half
                    high = mid - 1

                else:
                    # Target is not in the left half
                    # Search in the right half
                    low = mid + 1

            # Otherwise, the RIGHT HALF must be sorted
            else:

                # Example:
                # [6,7,0,1,2,4,5]
                #       mid     high
                #
                # Since 1 <= 5, the right half is sorted

                # Check if the target lies inside the sorted right half
                if nums[mid] < target <= nums[high]:

                    # Search only in the right half
                    low = mid + 1

                else:
                    # Target is not in the right half
                    # Search in the left half
                    high = mid - 1

        # Target not found
        return -1

"""

DRY RUN

Dry Run
nums = [4,5,6,7,0,1,2]
target = 0
Iteration 1
low	high	mid	nums[mid]
0	6	3	7
nums[low] <= nums[mid]
4 <= 7

Left half [4,5,6,7] is sorted.

4 <= 0 < 7

False.

Search right half:

low = mid + 1 = 4
Iteration 2
low	high	mid	nums[mid]
4	6	5	1
nums[low] <= nums[mid]
0 <= 1

Left half [0,1] is sorted.

0 <= 0 < 1

True.

Search left half:

high = mid - 1 = 4
Iteration 3
low	high	mid	nums[mid]
4	4	4	0
nums[mid] == target

Return:

4


============Complexity=============
Complexity	Value
Time	O(log n)
Space	O(1)

"""


            
        

