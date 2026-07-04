"""
102.BINARY TREE LEVEL ORDER TRAVERSAL

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        
class Solution:
    def levelOrder(self, root:Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result=[]
        
        while queue:
            level_size=len(queue)
            level_nodes=[]
            for _ in range(level_size):
                node=queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            result.append(level_nodes)
                    
        return result
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.levelOrder(root))


"""
DRY RUN


Tree Used
        3
       / \
      9   20
         /  \
        15   7
Initial State
Queue = [3]

Result = []
Iteration 1 (Level 0)
Queue before processing
[3]
Calculate level size
level_size = len(queue)
           = 1

This means only one node belongs to this level.

level_nodes = []
Process node 3
node = queue.popleft()

Queue becomes

[]

Add value

level_nodes = [3]

Add left child

queue.append(9)

Queue

[9]

Add right child

queue.append(20)

Queue

[9, 20]

Level finished.

Append it.

result = [[3]]

Current state

Queue

[9,20]
Iteration 2 (Level 1)

Queue

[9,20]

Calculate

level_size = 2

Meaning

This level has exactly 2 nodes.
level_nodes = []
Process node 9

Remove

Queue

[20]

Add value

level_nodes

[9]

Node 9 has no children.

Queue remains

[20]
Process node 20

Remove

Queue

[]

Add value

level_nodes

[9,20]

Left child

15

Queue

[15]

Right child

7

Queue

[15,7]

Level completed.

Append

result

[
 [3],
 [9,20]
]

Current queue

[15,7]
Iteration 3 (Level 2)

Queue

[15,7]
level_size = 2
level_nodes = []
Process 15

Remove

Queue

[7]

Add value

level_nodes

[15]

No children.

Process 7

Remove

Queue

[]

Add value

level_nodes

[15,7]

No children.

Append level

result

[
 [3],
 [9,20],
 [15,7]
]

Queue becomes empty.

The loop stops.

Return

[
 [3],
 [9,20],
 [15,7]
]
Dry Run Table
| Iteration | Queue Before | level_size | Nodes Processed | Queue After | Result              |
| --------- | ------------ | ---------- | --------------- | ----------- | ------------------- |
| Start     | [3]          | -          | -               | [3]         | []                  |
| 1         | [3]          | 1          | 3               | [9,20]      | [[3]]               |
| 2         | [9,20]       | 2          | 9,20            | [15,7]      | [[3],[9,20]]        |
| 3         | [15,7]       | 2          | 15,7            | []          | [[3],[9,20],[15,7]] |



Time Complexity
Time: O(n) — each node is enqueued and dequeued exactly once.
Space: O(n) — in the worst case, the queue may contain all nodes of the widest level of the tree.
"""