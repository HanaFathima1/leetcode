"""

LC: 643. Maximum Average Subarray I

Easy

Topics
Mid Level
Array
Sliding Window

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,405,727/2.9M
Acceptance Rate
49.2%

"""


# Brute-force code
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        # Start with a very small value
        max_average = float('-inf')

        # i represents the starting index
        # of each subarray
        for i in range(len(nums) - k + 1):

            # Calculate the sum of the current subarray
            window_sum = 0

            # j goes through k elements
            for j in range(i, i + k):
                window_sum += nums[j]

            # Calculate average
            average = window_sum / k

            # Update maximum average
            max_average = max(max_average, average)

        return max_average


"""
Dry run

Input:

nums = [1, 12, -5, -6, 50, 3]
k = 4
First loop: i = 0

We take:

[1, 12, -5, -6]

Sum:

1 + 12 - 5 - 6
= 2

Average:

2 / 4
= 0.5

So:

max_average = 0.5
i = 1

Take:

[12, -5, -6, 50]

Sum:

12 - 5 - 6 + 50
= 51

Average:

51 / 4
= 12.75

Update:

max_average = 12.75
i = 2

Take:

[-5, -6, 50, 3]

Sum:

-5 - 6 + 50 + 3
= 42

Average:

42 / 4
= 10.5

10.5 is less than 12.75, so:

max_average = 12.75

Final answer:

12.75
"""
#===========================
class Solution:
    def findMaxAverage(self, nums:list[int], k:int) -> float:
        window_sum=sum(nums[:k])
        max_sum=window_sum
        
        for i in range(k,len(nums)):
            window_sum=window_sum-nums[i-k]+nums[i]
            max_sum=max(window_sum, max_sum)
        return max_sum/k

sol=Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3],4))

"""
Our input is:

nums = [1, 12, -5, -6, 50, 3]
        0   1   2   3   4   5

And:

k = 4

So we need subarrays of exactly 4 elements.

The possible windows are:

[1, 12, -5, -6]
[12, -5, -6, 50]
[-5, -6, 50, 3]
Step 1️⃣

This line:

window_sum = sum(nums[:k])

means:

nums[:4]

which gives:

[1, 12, -5, -6]

Calculate:

1 + 12 + (-5) + (-6)
= 2

Therefore:

window_sum = 2
Step 2️⃣
max_sum = window_sum

So:

max_sum = 2

Currently our maximum window is:

[1, 12, -5, -6]

with sum:

2
Step 3️⃣ — Start the loop
for i in range(k, len(nums)):

We have:

k = 4
len(nums) = 6

So:

range(4, 6)

gives:

i = 4
i = 5

Why start at 4?

Because indices:

0, 1, 2, 3

were already used for our first window.

🟢 Iteration 1 — i = 4

Current array:

[1, 12, -5, -6, 50, 3]
 0   1   2   3   4   5

The new element is:

nums[i]

which is:

nums[4] = 50

Our current window is:

[1, 12, -5, -6]

We want the next window:

[12, -5, -6, 50]

So:

Remove the outgoing element
nums[i-k]

Substitute:

i = 4
k = 4

Therefore:

nums[4-4]
= nums[0]
= 1

So remove 1.

Add the incoming element
nums[i]
= nums[4]
= 50

Therefore:

window_sum = window_sum - nums[i-k] + nums[i]

becomes:

window_sum = 2 - 1 + 50
window_sum = 51

Our new window is:

[12, -5, -6, 50]

and its sum is:

51
Update max_sum

Before:

max_sum = 2

Now:

max_sum = max(window_sum, max_sum)

becomes:

max_sum = max(51, 2)

Therefore:

max_sum = 51
🟢 Iteration 2 — i = 5

Now:

nums = [1, 12, -5, -6, 50, 3]
                          ↑
                          i=5

The current window is:

[12, -5, -6, 50]

We want:

[-5, -6, 50, 3]

Again:

window_sum = window_sum - nums[i-k] + nums[i]

Substitute:

window_sum = 51
i = 5
k = 4
Remove outgoing element
nums[i-k]

becomes:

nums[5-4]
= nums[1]
= 12

So remove 12.

Add incoming element
nums[i]
= nums[5]
= 3

Therefore:

window_sum = 51 - 12 + 3
window_sum = 42

New window:

[-5, -6, 50, 3]

Sum:

42
Update max_sum

Currently:

max_sum = 51

And:

window_sum = 42

Therefore:

max_sum = max(42, 51)

So:

max_sum = 51
Step 4️⃣ — Return the average

After the loop:

max_sum = 51

We have:

return max_sum / k

So:

51 / 4
= 12.75

Therefore:

12.75
📊 Complete dry-run table
i	Window	Outgoing	Incoming	window_sum	max_sum
—	[1,12,-5,-6]	—	—	2	2
4	[12,-5,-6,50]	1	50	51	51
5	[-5,-6,50,3]	12	3	42	51

Finally:

max_sum = 51

and:

maximum average = 51 / 4 = 12.75
"""