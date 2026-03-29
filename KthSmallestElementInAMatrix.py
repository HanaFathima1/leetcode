"""

LC: 378. Kth Smallest Element in a Sorted Matrix

Medium

Topics:
Array
Binary Search
Sorting
Heap (Priority Queue)
Matrix

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.

"""
import heapq
class Solution:
    def kthSmallest(self, matrix:list[list[int]], k:int) -> int:
        n = len(matrix)
        heap = [(matrix[0][0],0,0)]
        visited = {(0,0)}
        while k:
            val,r,c = heapq.heappop(heap)
            k-=1
            if k==0:
                return val
            if r+1<n and (r+1,c) not in visited:
                heapq.heappush(heap, (matrix[r+1][c],r+1,c))
                visited.add((r+1,c))
            if c+1<n and (r,c+1) not in visited:
                heapq.heappush(heap, (matrix[r][c+1],r,c+1))
                visited.add((r,c+1))
sol = Solution()
print(sol.kthSmallest( matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))
print(sol.kthSmallest( matrix = [[-5]], k = 1))
             
    