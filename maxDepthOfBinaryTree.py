"""
104.MAXIMUM DEPTH OF BINARY TREE
    
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1+max(left_depth, right_depth)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
    
sol = Solution()
print(sol.maxDepth(root))


"""
=============DRY RUN============


Your tree is:

             1
           /   \
          2     3
         / \   / \
        4   5 6   7
                   \
                    8

The longest path is:

1 → 3 → 7 → 8

So the answer is 4.

1. What does this line mean?
left_depth = 1 + maxDepth(root.left)

The 1 represents the current node.

For node 1:

maxDepth(1)

calls:

maxDepth(2)
maxDepth(3)

It keeps going down until it reaches a node with no children.

2. Let's follow the recursion

Start:

maxDepth(1)

Node 1 has two children:

maxDepth(2)       maxDepth(3)

Then node 2:

maxDepth(4)       maxDepth(5)

Node 3:

maxDepth(6)       maxDepth(7)

Node 7:

maxDepth(None)    maxDepth(8)

Node 8:

maxDepth(None)    maxDepth(None)

Now something important happens.

3. Recursion reaches the bottom

For node 8:

if not root:
    return 0

Both children are None.

Therefore:

maxDepth(None) = 0
maxDepth(None) = 0

So for node 8:

left_depth = 1 + 0 = 1
right_depth = 1 + 0 = 1

return max(1, 1)

Therefore:

maxDepth(8) = 1
4. Now recursion goes BACK UP

This is the part that usually makes recursion confusing.

We calculated:

maxDepth(8) = 1

So node 7 can now calculate its depth:

left_depth = 1 + maxDepth(None)
           = 1 + 0
           = 1

right_depth = 1 + maxDepth(8)
            = 1 + 1
            = 2

Therefore:

maxDepth(7) = max(1, 2)
            = 2

So:

       7
        \
         8

depth = 2
5. Node 3

Node 3 has:

       3
      / \
     6   7
          \
           8

We already know:

maxDepth(6) = 1
maxDepth(7) = 2

Therefore:

left_depth = 1 + 1 = 2
right_depth = 1 + 2 = 3

maxDepth(3) = 3

So:

       3
      / \
     6   7
          \
           8

depth = 3
6. Node 2

Node 2:

       2
      / \
     4   5

Both 4 and 5 are leaf nodes:

maxDepth(4) = 1
maxDepth(5) = 1

Therefore:

left_depth = 1 + 1 = 2
right_depth = 1 + 1 = 2

maxDepth(2) = 2
7. Finally node 1

Now we have:

maxDepth(2) = 2
maxDepth(3) = 3

Therefore:

left_depth = 1 + 2 = 3
right_depth = 1 + 3 = 4

return max(3, 4)

So:

maxDepth(1) = 4

And your program prints:

4
The most important idea

Think of the function as answering this question:

"What is the maximum depth starting from this node?"

For every node:

maxDepth(root)

means:

1 + the deeper child

or mathematically:

depth(node) = 1 + max(depth(left), depth(right))

And when there is no node:

depth(None) = 0

So the calculations are:

8 → 1
7 → 1 + max(0, 1) = 2
3 → 1 + max(1, 2) = 3
2 → 1 + max(1, 1) = 2
1 → 1 + max(2, 3) = 4
A very useful way to visualize recursion

The recursion goes DOWN first:

1
 ↓
3
 ↓
7
 ↓
8
 ↓
None

Then it comes BACK UP with answers:

None → 0
  ↑
8 → 1
  ↑
7 → 2
  ↑
3 → 3
  ↑
1 → 4

That's the core of recursion in tree problems:

Go down → reach base case → return → calculate while coming back up.

"""
        