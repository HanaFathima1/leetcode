"""

LC: 3005. Count Elements With Maximum Frequency

Attempted

Easy

Topics:
Array
Hash Table
Counting
Weekly Contest 380

Hint
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

 

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
329,061/414.3K
Acceptance Rate
79.4%

Hint 1
Find frequencies of all elements of the array.
Hint 2
Find the elements that have the maximum frequencies and count their total occurrences.

"""

from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self,nums:List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())
        result = 0
        for num in count:
            if count[num] == max_freq:
                result += count[num]
        return result
sol = Solution()
print(sol.maxFrequencyElements([1,2,2,3,1,4]))
print(sol.maxFrequencyElements([1,2,3,4,5]))
            
        