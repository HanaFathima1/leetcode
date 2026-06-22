"""

LC: 35. Search Insert Position

Easy

Topics
Array
Binary Search

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
4,858,216/9.4M
Acceptance Rate
51.5%
 
"""
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left
sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))
print(sol.searchInsert([1,3,5,6], 2))  
print(sol.searchInsert([1,3,5,6], 7))  


"""
=========DRY RUN==========
nums = [1,3,5,6]
target = 7

Initial values:

left = 0
right = 3
Iteration 1
mid = (0 + 3) // 2 = 1
nums[mid] = 3

Since:

3 < 7

move left:

left = mid + 1 = 2

Now:

left = 2
right = 3
Iteration 2
mid = (2 + 3) // 2 = 2
nums[mid] = 5

Since:

5 < 7

move left:

left = 3

Now:

left = 3
right = 3
Iteration 3
mid = (3 + 3) // 2 = 3
nums[mid] = 6

Since:

6 < 7

move left:

left = 4

Now:

left = 4
right = 3
Loop condition
while left <= right

becomes:

4 <= 3   # False

Loop stops.

At this point:

left = 4
right = 3

and the code returns:

return left

which is:

4
"""
