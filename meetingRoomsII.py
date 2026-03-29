"""

LC: 253.Meeting Rooms II

Medium

Hints
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
     

Recommended Time & Space Complexity

Hint 1
Try to visualize the meetings as line segments on a number line representing start and end times. The number of rooms required is the maximum number of overlapping meetings at any point on the number line. Can you think of a way to determine this efficiently?


Hint 2
We create two arrays, start and end, containing the start and end times of all meetings, respectively. After sorting both arrays, we use a two-pointer based approach. How do you implement this?


Hint 3
We use two pointers, s and e, for the start and end arrays, respectively. We also maintain a variable count to track the current number of active meetings. At each iteration, we increment s while the start time is less than the current end time and increase count, as these meetings must begin before the earliest ongoing meeting ends.


Hint 4
Then, we increment e and decrement count as a meeting has ended. At each step, we update the result with the maximum value of active meetings stored in count.

"""

import heapq

class Interval(object):
    def __init__(self,start,end):
        self.start=start
        self.end=end

class Solution:
    def minMeetingRooms(self, intervals:list[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        min_heap=[]
        for interval in intervals:
            if min_heap and min_heap[0]<interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,interval.end)
        return len(min_heap)
sol=Solution()

intervals1 = [
    Interval(0, 30),
    Interval(5, 10),
    Interval(15, 20)
]

intervals2 = [
    Interval(5, 8),
    Interval(9, 15)
]

print(sol.minMeetingRooms(intervals1))  # Expected: 2
print(sol.minMeetingRooms(intervals2))  # Expected: 1


#-------------explanation----------------:


import heapq

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        # Store the start time of the meeting
        self.start = start
        
        # Store the end time of the meeting
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        # Step 1: Sort all meetings by their start time
        # Reason:
        # We must assign rooms when meetings BEGIN,
        # so we process meetings in chronological start order
        intervals.sort(key=lambda x: x.start)

        # Min-heap to keep track of end times of meetings
        # currently using rooms
        # The smallest end time will always be at index 0
        min_heap = []

        # Step 2: Process each meeting one by one
        for interval in intervals:
            # If there is at least one room already in use
            # AND the meeting in that room finishes
            # before or exactly when the current meeting starts
            if min_heap and min_heap[0] <= interval.start:
                # That room is now free, so we reuse it
                # Remove the earliest ending meeting
                heapq.heappop(min_heap)

            # Assign a room to the current meeting
            # (either a reused room or a new room)
            # Push the current meeting's end time
            heapq.heappush(min_heap, interval.end)

        # Step 3: The size of the heap represents
        # the maximum number of rooms used at the same time
        return len(min_heap)

