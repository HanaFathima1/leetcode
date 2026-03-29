"""

LC: 39. Combination Sum

Medium

Topics
Array
Backtracking

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
3,018,186/4M
Acceptance Rate
76.1%

"""

class Solution:
    def combinationSum(self,candidates:list[int],target:int)->list[list[int]]:
        res=[]
        def backtrack(start,path,total):
            if total==target:
                res.append(path[:])
                return
            if total>target:
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i,path,total+candidates[i])
                path.pop()
        backtrack(0,[],0)
        return res
sol=Solution()
print(sol.combinationSum(candidates = [2,3,6,7], target = 7))
print(sol.combinationSum(candidates = [2,3,5], target = 8))
print(sol.combinationSum(candidates = [2], target = 1))



#------dry run--------
"""🌳 FULL RECURSION TREE DRY RUN

I’ll write it like a tree.

Level 0
path = []
sum = 0
start = 0

Loop from index 0 → 3

🔹 i = 0 → choose 2
path = [2]
sum = 2
call backtrack(0, [2], 2)
🔹 Level 1 (inside [2])

Loop from index 0 → 3

i = 0 → choose 2 again
path = [2,2]
sum = 4
call backtrack(0, [2,2], 4)
🔹 Level 2 (inside [2,2])

Loop from 0 → 3

i = 0 → choose 2 again
path = [2,2,2]
sum = 6
call backtrack(0, [2,2,2], 6)
🔹 Level 3 (inside [2,2,2])

Loop from 0 → 3

i = 0 → choose 2
path = [2,2,2,2]
sum = 8

8 > 7 ❌ STOP
Return
Undo last 2

Back to:

path = [2,2,2]
sum = 6
i = 1 → choose 3
path = [2,2,2,3]
sum = 9

9 > 7 ❌ STOP
Undo

i = 2 → choose 6
sum = 12 ❌ STOP

Undo

i = 3 → choose 7
sum = 13 ❌ STOP

Undo

All options exhausted.
Return to previous level.

Back to Level 2

We were at:

path = [2,2]
sum = 4

Continue loop.

i = 1 → choose 3
path = [2,2,3]
sum = 7

🎉 sum == target
Save:

[2,2,3]

Return
Undo last 3

Back to:

path = [2,2]
sum = 4
i = 2 → choose 6
sum = 10 ❌ STOP

Undo

i = 3 → choose 7
sum = 11 ❌ STOP

Undo

Return to previous level.

Back to Level 1

We were at:

path = [2]
sum = 2

Continue loop.

i = 1 → choose 3
path = [2,3]
sum = 5
call backtrack(1, [2,3], 5)
Inside [2,3]

Loop from index 1 → 3

i = 1 → choose 3
path = [2,3,3]
sum = 8 ❌ STOP

Undo

i = 2 → choose 6
sum = 11 ❌ STOP

Undo

i = 3 → choose 7
sum = 12 ❌ STOP

Undo

Return.

i = 2 → choose 6
path = [2,6]
sum = 8 ❌ STOP

Undo

i = 3 → choose 7
path = [2,7]
sum = 9 ❌ STOP

Undo

Return to root.

Back to Level 0
path = []
sum = 0
i = 1 → choose 3
path = [3]
sum = 3
call backtrack(1, [3], 3)

Inside [3]

i = 1 → choose 3
[3,3] sum=6
choose 3 again
[3,3,3] sum=9 ❌

Undo.

Continue.

All branches fail.

Return.

i = 2 → choose 6
path = [6]
sum = 6

Try reuse 6:

[6,6] sum=12 ❌

Return.

i = 3 → choose 7
path = [7]
sum = 7

🎉 SAVE:

[7]

Return.

✅ FINAL RESULT
[[2,2,3], [7]]


The recursion tree looks like:

              []
         /      |      |      \
       2        3      6       7
     / | \ 
    2  3  ...
   /
  2

We explore one branch fully → then backtrack."""


"""

FULL BACKTRACKING TREE DIAGRAM
                              ([], 0)
            ------------------------------------------------
           /                    |               |           \
        ([2],2)              ([3],3)        ([6],6)       ([7],7) ✔
          |
   -------------------------
  /        |       |       \
[2,2]4  [2,3]5  [2,6]8❌  [2,7]9❌
   |
-----------------------
|        |       |     \
[2,2,2]6 [2,2,3]7✔ [2,2,6]10❌ [2,2,7]11❌
   |
-----------------------
|       |      |       \
[2,2,2,2]8❌ ...


🔥 Let’s Walk Through It Slowly
Root Node
([], 0)

Loop through all candidates.

Choose 2
([2], 2)

Try again from index 0 (reuse allowed).

Choose 2 again
([2,2], 4)
Choose 2 again
([2,2,2], 6)
Choose 2 again
([2,2,2,2], 8) ❌

8 > 7 → STOP (prune branch)

Backtrack to [2,2,2]

Try 3
([2,2,3], 7) ✔

Save solution.

Backtrack.

Try 6
([2,2,6], 10) ❌

Backtrack.

Try 7
([2,2,7], 11) ❌

Backtrack to [2]

Try 3 from root
([3], 3)
Try 3 again
([3,3], 6)
Try 3 again
([3,3,3], 9) ❌

Backtrack.

Try 6:

([3,6], 9) ❌

Try 7:

([3,7], 10) ❌

Backtrack to root.

Try 6 from root
([6], 6)

Try 6 again:

([6,6], 12) ❌

Try 7:

([6,7], 13) ❌

Backtrack.

Try 7 from root
([7], 7) ✔

Save solution.

✅ FINAL SOLUTIONS
[2,2,3]
[7]

"""