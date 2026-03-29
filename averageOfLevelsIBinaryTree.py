"""

LC: 637. Average of Levels in Binary Tree

Solved

Easy

https://leetcode.com/problems/average-of-levels-in-binary-tree

Topics
Tree
Depth-First Search
Breadth-First Search
Binary Tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
710,439/952.4K
Acceptance Rate
74.6%

"""

from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        q=deque([root])
        result=[]
        avg=0
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
            avg=total/size
            result.append(avg)
        return result

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)

sol=Solution()
print(sol.averageOfLevels(root))
        
        