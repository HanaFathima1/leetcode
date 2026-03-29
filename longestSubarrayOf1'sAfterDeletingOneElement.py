"""

LC: 1493. Longest Subarray of 1's After Deleting One Element

Medium

Topics
Array
Dynamic Programming
Sliding Window
Biweekly Contest 29

Hint
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
596,069/840.6K
Acceptance Rate
70.9%

Hint 1
Maintain a sliding window where there is at most one zero in it.

"""

class Solution:
    def longestSubarray(self,nums:list[int])->int:
        left=0
        max_len=0
        zero_count=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1
            while zero_count>1:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            max_len=max(max_len,right-left)
        return max_len
sol = Solution()
print(sol.longestSubarray(nums = [1,1,0,1]))       
print(sol.longestSubarray(nums = [0,1,1,1,0,1,1,0,1]))  
print(sol.longestSubarray(nums = [1,1,1]))   