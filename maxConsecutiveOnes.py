"""

LC:  485. Max Consecutive Ones

Easy

Topics
Array

Hint
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,942,440/3M
Acceptance Rate
63.8%

Hint 1
You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window. How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.

"""

class Solution:
    def findMaxConsecutiveOnes(self,nums:list[int]) -> int:
        count=0
        max_len=0
        for i in nums:
            if i==1:
                count+=1
                max_len=max(max_len,count)
            else:
                count=0
        return max_len
sol=Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))