"""

111.MINIMUM DEPTH OF BINARY TREE

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def minDepth(self, root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return 1+self.minDepth(root.right)
        if not root.right:
            return 1+self.minDepth(root.left)
        return 1+min(self.minDepth(root.left), self.minDepth(root.right))

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
    
sol = Solution()
print(sol.minDepth(root))


"""
============DRY RUN=============

Your tree is:

              3
            /   \
           9     20
                /  \
               15   7

Expected answer = 2, because the shortest root-to-leaf path is:

3 → 9
1. First understand your code
def minDepth(self, root):
    if not root:
        return 0

    if not root.left:
        return 1 + self.minDepth(root.right)

    if not root.right:
        return 1 + self.minDepth(root.left)

    return 1 + min(
        self.minDepth(root.left),
        self.minDepth(root.right)
    )

There are 3 situations:

Situation 1: No node
if not root:
    return 0
Situation 2: Only right child exists
if not root.left:
    return 1 + self.minDepth(root.right)
Situation 3: Only left child exists
if not root.right:
    return 1 + self.minDepth(root.left)
Situation 4: Both children exist
return 1 + min(
    self.minDepth(root.left),
    self.minDepth(root.right)
)
2. Let's start the recursion

We call:

sol.minDepth(root)

where:

root = 3

So conceptually:

minDepth(3)

Node 3 has:

left  = 9
right = 20

Therefore:

return 1 + min(
    minDepth(9),
    minDepth(20)
)

But we don't immediately know the answers.

The computer has to calculate:

minDepth(9)
minDepth(20)

This is where recursion starts going deeper.

3. First recursive call: minDepth(9)

We have:

    3
   /
  9

At node 9:

root = 9

Check:

if not root:

False.

Then:

if not root.left:

9.left is None.

Therefore this is True.

So Python executes:

return 1 + self.minDepth(root.right)

Since:

9.right = None

we get:

return 1 + minDepth(None)
4. minDepth(None)

Now recursion reaches:

minDepth(None)

First condition:

if not root:
    return 0

is true.

Therefore:

minDepth(None) = 0

Now we go back to the previous call:

minDepth(9)

It was waiting for:

1 + minDepth(None)

We now know:

minDepth(None) = 0

Therefore:

minDepth(9)
= 1 + 0
= 1

So:

minDepth(9) = 1
5. This is the important recursion idea

Think of it like this:

minDepth(3)
     |
     | needs minDepth(9)
     ↓
minDepth(9)
     |
     | needs minDepth(None)
     ↓
minDepth(None)
     |
     ↓
     0

Then the answer travels back upward:

minDepth(None) = 0
        ↑
minDepth(9) = 1
        ↑
minDepth(3) still waiting...

This is how recursion works in almost all these tree problems:

Go down until the base case → return the answer → use that answer while coming back up.

6. Now calculate minDepth(20)

Back at node 3, we still need:

minDepth(20)

Node 20:

       20
      /  \
     15   7

Both children exist.

So:

return 1 + min(
    minDepth(15),
    minDepth(7)
)

Again, we need to calculate both.

7. Calculate minDepth(15)

Node 15:

15

It has no children.

So:

minDepth(15)

eventually becomes:

1 + minDepth(None)

and:

minDepth(None) = 0

Therefore:

minDepth(15) = 1
8. Calculate minDepth(7)

Exactly the same:

minDepth(7) = 1

Now node 20 has the answers:

minDepth(15) = 1
minDepth(7)  = 1

So:

minDepth(20)
= 1 + min(1, 1)
= 2

Therefore:

minDepth(20) = 2
9. Finally return to node 3

Remember, node 3 was waiting for:

1 + min(
    minDepth(9),
    minDepth(20)
)

Now we know:

minDepth(9)  = 1
minDepth(20) = 2

Therefore:

minDepth(3)
= 1 + min(1, 2)
= 1 + 1
= 2

Final answer:

2
10. Complete dry run

You can visualize the whole thing like this:

                    minDepth(3)
                    /         \
                   /           \
            minDepth(9)     minDepth(20)
                /              /       \
               /              /         \
       minDepth(None)   minDepth(15)  minDepth(7)
             |                |            |
             0                1            1
             ↑
             1
                              ↑
                              2
                    ↑
                    2

More simply:

minDepth(9)
    ↓
minDepth(None)
    ↓
    0
    ↑
minDepth(9) = 1


minDepth(20)
    ↓
minDepth(15) = 1
minDepth(7)  = 1
    ↓
minDepth(20) = 1 + min(1,1)
             = 2


minDepth(3)
    ↓
1 + min(1,2)
    ↓
    2
11. Now the BIG question: Why doesn't the Maximum Depth code work?

Your Maximum Depth code was:

def maxDepth(root):
    if not root:
        return 0

    left_depth = 1 + maxDepth(root.left)
    right_depth = 1 + maxDepth(root.right)

    return max(left_depth, right_depth)

It's tempting to write Minimum Depth like this:

def minDepth(root):
    if not root:
        return 0

    left_depth = 1 + minDepth(root.left)
    right_depth = 1 + minDepth(root.right)

    return min(left_depth, right_depth)

This is wrong.

Why?

Because None is being treated as if it were a valid path.

12. Look at this simple tree

Consider:

       3
      /
     9

The minimum depth is obviously:

3 → 9

Therefore answer:

2

Now let's use the "wrong" code:

def minDepth(root):
    if not root:
        return 0

    left_depth = 1 + minDepth(root.left)
    right_depth = 1 + minDepth(root.right)

    return min(left_depth, right_depth)

At node 3:

left = 9
right = None

Calculate:

left_depth
= 1 + minDepth(9)
= 1 + 1
= 2

And:

right_depth
= 1 + minDepth(None)
= 1 + 0
= 1

Then:

return min(2, 1)

gives:

1

But that's WRONG.

There is no path:

3 → None

None is not a leaf!

13. This is why Maximum Depth doesn't have this problem

Suppose:

       3
      /
     9

For Maximum Depth:

left  = 9 → depth 1
right = None → depth 0

We calculate:

1 + max(1, 0)
= 2

Perfect.

Why?

Because Maximum chooses the larger path.

The nonexistent None path gives 0, so it doesn't affect the maximum.

14. But Minimum has the opposite problem

For Minimum:

left  = 9 → 1
right = None → 0

Then:

min(1, 0)

chooses:

0

But 0 represents:

"There is no node."

It does not represent:

"I found a leaf at depth 0."

That's the fundamental difference.

15. That's why your code handles one-child nodes

This part:

if not root.left:
    return 1 + self.minDepth(root.right)

means:

"There is no left subtree, so don't consider it. Follow the right subtree."

And:

if not root.right:
    return 1 + self.minDepth(root.left)

means:

"There is no right subtree, so don't consider it. Follow the left subtree."

Only when both children exist do we do:

min(left, right)
16. The easiest rule to remember
Maximum Depth
                 max
                /   \
               /     \
          valid      None
            1          0

max(1,0) → 1

No problem.

Minimum Depth
                 min
                /   \
               /     \
          valid      None
            1          0

min(1,0) → 0

Problem!

So we have to ignore the missing child.

17. Think about what the question is actually asking
Maximum Depth

How far can I go?

So if one side doesn't exist, that's okay.

take the LONGER path
Minimum Depth

What is the shortest path to a REAL LEAF?

Therefore:

I cannot choose a missing child.

This is the key idea.

Final mental model

For Maximum Depth:

if not root:
    return 0

return 1 + max(
    maxDepth(root.left),
    maxDepth(root.right)
)

For Minimum Depth:

if not root:
    return 0

if not root.left:
    return 1 + minDepth(root.right)

if not root.right:
    return 1 + minDepth(root.left)

return 1 + min(
    minDepth(root.left),
    minDepth(root.right)
)
Remember this one sentence:

Maximum depth can safely use max() because a missing subtree (0) will never win. Minimum depth cannot blindly use min() because a missing subtree (0) would incorrectly win.
"""