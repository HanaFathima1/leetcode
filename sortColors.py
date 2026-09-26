"""

LC: 75. Sort Colors

Medium

Topics:
Array
Two Pointers
Sorting

Hint 1
Hint
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
3,212,666/4.7M
Acceptance Rate
68.2%

Hint 1
A rather straight forward solution is a two-pass algorithm using counting sort.
Hint 2
Iterate the array counting number of 0's, 1's, and 2's.
Hint 3
Overwrite array with the total number of 0's, then 1's and followed by 2's.

"""

#Dutch National Flag
from typing import List
class Solution:
    def sortColors(self, nums:List[int]) -> None:
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums
sol = Solution()
print(sol.sortColors([2,0,2,1,1,0]))
print(sol.sortColors([2,0,1]))    

#------------------------------------


#counting sort
def sortColr(nums):
    count0 = nums.count(0)
    count1 = nums.count(1)
    count2 = nums.count(2)
    nums[:] = [0]*count0 + [1]*count1 + [2]*count2
    return nums
print(sortColr([2,0,2,1,1,0]))
               