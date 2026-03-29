"""

LC: 54. Spiral Matrix

Medium

Topics
Array
Matrix
Simulation

Hint
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,056,433/3.8M
Acceptance Rate
54.7%

Hint 1
Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what the problem asks us to do.
Hint 2
We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column, and then we move inwards by 1 and repeat. That's all. That is all the simulation that we need.
Hint 3
Think about when you want to switch the progress on one of the indexes. If you progress on i out of [i, j], you'll shift in the same column. Similarly, by changing values for j, you'd be shifting in the same row. Also, keep track of the end of a boundary so that you can move inwards and then keep repeating. It's always best to simulate edge cases like a single column or a single row to see if anything breaks or not.

"""

class Solution:
    def spiralOrder(self, matrix:list[list[int]]) -> list[int]:
        res = []
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        while top<=bottom and left<=right:
            for j in range(left, right+1):
                res.append(matrix[top][j])
            top+=1
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for j in range(right, left-1, -1):
                    res.append(matrix[bottom][j])
                bottom-=1
            if left<=right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left+=1
        return res
sol = Solution()
print(sol.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(sol.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
            