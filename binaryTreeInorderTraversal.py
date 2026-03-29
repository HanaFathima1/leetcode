"""
94.BINARY TREE INORDER TRAVERSAL

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root:Optional[TreeNode]) -> list[int]:
        res=[]
        
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
        
        inorder(root)
        return res
    
root = TreeNode(1)
root.left = None
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
print(sol.inorderTraversal(root))



#-------------------or--------------------
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return (
            self.inorderTraversal(root.left) +
            [root.val] +
            self.inorderTraversal(root.right)
        )


    
    
    