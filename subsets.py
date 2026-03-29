# LC_78:SUBSETS

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res, sol = [], []
        
        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            #Don't pick nums[i]
            backtrack(i+1)
            
            #pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)
        return res
    
sol = Solution()
print(sol.subsets([1,2,3])) 