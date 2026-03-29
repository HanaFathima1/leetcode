"""

LC: 1488. Avoid Flood in The City

Medium

Topics:
Array
Hash Table
Binary Search
Greedy
Heap (Priority Queue)
Weekly Contest 194

Hint
Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.

 

Example 1:

Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.
Example 2:

Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
Example 3:

Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.
 

Constraints:

1 <= rains.length <= 105
0 <= rains[i] <= 109
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
98,568/267K
Acceptance Rate
36.9%

Hint 1
Keep An array of the last day there was rains over each city.
Hint 2
Keep an array of the days you can dry a lake when you face one.
Hint 3
When it rains over a lake, check the first possible day you can dry this lake and assign this day to this lake.

"""
import bisect
class Solution:
    def avoidFlood(self, rains:list[int]) -> list[int]:
        n = len(rains)
        ans = [-1] * n
        full = {}        # lake -> last day it was filled
        dry_days = []    # indices of dry days (rains[i] == 0)

        for i, lake in enumerate(rains):
            if lake == 0:
                # dry day, we can decide later which lake to dry
                dry_days.append(i)
                ans[i] = 1  # temporary (we’ll overwrite later if needed)
            else:
                # it's raining on lake
                if lake in full:
                    # need to find a dry day after last rain of this lake
                    last_rain_day = full[lake]
                    idx = bisect.bisect_right(dry_days, last_rain_day)
                    
                    if idx == len(dry_days):
                        return []  # no dry day available, flood happens
                    
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake  # dry this lake on that dry day
                    dry_days.pop(idx)    # remove used dry day
                # mark this lake as filled
                full[lake] = i
        
        return ans

sol = Solution()
print(sol.avoidFlood(rains = [1,2,3,4]))
print(sol.avoidFlood(rains = [1,2,0,0,2,1]))
print(sol.avoidFlood(rains = [1,2,0,1,2]))
    
    
"""

Step-by-step:

Day	rains[i]	Action	ans	dry_days	full
0	1	Lake 1 filled	[-1]	[]	{1:0}
1	2	Lake 2 filled	[-1,-1]	[]	{1:0,2:1}
2	0	Dry day saved	[-1,-1,1]	[2]	{1:0,2:1}
3	1	Need to dry lake 1 after day 0 → use 2	[-1,-1,1,-1]	[]	{1:3,2:1}
4	2	No dry day left → Flood? No, fine now	[-1,-1,1,-1,-1]	[]	{1:3,2:4}

✅ Output:

[-1, -1, 1, -1, -1]

"""