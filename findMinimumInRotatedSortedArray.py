"""

LC: 153. Find Minimum in Rotated Sorted Array

Solved

Medium

Topics
Array
Binary Search

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
3,198,681/5.8M
Acceptance Rate
54.9%

Hint 1
Array was originally in ascending order. Now that the array is rotated, there would be a point in the array where there is a small deflection from the increasing sequence. eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].
Hint 2
You can divide the search space into two and see which direction to go. Can you think of an algorithm which has O(logN) search complexity?
Hint 3
All the elements to the low of inflection point > first element of the array.
All the elements to the high of inflection point < first element of the array.

"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        return min(nums)
"""
Complexity

The issue is the time complexity:

min(nums) scans every element in the array.
Time Complexity: O(n)
Space Complexity: O(1)
"""

#===========================================================

class Solution:
    def findMin(self, nums:list[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]
sol = Solution()
print(sol.findMin(nums = [3,4,5,1,2]))
print(sol.findMin(nums = [4,5,6,7,0,1,2]))
print(sol.findMin(nums = [11,13,15,17]))



#=================Explanation=================
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Initialize two pointers:
        # low points to the beginning of the array
        # high points to the end of the array
        low, high = 0, len(nums) - 1

        # Continue until both pointers meet
        # When low == high, we have found the minimum element
        while low < high:

            # Find the middle index of the current search space
            mid = (low + high) // 2

            # Compare nums[mid] with nums[high]
            #
            # Example:
            # nums = [4,5,6,7,0,1,2]
            #
            # mid = 3 -> nums[mid] = 7
            # high = 6 -> nums[high] = 2
            #
            # Since 7 > 2, the minimum cannot be in the left part.
            # It must be in the right half.
            if nums[mid] > nums[high]:

                # Discard the left half including mid
                # Search only in the right half
                low = mid + 1

            else:
                # nums[mid] <= nums[high]
                #
                # Example:
                # nums = [5,1,2,3,4]
                #
                # mid = 2 -> nums[mid] = 2
                # high = 4 -> nums[high] = 4
                #
                # Since 2 < 4, the minimum is either:
                # 1. At mid
                # 2. Somewhere to the left of mid
                #
                # Therefore keep mid and move high to mid
                high = mid

        # When the loop ends:
        # low == high
        #
        # Both pointers point to the minimum element
        return nums[low]


# Create an object of Solution class
sol = Solution()

# Test cases
print(sol.findMin([3,4,5,1,2]))      # Output: 1
print(sol.findMin([4,5,6,7,0,1,2]))  # Output: 0
print(sol.findMin([11,13,15,17]))    # Output: 11

"""

==================Dry Run=================
Input
nums = [3,4,5,1,2]
low	high	mid	nums[mid]	nums[high]	Action
0	4	2	5	2	low = mid + 1
3	4	3	1	2	high = mid
3	3	-	-	-	Stop

Return:

nums[3] = 1

=======================================
Why while low < high instead of <=?

Because we're narrowing down to one index.

When:

low == high

we have found the minimum element.
"""