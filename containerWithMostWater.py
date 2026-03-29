# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

#two pointers
def containerWithMostWater(height):
    n = len(height)
    maxArea = 0
    left, right = 0, n-1
    
    while left < right:
            width = right - left
            area = width * min(height[left], height[right])
            maxArea = max(maxArea, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
    return maxArea
print(containerWithMostWater([1,8,6,2,5,4,8,3,7]))


#-----------------------

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0
        while left < right:
            maxWater = max(maxWater, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater