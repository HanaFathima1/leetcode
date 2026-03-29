"""

LC: 1991. Find the Middle Index in Array

Easy

Topics
Array
Prefix Sum
Biweekly Contest 60

Hint
Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

 

Example 1:

Input: nums = [2,3,-1,8,4]
Output: 3
Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4
Example 2:

Input: nums = [1,-1,4]
Output: 2
Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0
Example 3:

Input: nums = [2,5]
Output: -1
Explanation: There is no valid middleIndex.
 

Constraints:

1 <= nums.length <= 100
-1000 <= nums[i] <= 1000
 

Note: This question is the same as 724: https://leetcode.com/problems/find-pivot-index/

 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
146,540/213.6K
Acceptance Rate
68.6%

Hint 1
Could we go from left to right and check to see if an index is a middle index?
Hint 2
Do we need to sum every number to the left and right of an index each time?
Hint 3
Use a prefix sum array where prefix[i] = nums[0] + nums[1] + ... + nums[i].

"""

class Solution:
    def findMiddleIndex(self,nums:list[int])->int:
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        total_sum=prefix[-1]
        for i in range(len(nums)):
            left_sum = prefix[i-1] if i>0  else 0
            right_sum = total_sum-prefix[i]
            if left_sum == right_sum:
                return i
        return -1
sol = Solution()
print(sol.findMiddleIndex(nums = [2,3,-1,8,4]))
print(sol.findMiddleIndex(nums = [1,-1,4]))
print(sol.findMiddleIndex(nums = [2,5]))