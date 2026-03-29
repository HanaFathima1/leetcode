"""

LC: 543. Diameter of Binary Tree

Easy

Topics
Tree
Depth-First Search
Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,322,503/3.6M
Acceptance Rate
64.7%

"""

from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def diameterOfBinaryTree(self,root:Optional[TreeNode]) -> int:
        diameter=0
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            diameter=max(diameter,left+right)
            return 1+max(left,right)
        dfs(root)
        return diameter

root1=TreeNode(1)
root1.left=TreeNode(2)
root1.left.left=TreeNode(4)
root1.left.right=TreeNode(5)
root1.right=TreeNode(3)

root2=TreeNode(1)
root2.left=TreeNode(2)

sol=Solution()
print(sol.diameterOfBinaryTree(root1))
print(sol.diameterOfBinaryTree(root2))