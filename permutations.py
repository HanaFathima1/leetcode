# LC_46.PERMUTATIONS

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]


class Solution:
    def permute(self, nums:list[int]) -> list[list[int]]:
        n = len(nums)
        res, sol = [], []
        
        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
                    
        backtrack()
        return res
    
sol = Solution()
print(sol.permute([1,2,3]))