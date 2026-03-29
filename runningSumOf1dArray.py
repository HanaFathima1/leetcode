"""

LC:1480. Running Sum of 1d Array
Solved

Easy

Topics:
Array
Prefix Sum
Weekly Contest 193

Hint
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,151,211/2.5M
Acceptance Rate
86.9%

Hint 1
Think about how we can calculate the i-th number in the running sum from the (i-1)-th number.

"""

class Solution:
    def runningSum(self, nums:list[int]) -> list[int]:
        sum=0
        result=[]
        for i in range(len(nums)):
            sum+=nums[i]
            result.append(sum)
        return result
sol = Solution()
print(sol.runningSum([1,2,3,4]))
print(sol.runningSum([1,1,1,1,1]))
print(sol.runningSum([3,1,2,10,1]))
    
