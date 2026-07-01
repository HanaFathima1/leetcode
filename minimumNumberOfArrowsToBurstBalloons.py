"""

LC: 452. Minimum Number of Arrows to Burst Balloons

Medium

Topics
Junior
Array
Greedy
Sorting

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
 

Constraints:

1 <= points.length <= 105
points[i].length == 2
-231 <= xstart < xend <= 231 - 1
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
795,485/1.3M
Acceptance Rate
61.5%

"""

#=========================PROBLEM EXPLANATION===============================
"""
LeetCode 452 - Minimum Number of Arrows to Burst Balloons

Problem Summary:
---------------
Each balloon is represented as an interval [start, end].

A balloon occupies every position from start to end (inclusive).

We can shoot an arrow at any x-coordinate.
An arrow bursts all balloons whose interval contains that x-coordinate.

Goal:
-----
Find the minimum number of arrows needed to burst all balloons.

Key Observation:
----------------
If multiple balloons overlap, a single arrow can burst all of them.

Example:
---------
Balloons:
[1,6]
[2,8]

These intervals overlap.

If we shoot an arrow at x = 6 (or any position between 2 and 6),
both balloons burst.

Therefore:
Answer = 1 arrow

Another Example:
----------------
Balloons:
[1,2]
[3,4]

These intervals do not overlap.

One arrow cannot burst both balloons.

Need:
- 1 arrow for [1,2]
- 1 arrow for [3,4]

Answer = 2 arrows

What the Problem is Really Asking:
----------------------------------
Group together all overlapping balloons.

Each overlapping group can be burst using one arrow.

Count the minimum number of arrows required to cover all balloon intervals.

Pattern:
--------
Intervals + Greedy + Sorting

Important Idea:
---------------
When balloons overlap, try to use the same arrow.
A new arrow is needed only when the next balloon starts after
the current overlapping region ends.
"""

class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[1])
        arrows = 1
        current_end = points[0][1]
        for start,end in points[1:]:
            if start > current_end:
                arrows+=1
                current_end = end
        return arrows
sol=Solution()
print(sol.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))
print(sol.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]]))
print(sol.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]))

#=========================CODE EXPLANATION=====================
class Solution:
    def findMinArrowShots(self, points):
        
        # If there are no balloons, no arrows are needed
        if not points:
            return 0

        # Sort balloons based on their ending position
        # This helps us place an arrow at the earliest possible end
        points.sort(key=lambda x: x[1])

        # We need at least one arrow for the first balloon
        arrows = 1

        # Shoot the first arrow at the end of the first balloon
        current_end = points[0][1]

        # Check all remaining balloons
        for start, end in points[1:]:

            # If the current balloon starts AFTER the position
            # where our arrow was shot, there is no overlap.
            # We need a new arrow.
            if start > current_end:
                arrows += 1          # Use one more arrow
                current_end = end    # Shoot it at this balloon's end

            # Otherwise:
            # start <= current_end
            # The current balloon overlaps with the previous group.
            # The arrow already shot at current_end will burst it.
            # So, do nothing and continue.

        # Return the minimum number of arrows needed
        return arrows

#=========================DRY RUN======================
"""
Example
points = [[1,5], [2,6], [7,9], [8,10]]

Visualize the balloons:

[1---------5]
   [2---------6]

                [7-----9]
                   [8------10]
Step 1: Sort by Ending Position

Already sorted:

[[1,5], [2,6], [7,9], [8,10]]
Step 2: Shoot First Arrow

Take the first balloon:

[1,5]

Shoot an arrow at:

x = 5

Current state:

arrows = 1
current_end = 5

Visual:

[1---------5]  ← Arrow at 5
   [2---------6]
Step 3: Check Next Balloon

Balloon:

[2,6]

Check:

start = 2
current_end = 5

2 <= 5

This balloon contains position 5.

So the same arrow bursts it.

arrows = 1

No new arrow needed.

Step 4: Check Next Balloon

Balloon:

[7,9]

Check:

start = 7
current_end = 5

7 > 5

No overlap.

The arrow at 5 cannot reach this balloon.

Need a new arrow.

Shoot at:

x = 9

Update:

arrows = 2
current_end = 9

Visual:

[1---------5]   ← Arrow 1
   [2---------6]

                [7-----9] ← Arrow 2
                   [8------10]
Step 5: Check Last Balloon

Balloon:

[8,10]

Check:

start = 8
current_end = 9

8 <= 9

Overlap exists.

The arrow at 9 bursts it.

No new arrow needed.

arrows = 2
Final Answer
2 arrows

"""

#==================TC & SC==================

"""
Time Complexity:
---------------
Sorting the intervals: O(n log n)
Traversing the intervals: O(n)

Total:
O(n log n)

TC = O(n log n)
→ Due to sorting the balloons by their ending coordinate.

Space Complexity:
----------------
Only a few variables are used.

O(1) auxiliary space

SC = O(1)
→ Only constant extra variables are used (arrows and current_end).
"""
                