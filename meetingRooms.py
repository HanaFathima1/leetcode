"""

LC: 252. Meeting Rooms

Locked question 

Easy

Hints
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000


Recommended Time & Space Complexity

Hint 1
If two intervals are sorted in ascending order by their start values, they overlap if the start value of the second interval is less than the end value of the first interval. And these are called overlapping intervals.


Hint 2
A brute force approach would be to check every pair of intervals and return false if any overlap is found. This would be an O(n^2) solution. Can you think of a better way? Maybe you should visualize the given intervals as line segments.


Hint 3
We should sort the given intervals based on their start values, as this makes it easier to check for overlaps by comparing adjacent intervals. We then iterate through the intervals from left to right and return false if any adjacent intervals overlap.

"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.end)
        end=intervals[0].end
        for interval in intervals[1:]:
            if interval.start<end:
                return False
            end=interval.end
        return True
sol=Solution()
print(sol.canAttendMeetings([Interval(0,30),Interval(5,10),Interval(15,20)]))
print(sol.canAttendMeetings([Interval(5,8),Interval(9,15)]))