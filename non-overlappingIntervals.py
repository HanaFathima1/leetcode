"""

LC: 435. Non-overlapping Intervals

Medium

Topics
Array
Dynamic Programming
Greedy
Sorting

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
950,205/1.7M
Acceptance Rate
56.6%

"""

class Solution:
    def eraseOverlapIntervals(self,intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        end=intervals[0][1]
        remove=0
        for s,e in intervals[1:]:
            if s<end:
                remove+=1
            else:
                end=e
        return remove
sol=Solution()
print(sol.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
print(sol.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))
print(sol.eraseOverlapIntervals(intervals = [[1,2],[2,3]]))