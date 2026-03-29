"""

LC: 450. Delete Node in a BST

Medium

Topics
Tree
Binary Search Tree
Binary Tree

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 

Follow up: Could you solve it with time complexity O(height of tree)?

 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
798,001/1.5M
Acceptance Rate
53.9%

"""

from typing import Optional

# ---------------------------
# Binary Tree Node
# ---------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ---------------------------
# Solution Class
# ---------------------------
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # CASE 1 & 2: node has 0 or 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # CASE 3: node has 2 children
            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

# ---------------------------
# Helper Functions
# ---------------------------
def build_tree():
    """
        Build this BST:
        
                5
               / \
              3   6
             / \   \
            2   4   7
    """
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    return root

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

# ---------------------------
# MAIN EXECUTION
# ---------------------------
if __name__ == "__main__":
    root = build_tree()

    print("Inorder BEFORE deletion:")
    inorder(root)

    sol = Solution()
    root = sol.deleteNode(root, 3)   # delete node with value 3

    print("\nInorder AFTER deletion:")
    inorder(root)
