"""

LC: 3349. Adjacent Increasing Subarrays Detection I

Easy

Topics
Array
Weekly Contest 423

Hint
Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3

Output: true

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, so the result is true.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5

Output: false

 

Constraints:

2 <= nums.length <= 100
1 < 2 * k <= nums.length
-1000 <= nums[i] <= 1000
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
96,425/207.8K
Acceptance Rate
46.4%

Hint 1
Store the longest decreasing subarray starting and ending at an index.

"""

class Solution:
    def hasIncreasingSubarrays(self, nums:list[int], k:int) -> bool:
        n = len(nums)
        for a in range(0,n - 2*k + 1):
            if all(nums[j] < nums[j+1] for j in range(a, a+k-1)):
                if all(nums[j] < nums[j+1] for j in range(a+k, a + 2*k -1)):
                    return True
        return False
sol = Solution()
print(sol.hasIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1], k = 3))
print(sol.hasIncreasingSubarrays(nums = [1,2,3,4,4,4,4,5,6,7], k = 5))