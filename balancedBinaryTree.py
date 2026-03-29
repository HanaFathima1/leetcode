"""

LC: 110. Balanced Binary Tree

Easy

Topics
Tree
Depth-First Search
Binary Tree

Given a binary tree, determine if it is height-balanced.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,206,968/3.9M
Acceptance Rate
56.7%

"""

from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # This helper function returns:
        # - the height of the subtree if it is balanced
        # - -1 if the subtree is NOT balanced
        def height(node):

            # Base case:
            # An empty tree has height 0 and is balanced
            if not node:
                return 0

            # Recursively find the height of the left subtree
            left = height(node.left)

            # If left subtree is unbalanced, propagate -1 upward
            if left == -1:
                return -1

            # Recursively find the height of the right subtree
            right = height(node.right)

            # If right subtree is unbalanced, propagate -1 upward
            if right == -1:
                return -1

            # Check balance condition at the current node
            # If height difference is more than 1, tree is unbalanced
            if abs(left - right) > 1:
                return -1

            # If balanced, return the height of the subtree
            # Height = 1 (current node) + max(left height, right height)
            return 1 + max(left, right)

        # If height(root) returns -1, tree is unbalanced
        # Otherwise, tree is balanced
        return height(root) != -1

root1=TreeNode(3)
root1.left=TreeNode(9)
root1.right=TreeNode(20)
root1.right.left=TreeNode(15)
root1.right.right=TreeNode(7)

root2=TreeNode(1)
root2.right=TreeNode(2)
root2.left=TreeNode(2)
root2.left.left=TreeNode(3)
root2.left.right=TreeNode(3)
root2.left.left.left=TreeNode(4)
root2.left.left.right=TreeNode(4)

root3=TreeNode()
root3.left=None
root3.right=None

sol = Solution()
print(sol.isBalanced(root1))
print(sol.isBalanced(root2))
print(sol.isBalanced(root3))
