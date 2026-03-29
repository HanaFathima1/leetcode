"""

LC: 334. Increasing Triplet Subsequence

Attempted

Medium

Topics
Array
Greedy

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (3, 4, 5), because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
860,180/2.2M
Acceptance Rate
39.1%

"""

class Solution:
    def increasingTriplet(self,nums:list[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else: # Found num > second > first
                return True
        return False
sol = Solution()
print(sol.increasingTriplet(nums = [1,2,3,4,5]))
print(sol.increasingTriplet(nums = [5,4,3,2,1]))
print(sol.increasingTriplet(nums = [2,1,5,0,4,6]))

"""

| Variable | Meaning                                 |
| -------- | --------------------------------------- |
| `first`  | Smallest element seen so far            |
| `second` | Smallest element greater than `first`   |
| `num`    | Current number while scanning the array |



🧠 Dry Run Example

nums = [2, 1, 5, 0, 4, 6]

num	first	second	action
2	2	∞	first updated
1	1	∞	smaller → first updated
5	1	5	second updated
0	0	5	smaller → first updated
4	0	4	second updated
6	0	4	✅ num > second → return True

✅ Increasing triplet is (0, 4, 6)


⏱️ Complexity

Time: O(n) — single traversal
Space: O(1) — constant extra space

"""   