"""

LC: 103. Binary Tree Zigzag Level Order Traversal

Medium

Topics
Tree
Breadth-First Search
Binary Tree

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,836,889/2.9M
Acceptance Rate
64.0%

"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root:Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        left_to_right = True
        while queue:
            levels = len(queue) 
            level_nodes = [] 
            for _ in range(levels):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level_nodes.reverse()
            result.append(level_nodes)
            left_to_right = not left_to_right
        return result
 
root =  TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20) 
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.zigzagLevelOrder(root))

"""
Dry Run

Consider the tree:

        1
      /   \
     2     3
    / \   / \
   4   5 6   7
Initial State
Queue = [1]
left_to_right = True
result = []
Level 0

Process node 1

level_nodes = [1]
Queue = [2, 3]

Direction is Left → Right

result = [[1]]

Flip direction

left_to_right = False
Level 1

Queue:

[2, 3]

Process nodes

level_nodes = [2, 3]
Queue = [4, 5, 6, 7]

Since direction is Right → Left

level_nodes.reverse()

[3, 2]
result =

[
 [1],
 [3,2]
]

Flip direction

left_to_right = True
Level 2

Queue

[4,5,6,7]

Process nodes

level_nodes = [4,5,6,7]

No reverse.

result =

[
 [1],
 [3,2],
 [4,5,6,7]
]

Finished.

Time Complexity
Time: O(n)
Each node is visited exactly once.
Reversing each level takes O(level_size), and across all levels this sums to O(n).
Space: O(n)
Queue stores at most one level of the tree.
Result stores all n node values.

"""
        