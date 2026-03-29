"""

LC: 169. Majority Element

Attempted

Easy

Topics:
Array
Hash Table
Divide and Conquer
Sorting
Counting

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
4,733,426/7.2M
Acceptance Rate
65.9%

"""

from collections import Counter
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num in count:
            if count[num] > len(nums)//2:
                return num

sol = Solution()
print(sol.majorityElement(nums = [3,2,3]))
print(sol.majorityElement(nums = [2,2,1,1,1,2,2]))