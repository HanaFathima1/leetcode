"""

LC: 128. Longest Consecutive Sequence

Attempted 
 
Medium

Topics
Array
Hash Table
Union-Find

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
3,632,733/7.7M
Acceptance Rate
47.2%

"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        count=1
        longest=1
        nums.sort()
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                count+=1
            else:
                count=1
            longest=max(longest,count)
        return longest
