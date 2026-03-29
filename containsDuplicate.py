"""

LC: 217. Contains Duplicate

Attempted

Easy

Topics
Array
Hash Table
Sorting
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
6,119,813/9.6M
Acceptance Rate
64.1%

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res=[]
        for num in nums:
            if num in res:
                return True
            res.append(num)
        return False


        # #or
        s=set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

        #or
        return len(nums)!=len(set(nums))