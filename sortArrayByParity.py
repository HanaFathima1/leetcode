"""

LC: 905. Sort Array By Parity

Solved

Easy

Topics:
Array
Two Pointers
Sorting
Weekly Contest 102

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
941,177/1.2M
Acceptance Rate
76.3%

"""

from typing import List
class Solution:
    def sortArrayByParity(self,nums:List[int]) -> List[int]:
        low,mid,high = 0,0,len(nums)-1
        while mid<=high:
            if nums[mid]%2==0:
                nums[mid], nums[low] = nums[low], nums[mid] 
                mid+=1
                low+=1
            elif nums[mid]%2==1:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums
sol = Solution()
print(sol.sortArrayByParity([3,1,2,4]))
print(sol.sortArrayByParity([0]))