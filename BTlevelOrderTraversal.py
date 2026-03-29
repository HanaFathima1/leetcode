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