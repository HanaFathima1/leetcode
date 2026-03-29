"""

LC: 144. Binary Tree Preorder Traversal

Solved

Easy

Topics
Stack
Tree
Depth-First Search
Binary Tree

Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?

 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,279,571/3.1M
Acceptance Rate
74.7%

"""

from typing import Optional,List

class TreeNode:
    def __init__(self,val=0,left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        
class Solution:
    def preorderTraversal(self,root:Optional[TreeNode]) -> List[int]:
        res=[]
        def preorder(node):
            if node:
                res.append(node.val)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return res
        
root1=TreeNode(1)
root1.left=None
root1.right=TreeNode(2)
root1.right.left=TreeNode(3)

root2=TreeNode(1)
root2.left=TreeNode(2)
root2.left.left=TreeNode(4)
root2.left.right=TreeNode(5)
root2.left.right.left=TreeNode(6)
root2.left.right.right=TreeNode(7)
root2.right=TreeNode(3)
root2.right.right=TreeNode(8)
root2.right.right.left=TreeNode(9)

sol=Solution()
print(sol.preorderTraversal(root1))
print(sol.preorderTraversal(root2))

