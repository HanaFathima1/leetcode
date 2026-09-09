"""

LC: 560. Subarray Sum Equals K

Medium

Topics
Senior Staff
Array
Hash Table
Prefix Sum

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
2,734,215/5.7M
Acceptance Rate
48.1%

Hint 1
Will Brute force work here? Try to optimize it.
Hint 2
Can we optimize it by using some extra space?
Hint 3
What about storing sum frequencies in a hash table? Will it be useful?
Hint 4
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.

"""

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count=0
        prefix_sum=0
        prefix={0:1}
        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in prefix:
                count+=prefix[prefix_sum-k]
            prefix[prefix_sum]=prefix.get(prefix_sum,0)+1
        return count
#or
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            current_sum=0
            for j in range(i,len(nums)):
                current_sum+=nums[j]
                if current_sum==k:
                    count+=1
        return count
