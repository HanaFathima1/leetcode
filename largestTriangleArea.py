"""

LC: 812. Largest Triangle Area

Easy

Topics
Array
Math
Geometry
Weekly Contest 79

Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:


Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
 

Constraints:

3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
110,732/163.2K
Acceptance Rate
67.9%

"""

class Solution:
    def largestTriangleArea(self, points:list[list[int]]) -> float:
        n = len(points)
        max_area = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
                    max_area = max(max_area, area)
        return max_area
sol = Solution()
print(sol.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))
print(sol.largestTriangleArea([[1,0],[0,0],[0,1]]))       