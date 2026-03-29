"""

LC: 98. Validate Binary Search Tree

Medium

Topics
Tree
Depth-First Search
Binary Search Tree
Binary Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
3,148,437/9M
Acceptance Rate
35.1%

"""

from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def isValidBST(self,root:Optional[TreeNode])->bool:
        def dfs(node,low,high):
            if not node:
                return True
            if not low<node.val<high:
                return False
            return (
                dfs(node.left,low,node.val)
                and
                dfs(node.right,node.val,high)
            )
        return dfs(root,float('-inf'),float('inf'))
    
root1=TreeNode(2)
root1.left=TreeNode(1)
root1.right=TreeNode(3)

root2=TreeNode(5)
root2.left=TreeNode(1)
root2.right=TreeNode(4)
root2.right.left=TreeNode(3)
root2.right.right=TreeNode(6)

sol=Solution()
print(sol.isValidBST(root1))
print(sol.isValidBST(root2))