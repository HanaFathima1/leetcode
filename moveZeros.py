"""

LC: 283. Move Zeroes

Easy

Topics
Array
Two Pointers

Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
4,407,802/7M
Acceptance Rate
63.1%

Hint 1
In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.
Hint 2
A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.

"""

def moveZeros(nums):
    left=0
    for right in range(len(nums)):
        if nums[right]!=0:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
    return nums
print(moveZeros([0,1,0,3,12]))
            
            
            
