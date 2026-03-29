"""

LC: 3186. Maximum Total Damage With Spell Casting

Medium

Topics
Array
Hash Table
Two Pointers
Binary Search
Dynamic Programming
Sorting
Counting
Weekly Contest 402

Hint
A magician has various spells.

You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.

Each spell can be cast only once.

Return the maximum possible total damage that a magician can cast.

 

Example 1:

Input: power = [1,1,3,4]

Output: 6

Explanation:

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

Example 2:

Input: power = [7,1,6,6]

Output: 13

Explanation:

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

 

Constraints:

1 <= power.length <= 105
1 <= power[i] <= 109
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
89,414/207.2K
Acceptance Rate
43.1%

Hint 1
If we ever decide to use some spell with power x, then we will use all spells with power x.
Hint 2
Think of dynamic programming.
Hint 3
dp[i][j] represents the maximum damage considering up to the i-th unique spell and j represents the number of spells skipped (up to 3 as per constraints).

"""
from collections import Counter
class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt.keys())
        f = [0] * (len(a)+1)
        j = 0
        for i, x in enumerate(a):
            while a[j]<x-2:
                j += 1
            f[i+1] = max(f[i], f[j]+x*cnt[x])
        return f[-1]
sol = Solution()
print(sol.maximumTotalDamage([1,1,3,4]))
print(sol.maximumTotalDamage([7,1,6,6]))