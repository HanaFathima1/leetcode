"""

LC: 437. Path Sum III

Medium

Topics
Tree
Depth-First Search
Binary Tree

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
756,446/1.6M
Acceptance Rate
46.2%

"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self,root:Optional[TreeNode],targetSum:int)->int:
        def dfs(node,curr_sum):
            if not node:
                return 0
            curr_sum+=node.val
            count=1 if curr_sum==targetSum else 0
            count+=dfs(node.left,curr_sum)
            count+=dfs(node.right,curr_sum)
            return count
        if not root:
            return 0
        return (
            dfs(root,0)+
            self.pathSum(root.left,targetSum)+
            self.pathSum(root.right,targetSum)
        )
        
root1=TreeNode(10)
root1.left=TreeNode(5)
root1.left.left=TreeNode(3)
root1.left.left.left=TreeNode(3)
root1.left.left.right=TreeNode(-2)
root1.left.right=TreeNode(2)
root1.left.right.right=TreeNode(1)
root1.right=TreeNode(-3)
root1.right.right=TreeNode(11)

sol=Solution()
print(sol.pathSum(root1,8))