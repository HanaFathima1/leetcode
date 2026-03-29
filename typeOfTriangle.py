"""

LC: 3024. Type of Triangle

Solved

Easy

Topics:
Array
Math
Sorting
Biweekly Contest 123

You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.
Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

 

Example 1:

Input: nums = [3,3,3]
Output: "equilateral"
Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.
Example 2:

Input: nums = [3,4,5]
Output: "scalene"
Explanation: 
nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. 
Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
As all the sides are of different lengths, it will form a scalene triangle.
 

Constraints:

nums.length == 3
1 <= nums[i] <= 100
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
196,493/441.7K
Acceptance Rate
44.5%

Hint 1
The condition for a valid triangle is that for any two sides, the sum of their lengths must be greater than the third side.
Hint 2
Simply count the number of unique edge lengths after checking it’s a valid triangle.

"""

from typing import List
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        n = len(nums)
        l1, l2, l3 = nums[0], nums[1], nums[2]
        if n==3 and l1+l2>l3 and l2+l3>l1 and l1+l3>l2:
            if l1==l2==l3:
                return "equilateral"
            elif l1==l2 or l2==l3 or l1==l3:
                return "isosceles"
            elif l1!=l2 and l2!=l3 and l3!=l1 :
                return "scalene"
        else:
            return "none"
sol = Solution()
print(sol.triangleType(nums = [3,3,3]))
print(sol.triangleType(nums = [3,4,5]))