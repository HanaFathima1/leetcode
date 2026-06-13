"""

LC: 494. Target Sum

Medium

Topics
Senior Staff
Array
Dynamic Programming
Backtracking

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,109,317/2.1M
Acceptance Rate
52.3%

"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} #(index, total) -> # of ways
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = (backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i]))
            return dp[(i, total)]
        return backtrack(0, 0)


#EXPLANATION

class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # Memoization dictionary
        # Key   = (current index, current total)
        # Value = number of ways to reach target from this state
        dp = {} #(index, total) -> # of ways

        def backtrack(i, total):

            # Base case:
            # If we have processed all elements in nums
            if i == len(nums):

                # If the current total equals target,
                # this is one valid way
                return 1 if total == target else 0

            # If this state was already solved before,
            # return the stored answer instead of recomputing
            if (i,total) in dp:

                return dp[(i, total)]

            # At each index we have 2 choices:
            #
            # 1. Add nums[i] to the current total
            #    backtrack(i+1, total+nums[i])
            #
            # 2. Subtract nums[i] from the current total
            #    backtrack(i+1, total-nums[i])
            #
            # Total ways from this state =
            # ways from '+' choice + ways from '-' choice
            dp[(i, total)] = (
                backtrack(i+1, total+nums[i]) +
                backtrack(i+1, total-nums[i])
            )

            # Return the computed number of ways
            # for the current state
            return dp[(i, total)]

        # Start from index 0 with total = 0
        return backtrack(0, 0)
    
#DRY RUN
"""
nums = [1,1,1]
target = 1

We start with:

backtrack(0,0)
Complete Recursive Tree
backtrack(0,0)
│
├── +1 → backtrack(1,1)
│   │
│   ├── +1 → backtrack(2,2)
│   │   │
│   │   ├── +1 → backtrack(3,3) = 0
│   │   │
│   │   └── -1 → backtrack(3,1) = 1
│   │
│   └── -1 → backtrack(2,0)
│       │
│       ├── +1 → backtrack(3,1) = 1
│       │
│       └── -1 → backtrack(3,-1) = 0
│
└── -1 → backtrack(1,-1)
    │
    ├── +1 → backtrack(2,0)
    │   │
    │   ├── +1 → backtrack(3,1) = 1
    │   │
    │   └── -1 → backtrack(3,-1) = 0
    │
    └── -1 → backtrack(2,-2)
        │
        ├── +1 → backtrack(3,-1) = 0
        │
        └── -1 → backtrack(3,-3) = 0
Leaf Node Evaluation

When:

i == len(nums)

we check:

return 1 if total == target else 0

Since:

target = 1

the leaves become:

State	Return
(3,3)	0
(3,1)	1
(3,1)	1
(3,-1)	0
(3,1)	1
(3,-1)	0
(3,-1)	0
(3,-3)	0
Returning Back Up
State (2,2)
backtrack(2,2)
=
backtrack(3,3)
+
backtrack(3,1)

= 0 + 1
= 1

Store:

dp[(2,2)] = 1
State (2,0)
backtrack(2,0)
=
backtrack(3,1)
+
backtrack(3,-1)

= 1 + 0
= 1

Store:

dp[(2,0)] = 1
State (1,1)
backtrack(1,1)
=
backtrack(2,2)
+
backtrack(2,0)

= 1 + 1
= 2

Store:

dp[(1,1)] = 2
State (1,-1)

Notice:

backtrack(2,0)

was already calculated.

So:

if (2,0) in dp:
    return dp[(2,0)]

returns:

1

No recursion happens again.

Now calculate:

backtrack(2,-2)
=
0 + 0
=
0

Store:

dp[(2,-2)] = 0

Therefore:

backtrack(1,-1)
=
1 + 0
=
1

Store:

dp[(1,-1)] = 1
Final State (0,0)
backtrack(0,0)
=
backtrack(1,1)
+
backtrack(1,-1)

=
2 + 1

=
3

Store:

dp[(0,0)] = 3
DP Table Formed

After execution:

dp = {
    (2,2): 1,
    (2,0): 1,
    (1,1): 2,
    (2,-2): 0,
    (1,-1): 1,
    (0,0): 3
}
"""