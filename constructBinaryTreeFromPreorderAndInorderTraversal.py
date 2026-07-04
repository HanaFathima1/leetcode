"""

LC: 105. Construct Binary Tree from Preorder and Inorder Traversal

Medium

Topics
Array
Hash Table
Divide and Conquer
Tree
Binary Tree

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,924,150/2.8M
Acceptance Rate
69.1%

"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preOrder:list[int], inOrder:list[int]) -> Optional[TreeNode]:
        if not preOrder or not inOrder:
            return None
        root = TreeNode(preOrder[0]) #preorder gives the first element is always the root.
        mid = inOrder.index(preOrder[0]) #This line finds where the root appears in the inorder array.
        root.left = self.buildTree(preOrder[1:mid+1],inOrder[:mid]) #
        root.right = self.buildTree(preOrder[mid+1:], inOrder[mid+1:])
        return root

from typing import Deque
def levelOrder(root):
    if not root:
        return []
    queue = Deque([root])
    result = []
    while queue:
        level_node = []
        for _ in range(len(queue)):
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_node)
    return result

preOrder=[3,9,20,15,7]
inOrder=[9,3,15,20,7]

sol = Solution()
root = sol.buildTree(preOrder, inOrder)

print("Level Order Traversal: ")
print(levelOrder(root))
    
"""
========explanation===========

# Create the root node.
# In preorder traversal, the first element is always the root of the current subtree.
root = TreeNode(preOrder[0])

# Find the position of the root in the inorder traversal.
# In inorder traversal:
#   Left Subtree -> Root -> Right Subtree
# Everything before 'mid' belongs to the left subtree.
# Everything after 'mid' belongs to the right subtree.
mid = inOrder.index(preOrder[0])

# -------------------- Build the Left Subtree --------------------
# inorder[:mid]
#   -> All nodes before the root in inorder.
#
# preOrder[1:mid+1]
#   -> Skip the first element (the root).
#   -> The next 'mid' elements belong to the left subtree because
#      'mid' is the number of nodes in the left subtree.
#
# Recursively construct the left subtree and attach it to root.left.
root.left = self.buildTree(
    preOrder[1:mid + 1],
    inOrder[:mid]
)

# -------------------- Build the Right Subtree --------------------
# inOrder[mid+1:]
#   -> All nodes after the root in inorder.
#
# preOrder[mid+1:]
#   -> After removing the root and the left subtree nodes,
#      the remaining preorder elements belong to the right subtree.
#
# Recursively construct the right subtree and attach it to root.right.
root.right = self.buildTree(
    preOrder[mid + 1:],
    inOrder[mid + 1:]
)

# Return the root of the constructed subtree.
return root

"""
"""
Dry Run

Suppose

preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
Step 1

Root is

3

Find 3 in inorder

9 |3| 15 20 7

Split:

Left inorder  = [9]
Right inorder = [15,20,7]

Now split preorder.

Since the left subtree has 1 node, the next 1 element in preorder belongs to the left subtree.

Left preorder  = [9]
Right preorder = [20,15,7]

Now the tree is

        3
       / \
      ?   ?
Step 2 (Left)
preorder = [9]
inorder  = [9]

Root is 9.

No left or right elements remain.

      9
Step 3 (Right)
preorder = [20,15,7]
inorder  = [15,20,7]

Root is 20.

Find it.

15 |20| 7

Split

Left inorder  = [15]
Right inorder = [7]

Left subtree has 1 node, so

Left preorder = [15]
Right preorder = [7]

Tree becomes

        20
       /  \
      15   7

Finally,

        3
       / \
      9   20
         /  \
        15   7
Why does preorder[1:mid+1] work?

Suppose

preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]

Root is 3.

The root is at index 1 in inorder.

inorder

9 |3| 15 20 7
  ^
 mid = 1

Everything before mid belongs to the left subtree.

Number of left subtree nodes is

mid = 1

So after removing the root (preorder[0]), the next mid elements belong to the left subtree.

preorder

[3, 9, 20, 15, 7]
 ^
 Root

Remaining

[9,20,15,7]

Take first 1 element

[9]

That's exactly what

preorder[1:mid+1]

does.

The remaining elements automatically belong to the right subtree.

preorder[mid+1:]
Complexity
Time: O(n²) (because inorder.index() takes O(n) each recursive call, and slicing also copies arrays)
Space: O(n²) in the worst case due to slicing and recursion.
"""

#===========Optimal O(n) solution============

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Store the index of each value in inorder for O(1) lookup
        inorder_map = {value: index for index, value in enumerate(inorder)}

        # Index to track the current root in preorder
        self.preIndex = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            # No elements in this subtree
            if left > right:
                return None

            # Root value comes from preorder
            root_val = preorder[self.preIndex]
            self.preIndex += 1

            # Create the root node
            root = TreeNode(root_val)

            # Find root position in inorder
            mid = inorder_map[root_val]

            # Build left subtree
            root.left = build(left, mid - 1)

            # Build right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)