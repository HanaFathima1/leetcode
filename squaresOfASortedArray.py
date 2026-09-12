"""

LC: 977. Squares of a Sorted Array

Solved 

Easy

Topics
Junior
Array
Two Pointers
Sorting
Weekly Contest 120

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
2,839,224/3.8M
Acceptance Rate
74.1%

"""
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res=[]
        for i in range(len(nums)):
            res.append(nums[i]**2)
        return sorted(res)
sol=Solution()
print(sol.sortedSquares(nums = [-4,-1,0,3,10]))


#or


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums)-1
        result = []
        while l <= r:
            if nums[l]**2 < nums[r]**2:
                result.append(nums[r]**2)
                r-=1
            else:
                result.append(nums[l]**2)
                l+=1
        return result[::-1] #reverse array