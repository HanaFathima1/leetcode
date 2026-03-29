"""

LC: 1161. Maximum Level Sum of a Binary Tree

Medium

Topics
Tree
Depth-First Search
Breadth-First Search
Binary Tree
Weekly Contest 150

Hint
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
419,687/622K
Acceptance Rate
67.5%

Hint 1
Calculate the sum for each level then find the level with the maximum sum.
Hint 2
How can you traverse the tree ?
Hint 3
How can you sum up the values for every level ?
Hint 4
Use DFS or BFS to traverse the tree keeping the level of each node, and sum up those values with a map or a frequency array.

"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
class Solution:
    def maxLevelSum(self,root:Optional[TreeNode])->int:
        if not root:
            return 0
        q=deque([root])
        max_sum=float('-inf')
        max_level=1
        level=1
        while q:
            total=0
            size=len(q)
            for i in range(size):
                node=q.popleft()
                total+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if total>max_sum:
                max_sum=total
                max_level=level
            level+=1
        return max_level
        
root1=TreeNode(1)
root1.left=TreeNode(7)
root1.right=TreeNode(0)
root1.left.left=TreeNode(7)
root1.left.right=TreeNode(-8)
        
sol=Solution()
print(sol.maxLevelSum(root1))