"""

LC: 149. Max Points on a Line

Hard

Topics
Array
Hash Table
Math
Geometry

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
535,525/1.7M
Acceptance Rate
30.9%

"""

class Solution:
    def maxPoints(self, points:list[list[int]]) -> int:
        n=len(points)
        if n<=2:
            return n
        answer=2
        for i in range(n):
            for j in range(i+1,n):
                count=2
                x1,y1=points[i]
                x2,y2=points[j]
                for k in range(n):
                    if k==i or k==j:
                        continue
                    x3,y3=points[k]
                    if (x2-x1)*(y3-y1)==(y2-y1)*(x3-x1):
                        count+=1
                answer=max(answer,count)
        return answer
sol=Solution()
print(sol.maxPoints(points = [[1,1],[2,2],[3,3]]))
print(sol.maxPoints(points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))

#Explanation
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        # Number of points
        n = len(points)

        # If there are 2 or fewer points,
        # all of them lie on the same line.
        if n <= 2:
            return n

        # At least 2 points can always form a line.
        answer = 2

        # Choose the first point of the line.
        for i in range(n):

            # Choose the second point of the line.
            # Together, points i and j define a unique line.
            for j in range(i + 1, n):

                # The line currently contains
                # points i and j.
                count = 2

                # Coordinates of first point.
                x1, y1 = points[i]

                # Coordinates of second point.
                x2, y2 = points[j]

                # Check every other point.
                for k in range(n):

                    # Skip the two points that
                    # already define the line.
                    if k == i or k == j:
                        continue

                    # Coordinates of third point.
                    x3, y3 = points[k]

                    # Check if points (x1,y1),
                    # (x2,y2), and (x3,y3)
                    # are on the same line.
                    #
                    # Instead of comparing slopes:
                    # (y2-y1)/(x2-x1) == (y3-y1)/(x3-x1)
                    #
                    # we use cross multiplication
                    # to avoid division and floating
                    # point precision issues.
                    if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
                        count += 1

                # Update the maximum number of
                # points found on any line so far.
                answer = max(answer, count)

        # Return the maximum number of
        # collinear points.
        return answer


#-====================or===============================

from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):

        # If there are at most 2 points,
        # answer is simply the number of points.
        if len(points) <= 2:
            return len(points)

        answer = 1

        # Pick every point as an anchor point.
        for i in range(len(points)):

            # Stores:
            # slope -> number of points with that slope
            slopes = defaultdict(int)

            x1, y1 = points[i]

            # Compare anchor point with remaining points.
            for j in range(i + 1, len(points)):

                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                # Reduce slope using gcd.
                g = gcd(dx, dy)

                dx //= g
                dy //= g

                # Count this slope.
                slopes[(dy, dx)] += 1

            # Largest number of points having same slope.
            current_max = max(slopes.values(), default=0)

            # Add anchor point itself.
            answer = max(answer, current_max + 1)

        return answer
    
    
#=================DRY RUN=====================
"""
Dry Run
Input
points = [[1,1],[2,2],[3,3],[4,5]]
Initialization
n = 4
answer = 2
Iteration 1
i = 0 → Point (1,1)
j = 1 → Point (2,2)

Current line:

(1,1) ---- (2,2)
count = 2
| k | Point | Check                   | Result  | Count |
| - | ----- | ----------------------- | ------- | ----- |
| 0 | (1,1) | Skip                    | -       | 2     |
| 1 | (2,2) | Skip                    | -       | 2     |
| 2 | (3,3) | (2-1)(3-1) = (2-1)(3-1) | 2 = 2 ✓ | 3     |
| 3 | (4,5) | (2-1)(5-1) = (2-1)(4-1) | 4 ≠ 3 ✗ | 3     |

After loop:

answer = max(2,3)
        = 3
j = 2 → Point (3,3)

Current line:

(1,1) ---- (3,3)
count = 2
k	Point	Result
1	(2,2)	On line ✓
3	(4,5)	Not on line ✗

Final:

count = 3
answer = max(3,3)
       = 3
j = 3 → Point (4,5)

Current line:

(1,1) ---- (4,5)
count = 2
k	Point	Result
1	(2,2)	Not on line ✗
2	(3,3)	Not on line ✗

Final:

count = 2
answer = 3
Iteration 2
i = 1 → Point (2,2)
j = 2 → Point (3,3)

Current line:

(2,2) ---- (3,3)
count = 2
k	Point	Result
0	(1,1)	On line ✓
3	(4,5)	Not on line ✗

Final:

count = 3
answer = 3
j = 3 → Point (4,5)

Current line:

(2,2) ---- (4,5)
count = 2
k	Point	Result
0	(1,1)	Not on line ✗
2	(3,3)	Not on line ✗

Final:

count = 2
answer = 3
Iteration 3
i = 2 → Point (3,3)
j = 3 → Point (4,5)

Current line:

(3,3) ---- (4,5)
count = 2
k	Point	Result
0	(1,1)	Not on line ✗
1	(2,2)	Not on line ✗

Final:

count = 2
answer = 3
Final Answer
return answer
3

The points on the same line are:

(1,1), (2,2), (3,3)
Complexity Analysis
Outer Loop
for i in range(n)

Runs:

n

times.

Middle Loop
for j in range(i+1, n)

Runs approximately:

n

times for each i.

So far:

O(n²)
Inner Loop
for k in range(n)

Runs:

n

times for every (i,j) pair.

Therefore:

O(n²) × O(n)
=
O(n³)
Time Complexity
O(n³)

For n = 300:

300 × 300 × 300
=
27,000,000

operations in the worst case.

Space Complexity

Only a few variables are used:

answer
count
x1,y1
x2,y2
x3,y3

No extra arrays, hash maps, or recursion.

Space Complexity
O(1)

| Complexity | Value     |
| ---------- | --------- |
| Time       | **O(n³)** |
| Space      | **O(1)**  |

"""