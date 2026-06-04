"""

LC: 303. Range Sum Query - Immutable

Easy

Topics
Array
Design
Prefix Sum

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
941,428/1.3M
Acceptance Rate
72.3%

"""


class NumArray: 
    def __init__(self, nums:list[int]):
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1]+num)
    def sumRange(self, left:int, right:int) -> int:
        return self.prefix_sum[right+1]-self.prefix_sum[left]
sol = NumArray([-2,0,3,-5,2,-1])
print(sol.sumRange(0,2))



#-----------------explanation---------------

class NumArray:

    def __init__(self, nums: List[int]):
        
        # Create a prefix sum array and initialize it with 0.
        # prefix_sum[i] will store the sum of the first i elements.
        self.prefix_sum = [0]

        # Build the prefix sum array
        for num in nums:
            
            # self.prefix_sum[-1] gives the last prefix sum calculated
            # Add the current number to it and append the result
            self.prefix_sum.append(self.prefix_sum[-1] + num)

        # Example:
        # nums = [-2, 0, 3, -5, 2, -1]
        #
        # prefix_sum becomes:
        # [0, -2, -2, 1, -4, -2, -3]
        #
        # Meaning:
        # prefix_sum[0] = 0
        # prefix_sum[1] = -2
        # prefix_sum[2] = -2      (-2 + 0)
        # prefix_sum[3] = 1       (-2 + 0 + 3)
        # prefix_sum[4] = -4      (-2 + 0 + 3 - 5)
        # prefix_sum[5] = -2      (-2 + 0 + 3 - 5 + 2)
        # prefix_sum[6] = -3      (-2 + 0 + 3 - 5 + 2 - 1)


    def sumRange(self, left: int, right: int) -> int:

        # To find the sum from index left to right:
        #
        # prefix_sum[right + 1]
        # = sum of elements from index 0 to right
        #
        # prefix_sum[left]
        # = sum of elements before index left
        #
        # Subtracting them removes the unwanted part
        #
        # Formula:
        # Range Sum(left, right)
        # = prefix_sum[right + 1] - prefix_sum[left]

        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Example
sol = NumArray([-2, 0, 3, -5, 2, -1])

# sumRange(0, 2)
# = (-2 + 0 + 3)
# = 1
#
# prefix_sum[3] - prefix_sum[0]
# = 1 - 0
# = 1

print(sol.sumRange(0, 2))