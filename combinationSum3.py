"""

LC: 216. Combination Sum III

Medium

Topics
Array
Backtracking

Companies
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

Constraints:

2 <= k <= 9
1 <= n <= 60
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
782,739/1.1M
Acceptance Rate
73.0%

"""

class Solution:
    def combinationSum3(self,k:int,n:int):
        res=[]
        def backtrack(start,path,total):
            if total==n and len(path)==k:
                res.append(path[:])
                return
            if total>n or len(path)>k:
                return
            for i in range(start,10):
                path.append(i)
                backtrack(i+1,path,total+i)
                path.pop()
        backtrack(1,[],0)
        return res
sol=Solution()
print(sol.combinationSum3(k = 3, n = 7))
print(sol.combinationSum3(k = 3, n = 9))
print(sol.combinationSum3(k = 4, n = 1))


"""

dry run:

1️⃣ Dry Run Example — Combination Sum III
Input
k = 3
n = 9

We must choose 3 numbers from 1–9 whose sum is 9.

Start
path = []
sum = 0
start = 1
Step 1 — Choose 1
path = [1]
sum = 1

Next numbers can start from 2.

Step 2 — Choose 2
path = [1,2]
sum = 3

Next numbers start from 3.

Try 3
path = [1,2,3]
sum = 6

Length = 3 but sum ≠ 9 ❌
Backtrack.

Try 4
path = [1,2,4]
sum = 7

Length = 3 but sum ≠ 9 ❌
Backtrack.

Try 5
path = [1,2,5]
sum = 8

Length = 3 but sum ≠ 9 ❌
Backtrack.

Try 6
path = [1,2,6]
sum = 9

✔ Valid solution

[1,2,6]

Backtrack.

Step 3 — Continue from [1]

Try next number.

Choose 3
path = [1,3]
sum = 4

Try 4

path = [1,3,4]
sum = 8

❌

Try 5

path = [1,3,5]
sum = 9

✔ Save

[1,3,5]

Backtrack.

Step 4 — Continue

Choose 4

path = [1,4]
sum = 5

Try 4,5,6...

None produce valid length-3 sum 9.

Backtrack.

Step 5 — Start with 2
path = [2]
sum = 2

Choose 3

path = [2,3]
sum = 5

Try 4

path = [2,3,4]
sum = 9

✔ Save

[2,3,4]

Backtrack.

Final Result
[
[1,2,6],
[1,3,5],
[2,3,4]
]
Tree Visualization
                []
          /      |      \
         1       2       3
       / | \    / \
   [1,2,6]✔ [2,3,4]✔
      |
   [1,3,5]✔

"""