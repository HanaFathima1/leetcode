"""

LC: 236. Lowest Common Ancestor of a Binary Tree

Medium

Topics
Tree
Depth-First Search
Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,426,786/3.6M
Acceptance Rate
68.3%

"""
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
class Solution:
    def lowestCommonAncestor(self,root:'TreeNode',p:'TreeNode',q:'TreeNode')->'TreeNode':
        def dfs(node):
            if not node:
                return None
            if node==p or node==q:
                return node
            left=dfs(node.left)
            right=dfs(node.right)
            if left and right:
                return node
            return left if left else right
        return dfs(root)

root1=TreeNode(3)
root1.left=TreeNode(5)
root1.left.left=TreeNode(6)
root1.left.right=TreeNode(2)
root1.left.right.left=TreeNode(7)
root1.left.right.right=TreeNode(4)
root1.right=TreeNode(1)
root1.right.left=TreeNode(0)
root1.right.right=TreeNode(8)

p = root1.left        # TreeNode with value 5
q = root1.right       # TreeNode with value 1

sol=Solution()
print(sol.lowestCommonAncestor(root1, p, q).val)
