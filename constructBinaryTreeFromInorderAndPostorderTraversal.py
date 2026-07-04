"""

LC: 106. Construct Binary Tree from Inorder and Postorder Traversal

Medium

Topics
Array
Hash Table
Divide and Conquer
Tree
Binary Tree

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
984,092/1.4M
Acceptance Rate
69.0%

"""


from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:

        # Base case
        if not inorder or not postorder:
            return None

        # The last element in postorder is always the root
        root = TreeNode(postorder[-1])

        # Find the root's position in inorder
        mid = inorder.index(postorder[-1])

        # ---------------- Build Right Subtree ----------------
        # Build the right subtree first because after removing
        # the root from postorder, the next element from the end
        # belongs to the right subtree.
        root.right = self.buildTree(
            inorder[mid + 1:],
            postorder[mid:-1]
        )

        # ---------------- Build Left Subtree -----------------
        root.left = self.buildTree(
            inorder[:mid],
            postorder[:mid]
        )

        return root


# ---------------------------------------------------
# Helper Function: Level Order Traversal
# ---------------------------------------------------
def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# ---------------------------------------------------
# Driver Code
# ---------------------------------------------------
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

solution = Solution()
root = solution.buildTree(inorder, postorder)

print("Level Order Traversal of Constructed Tree:")
print(levelOrder(root))

"""

DRY RUN

Dry Run

Input:

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
First Call
root = TreeNode(postorder[-1])   # 3

Tree:

    3

Find 3 in inorder:

9 |3| 15 20 7

Split:

Left Inorder  = [9]

Right Inorder = [15,20,7]
Build Right
postorder[mid:-1]

mid = 1

postorder[1:-1]

= [15,7,20]

Recursive call:

buildTree([15,20,7], [15,7,20])

Root becomes 20.

Build Left
inorder[:1]

= [9]

postorder[:1]

= [9]

Recursive call:

buildTree([9], [9])

Root becomes 9.

Final tree:

        3
       / \
      9   20
         /  \
        15   7
        
COMPLEXITY

| Operation                    | Complexity  |
| ---------------------------- | ----------- |
| Finding root using `index()` | `O(n)`      |
| List slicing                 | `O(n)`      |
| Recursive calls              | `n` calls   |
| **Total Time Complexity**    | **`O(n²)`** |
| **Total Space Complexity**   | **`O(n²)`** |

"""