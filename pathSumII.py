"""

LC: 113. Path Sum II

Medium

Topics
Backtracking
Tree
Depth-First Search
Binary Tree

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,113,072/1.8M
Acceptance Rate
61.5%

"""

from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self,root:Optional[TreeNode],targetSum:int)->List[List[int]]:
        res=[]
        def dfs(node,remaining,path):
            if not node:
                return 
            path.append(node.val)
            if not node.left and not node.right and remaining==node.val:
                res.append(path.copy())
            dfs(node.left,remaining-node.val,path)
            dfs(node.right,remaining-node.val,path)
            path.pop()
        dfs(root,targetSum,[])
        return res
        
root1=TreeNode(5)
root1.left=TreeNode(4)
root1.left.left=TreeNode(11)
root1.left.left.left=TreeNode(7)
root1.left.left.right=TreeNode(2)
root1.right=TreeNode(8)
root1.right.left=TreeNode(13)
root1.right.right=TreeNode(4)
root1.right.right.right=TreeNode(1)
root1.right.right.left=TreeNode(5)

sol=Solution()
print(sol.pathSum(root1,22))