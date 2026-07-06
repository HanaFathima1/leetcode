"""

LC: 129. Sum Root to Leaf Numbers

Medium

Topics
Tree
Depth-First Search
Binary Tree

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,305,766/1.9M
Acceptance Rate
70.1%

"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root:Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            path = path*10+node.val
            if not node.left and not node.right:
                return path
            left_sum = dfs(node.left, path)
            right_sum = dfs(node.right, path)
            return left_sum + right_sum
        return dfs(root, 0)
    
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1  
    while queue and i < len(values):
        current = queue.popleft()
        if i<len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i+=1
        if i<len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i+=1
    return root

if __name__ == "__main__":

    # Example 1
    values = [4, 9, 0, 5, 1]

    # Uncomment to test other examples

    # values = [1, 2, 3]
    # Expected Output: 25
    # (12 + 13)

    # values = [1]
    # Expected Output: 1

    root = build_tree(values)

    solution = Solution()
    answer = solution.sumNumbers(root)

    print("Tree (Level Order):", values)
    print("Sum of Root-to-Leaf Numbers:", answer)
    
    

"""
Dry Run
Input
values = [4, 9, 0, 5, 1]

The build_tree() function constructs the following binary tree:

        4
       / \
      9   0
     / \
    5   1

The root-to-leaf paths are:

4 → 9 → 5 → 495
4 → 9 → 1 → 491
4 → 0 → 40

Expected Answer:

495 + 491 + 40 = 1026
Step 1: Call the function
answer = solution.sumNumbers(root)

Inside sumNumbers():

return dfs(root, 0)

So the first recursive call is

dfs(node=4, path=0)
Step 2: Recursive Calls
Call 1
dfs(4, 0)

Current node:

4

Update path

path = 0 × 10 + 4
     = 4

Node 4 is not a leaf.

Call left subtree.

Call 2
dfs(9, 4)

Current node:

9

Update path

path = 4 × 10 + 9
     = 49

Node 9 is not a leaf.

Call left subtree.

Call 3
dfs(5, 49)

Current node:

5

Update path

path = 49 × 10 + 5
     = 495

Node 5 is a leaf.

Return

495

Back to node 9.

Call 4
dfs(1, 49)

Current node:

1

Update path

path = 49 × 10 + 1
     = 491

Node 1 is a leaf.

Return

491

Back to node 9.

Now

left_sum = 495
right_sum = 491

Return

495 + 491 = 986

Back to node 4.

Call 5
dfs(0, 4)

Current node:

0

Update path

path = 4 × 10 + 0
     = 40

Node 0 is a leaf.

Return

40

Back to node 4.

Now

left_sum = 986
right_sum = 40

Return

986 + 40 = 1026

This value is returned by

sumNumbers()
Dry Run Table

| Function Call    | Previous Path | New Path (`path = path × 10 + node.val`) | Leaf Node? |      Returned Value |
| ---------------- | ------------: | ---------------------------------------: | :--------: | ------------------: |
| `dfs(4, 0)`      |             0 |                                        4 |     No     |            Continue |
| `dfs(9, 4)`      |             4 |                                       49 |     No     |            Continue |
| `dfs(5, 49)`     |            49 |                                      495 |     Yes    |             **495** |
| `dfs(1, 49)`     |            49 |                                      491 |     Yes    |             **491** |
| Return to node 9 |             - |                                        - |      -     | **495 + 491 = 986** |
| `dfs(0, 4)`      |             4 |                                       40 |     Yes    |              **40** |
| Return to node 4 |             - |                                        - |      -     | **986 + 40 = 1026** |

Recursion Tree
                     dfs(4,0)
                    path = 4
                  /            \
         dfs(9,4)              dfs(0,4)
         path = 49             path = 40
        /        \                 |
 dfs(5,49)    dfs(1,49)        Leaf → 40
 path=495     path=491
 Leaf→495     Leaf→491

            ↑
     Return 495 + 491 = 986

Final Answer = 986 + 40 = 1026

======================================================================================

| Complexity           | Value                                                                      |
| -------------------- | -------------------------------------------------------------------------- |
| **Time Complexity**  | **O(n)**                                                                   |
| **Space Complexity** | **O(h)** (or **O(log n)** for a balanced tree, **O(n)** in the worst case) |


"""