"""

LC: 53. Maximum Subarray

Medium

Topics
Array
Divide and Conquer
Dynamic Programming

Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
5,359,939/10.2M
Acceptance Rate
52.4%

"""

class Solution:
    def maxSubArray(self,nums):
        global_max = nums[0]
        current_max = nums[0]
        for i in range(1,len(nums)):
            current_max = max(nums[i], nums[i] + current_max)
            global_max = max(current_max, global_max)
        return global_max
    
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))