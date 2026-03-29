"""

LC: 1351. Count Negative Numbers in a Sorted Matrix
Easy

Topics:
Array
Binary Search
Matrix
Weekly Contest 176

Hint
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 

Follow up: Could you find an O(n + m) solution?
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
506,540/651.5K
Acceptance Rate
77.8%

Hint 1
Use binary search for optimization or simply brute force.

"""

class Solution:
    def countNegatives(self, grid:list[list[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    count+=1
        return count
sol = Solution()
print(sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(sol.countNegatives([[3,2],[1,0]]))
                