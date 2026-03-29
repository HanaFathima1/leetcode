"""

LC: 179. Largest Number

Medium

Topics
Array
String
Greedy
Sorting

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
749,616/1.8M
Acceptance Rate
41.7%

"""

from typing import List
class Solution:
    def largestNumber(self, nums:List[int]) -> str:
        nums = list(map(str,nums))
        nums.sort(key=lambda x : x*10, reverse=True)
        result = ''.join(nums)
        return '0' if result[0] == '0' else result
sol = Solution()
print(sol.largestNumber([10,2]))
print(sol.largestNumber([3,30,34,5,9]))

# 🔹 Example Dry Run

# Input:

# nums = [3, 30, 34, 5, 9]


# Step 1: Convert to strings →
# ["3", "30", "34", "5", "9"]

# Step 2: Sorting with x*10:

# "3"*10 = "3333333333"

# "30"*10 = "3030303030"

# "34"*10 = "3434343434"

# "5"*10 = "5555555555"

# "9"*10 = "9999999999"

# Sorting in descending order →
# ["9", "5", "34", "3", "30"]

# Step 3: Join →
# "9534330"

# ✅ Correct output.

# 🔹 Edge Case Check

# Input:

# nums = [0, 0]


# Strings → ["0", "0"]

# Sort → ["0", "0"]

# Join → "00"

# Fix with return '0' → ✅ "0"

