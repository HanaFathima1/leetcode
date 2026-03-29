"""

LC: 118. Pascal's Triangle

Easy

Topics
Array
Dynamic Programming

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,346,693/3M
Acceptance Rate
78.0%

"""

class Solution:
    def generate(self, numRows:int):
        triangle = []
        for i in range(numRows):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle
sol = Solution()
print(sol.generate(numRows=5))
print(sol.generate(numRows=1))