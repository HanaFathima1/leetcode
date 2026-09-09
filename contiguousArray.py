"""

LC: 525. Contiguous Array

Medium

Topics
Principal
Array
Hash Table
Prefix Sum

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
738,410/1.4M
Acceptance Rate
52.3%

"""

def contiguousArray(nums):
    max_len=0
    for i in range(len(nums)):
        zero=0
        one=0
        for j in range(i,len(nums)):
            if nums[j]==0:
                zero+=1
            else:
                one+=1
            if zero==one:
                length=j-i+1
                max_len=max(max_len,length)
    return max_len
        

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        balance = 0
        result = 0
        lookup = {0:-1}
        for idx, val in enumerate(nums):
            balance += 1 if val == 1 else -1
            if balance in lookup:
                result = max(result, idx-lookup[balance])
            else:
                lookup[balance] = idx
        return result