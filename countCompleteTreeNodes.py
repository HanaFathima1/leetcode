"""

LC: 222. Count Complete Tree Nodes

Easy

Topics
Binary Search
Bit Manipulation
Tree
Binary Tree

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,212,209/1.7M
Acceptance Rate
73.0%

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Value stored in the node
        self.val = val

        # Pointer to left child
        self.left = left

        # Pointer to right child
        self.right = right


class Solution:

    # Function to calculate the height by continuously moving LEFT.
    # Height here means the number of nodes in the leftmost path.
    def leftHeight(self, node):
        height = 0

        # Keep moving towards the left child
        while node:
            height += 1          # Count current node
            node = node.left     # Move left

        return height


    # Function to calculate the height by continuously moving RIGHT.
    # Height here means the number of nodes in the rightmost path.
    def rightHeight(self, node):
        height = 0

        # Keep moving towards the right child
        while node:
            height += 1          # Count current node
            node = node.right    # Move right

        return height


    def countNodes(self, root: Optional[TreeNode]) -> int:

        # Base Case:
        # If the tree is empty, there are no nodes.
        if not root:
            return 0

        # Find the leftmost height.
        lh = self.leftHeight(root)

        # Find the rightmost height.
        rh = self.rightHeight(root)

        # If both heights are equal,
        # the tree is a PERFECT binary tree.
        if lh == rh:

            # Number of nodes in a perfect binary tree:
            # 2^height - 1
            #
            # (1 << lh) means 2^lh
            #
            # Example:
            # lh = 3
            #
            # 1 << 3
            # = 0001 << 3
            # = 1000 (binary)
            # = 8
            #
            # Nodes = 8 - 1 = 7

            return (1 << lh) - 1

        # Otherwise,
        # recursively count nodes in left subtree
        # and right subtree.
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# -------------------------------
# Driver Code (For VS Code)
# -------------------------------

'''
Construct the following complete binary tree

          1
        /   \
       2     3
      / \   /
     4   5 6

Answer = 6
'''

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)

sol = Solution()

print("Total Nodes =", sol.countNodes(root))

"""
Dry Run
Tree
          1
        /   \
       2     3
      / \   /
     4   5 6
First Function Call
countNodes(1)

Calculate left height.

1
|
2
|
4

Height = 3

Calculate right height.

1
 \
  3

Height = 2

lh = 3
rh = 2

Not equal.

So return

1
+
countNodes(2)
+
countNodes(3)
Left Subtree
      2
     / \
    4   5

Calculate left height.

2
|
4

Height = 2

Calculate right height.

2
 \
  5

Height = 2

Both heights are equal.

Perfect tree.

Nodes

2² - 1

=4-1

=3

Return 3

Right Subtree
    3
   /
  6

Left height

3
|
6

Height = 2

Right height

3

Height = 1

Not equal.

Return

1
+
countNodes(6)
+
countNodes(None)
Node 6
6

Left Height = 1

Right Height = 1

Perfect tree.

Return

2¹-1

=1
None

Return

0

So node 3 returns

1+1+0

=2

Finally

countNodes(1)

=1+3+2

=6

Output

Total Nodes = 6
Why does leftHeight == rightHeight mean the tree is perfect?

In a complete binary tree:

Every level except the last is completely filled.
The last level is filled from left to right.

If:

Left Height == Right Height

then the leftmost and rightmost paths reach the same depth.

This means every level, including the last, is completely filled, so the tree is a perfect binary tree.

For a perfect binary tree of height h, the number of nodes is:

2^h - 1

Instead of recursively counting all nodes, we calculate the answer directly.

Why (1 << lh) - 1?

<< is the left shift operator.

1 << n

means move the binary digit 1 to the left by n positions.

Example:

1 << 0 = 1 = 2⁰

1 << 1 = 2 = 2¹

1 << 2 = 4 = 2²

1 << 3 = 8 = 2³

1 << 4 = 16 = 2⁴

So,

(1 << lh)

is exactly the same as

2^lh

Therefore,

(1 << lh) - 1

computes:

2^height - 1

which is the formula for the number of nodes in a perfect binary tree.

Time Complexity

Let n be the number of nodes.

Calculating the left height takes O(log n).
Calculating the right height takes O(log n).
The recursive calls occur for at most O(log n) levels because the tree is complete.

Overall Time Complexity:

O((log n)²)
Space Complexity

The extra space comes only from the recursive call stack.

Maximum recursion depth = height of the tree = O(log n).

Overall Space Complexity:

O(log n)
"""
