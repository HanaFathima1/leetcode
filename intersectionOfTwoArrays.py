"""

LC: 349. Intersection of Two Arrays

Solved

Easy

Topics:
Array
Hash Table
Two Pointers
Binary Search
Sorting
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,622,903/2.1M
Acceptance Rate
76.8%

"""

from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            if num in nums2 and num not in result:
                result.append(num)
        return result
sol = Solution()
print(sol.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))