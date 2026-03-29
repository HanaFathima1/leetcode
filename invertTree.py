# 226.INVERT BINARY TREE
# EASY

# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)


#build tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

#invert
sol= Solution()
sol.invertTree(root)

#print Inorder
print("Inorder after invert: ")
inorder(root)

#-----------------

class TreeNode:
    def __init__(self,val,left,right):
        self.val=val
        self.left=None
        self.right=None

def invertTree(root):
    if not root:
        return None
    root.left,root.right=root.right,root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

def inorder(node):
    inorder(node.left)
    print(node.val)
    inorder(node.right)

    