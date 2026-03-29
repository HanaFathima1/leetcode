"""

LC: 1572. Matrix Diagonal Sum

Easy

Topics
Array
Matrix

Hint
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and
all the elements on the secondary diagonal that are not part of the 
primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
457,529/545.9K
Acceptance Rate
83.8%

Hint 1
There will be overlap of elements in the primary and secondary diagonals if and only if the length of the matrix is odd, which is at the center.

"""

class Solution:
    def diagonalSum(self, mat:list[list[int]]) -> int:
        total = 0
        n = len(mat)
        for i in range(n):
            total+=mat[i][i]
            if i != n-1-i:
                total+=mat[i][n-1-i]
        return total
sol = Solution()
print(sol.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))
print(sol.diagonalSum([[5]]))


# attempt:
    
#     class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         # primary_sum=0
#         # secondary_sum=0
#         total=0
#         n=len(mat)
#         for i in range(n):
#             # primary_sum+=mat[i][i]
#             total+=mat[i][i]
#             # i+=1
#         for i in range(n):
#             # secondary_sum+=mat[i][n-i-1]
#             if i!=n-1-i:
#                 total+=mat[i][n-i-1]
#             # i+=1
#         # total=primary_sum+secondary_sum
#         return total


 