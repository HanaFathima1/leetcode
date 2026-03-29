"""

LC: 40. Combination Sum II

Medium

Topics
Array
Backtracking

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,646,491/2.8M
Acceptance Rate
59.0%

"""

class Solution:
    def combinationSum2(self,candidates:list[int],target:int)->list[list[int]]:
        res=[]
        candidates.sort()
        def backtrack(start,path,total):
            if total==target:
                res.append(path[:])
                return
            if total>target:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path,total+candidates[i])
                path.pop()
        backtrack(0,[],0)
        return res
sol=Solution()
print(sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
print(sol.combinationSum2(candidates = [2,5,2,1,2], target = 5))
                