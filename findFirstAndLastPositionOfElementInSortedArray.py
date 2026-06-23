"""

LC: 34. Find First and Last Position of Element in Sorted Array

Attempted

Medium

Topics
Array
Binary Search

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
3,401,761/6.9M
Acceptance Rate
49.1%

"""

class Solution:
    def searchRange(self, nums:list[int], target:int) -> list[int]:
        def firstPosition():
            left, right  = 0, len(nums)-1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first
        def lastPosition():
            left, right = 0, len(nums)-1
            last = -1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last
        return [firstPosition(), lastPosition()]
sol = Solution()
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(sol.searchRange(nums = [], target = 0))
                    
                    
                    
#============EXPLANATION=============

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        # Function to find the FIRST occurrence of target
        def firstPosition():

            # Initialize pointers at the beginning and end of the array
            left, right = 0, len(nums) - 1

            # Store the answer; -1 means target not found yet
            first = -1

            # Continue searching while the search space is valid
            while left <= right:

                # Find the middle index
                mid = (left + right) // 2

                # If target is found
                if nums[mid] == target:

                    # Store current position as a possible first occurrence
                    first = mid

                    # Continue searching on the LEFT side
                    # to check if there is an earlier occurrence
                    right = mid - 1

                # If target is greater than middle element
                elif nums[mid] < target:

                    # Search in the right half
                    left = mid + 1

                # If target is smaller than middle element
                else:

                    # Search in the left half
                    right = mid - 1

            # Return the first occurrence index
            # If target was never found, returns -1
            return first

        # Function to find the LAST occurrence of target
        def lastPosition():

            # Initialize pointers at the beginning and end of the array
            left, right = 0, len(nums) - 1

            # Store the answer; -1 means target not found yet
            last = -1

            # Continue searching while the search space is valid
            while left <= right:

                # Find the middle index
                mid = (left + right) // 2

                # If target is found
                if nums[mid] == target:

                    # Store current position as a possible last occurrence
                    last = mid

                    # Continue searching on the RIGHT side
                    # to check if there is a later occurrence
                    left = mid + 1

                # If target is greater than middle element
                elif nums[mid] < target:

                    # Search in the right half
                    left = mid + 1

                # If target is smaller than middle element
                else:

                    # Search in the left half
                    right = mid - 1

            # Return the last occurrence index
            # If target was never found, returns -1
            return last

        # Return both first and last positions as a list
        return [firstPosition(), lastPosition()]


# Create an object of Solution class
sol = Solution()

# Example 1
# Target 8 appears at indices 3 and 4
print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
# Output: [3, 4]

# Example 2
# Target 6 does not exist in the array
print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
# Output: [-1, -1]

# Example 3
# Empty array, so target cannot be found
print(sol.searchRange(nums=[], target=0))
# Output: [-1, -1]


"""
Dry Run
nums = [5,7,7,8,8,10]
target = 8

findFirst()

| left | right | mid | nums[mid] | first |
| ---- | ----- | --- | --------- | ----- |
| 0    | 5     | 2   | 7         | -1    |
| 3    | 5     | 4   | 8         | 4     |
| 3    | 3     | 3   | 8         | 3     |


Result: 3

findLast()

| left | right | mid | nums[mid] | last |
| ---- | ----- | --- | --------- | ---- |
| 0    | 5     | 2   | 7         | -1   |
| 3    | 5     | 4   | 8         | 4    |
| 5    | 5     | 5   | 10        | 4    |

Result: 4

Final Answer:

[3, 4]

Complexity

Time: O(log n) + O(log n) = O(log n)
Space: O(1)
"""