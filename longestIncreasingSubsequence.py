"""

LC: 300. Longest Increasing Subsequence

Medium

Topics
Array
Binary Search
Dynamic Programming

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

Seen this question in a real interview before?
1/6
Yes
No
Accepted
2,663,458/4.5M
Acceptance Rate
59.5%

"""

class Solution:
    def lengthOfLIS(self, nums):

        n = len(nums)

        # dp[i]
        #
        # Length of LIS ending at index i
        #
        dp = [1] * n

        # Try every element
        for i in range(n):

            # Look at all previous elements
            for j in range(i):

                # Can we extend the subsequence?
                if nums[j] < nums[i]:

                    dp[i] = max(
                        dp[i],
                        dp[j] + 1
                    )

        # Longest LIS anywhere in array
        return max(dp)
sol = Solution()
print(sol.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS(nums = [0,1,0,3,2,3]))
print(sol.lengthOfLIS(nums = [7,7,7,7,7,7,7]))

"""

Easy Dry Run

Input:

nums = [10,9,2,5,3,7]

Initialize:

dp = [1,1,1,1,1,1]
i = 0

Nothing before it.

dp = [1,1,1,1,1,1]
i = 1

Value:

9

Check:

10 < 9

False

dp = [1,1,1,1,1,1]
i = 2

Value:

2

Check previous:

10 < 2

False

9 < 2

False

dp = [1,1,1,1,1,1]
i = 3

Value:

5

Check:

10 < 5

False

9 < 5

False

2 < 5

True

dp[3]
=
max(1, dp[2]+1)
=
max(1,2)
=
2

DP:

[1,1,1,2,1,1]
i = 4

Value:

3

Check:

2 < 3

True

dp[4] = 2

DP:

[1,1,1,2,2,1]
i = 5

Value:

7

Check:

2 < 7
dp[5] = 2

Check:

5 < 7
dp[5]
=
max(2, dp[3]+1)
=
max(2,3)
=
3

Check:

3 < 7
dp[5]
=
max(3, dp[4]+1)
=
3

Final:

[1,1,1,2,2,3]

"""


"""

Complexity
Time

Two nested loops:

O(n²)
Space

DP array:

O(n)

"""