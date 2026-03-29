"""

LC: 1372. Longest ZigZag Path in a Binary Tree

Medium

Topics
Dynamic Programming
Tree
Depth-First Search
Binary Tree
Biweekly Contest 21

Hint
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 

Example 1:


Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:


Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
270,090/403.6K
Acceptance Rate
66.9%

Hint 1
Create this function maxZigZag(node, direction) maximum zigzag given a node and direction (right or left).

"""

from typing import Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
class Solution:
    def longestZigZag(self,root:Optional[TreeNode]) -> int:
        self.max_len=0
        def dfs(node,direction,length):
            if not node:
                return
            self.max_len=max(self.max_len,length)
            if direction == "left":
                dfs(node.right,"right",length+1)
                dfs(node.left,"left",1)
            else:
                dfs(node.left,"left",length+1)
                dfs(node.right,"right",1)
        dfs(root.left,"left",1)
        dfs(root.right,"right",1)
        return self.max_len

root1=TreeNode(1)
root1.left=None
root1.right=TreeNode(1)
root1.right.left=TreeNode(1)
root1.right.right=TreeNode(1)
root1.right.right.left=TreeNode(1)
root1.right.right.right=TreeNode(1)
root1.right.right.left.right=TreeNode(1)
root1.right.right.left.right.right=TreeNode(1)

root2=TreeNode(1)
root2.right=TreeNode(1)
root2.left=TreeNode(1)
root2.left.right=TreeNode(1)
root2.left.right.left=TreeNode(1)
root2.left.right.right=TreeNode(1)
root2.left.right.left.right=TreeNode(1)


sol=Solution()
print(sol.longestZigZag(root1))
print(sol.longestZigZag(root2))