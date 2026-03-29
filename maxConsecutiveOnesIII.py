"""

LC: 1004. Max Consecutive Ones III

Medium

Topics
Array
Binary Search
Sliding Window
Prefix Sum
Weekly Contest 126

Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,222,837/1.8M
Acceptance Rate
66.9%

Hint 1
One thing's for sure, we will only flip a zero if it extends an existing window of 1s. Otherwise, there's no point in doing it, right? Think Sliding Window!
Hint 2
Since we know this problem can be solved using the sliding window construct, we might as well focus in that direction for hints. Basically, in a given window, we can never have > K zeros, right?
Hint 3
We don't have a fixed size window in this case. The window size can grow and shrink depending upon the number of zeros we have (we don't actually have to flip the zeros here!).
Hint 4
The way to shrink or expand a window would be based on the number of zeros that can still be flipped and so on.

"""

class Solution:
    def longestOnes(self,nums:list[int],k:int)->int:
        left=0
        max_len=0
        zero_count=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1
            while zero_count>k:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
sol = Solution()
print(sol.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(sol.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))
                
        