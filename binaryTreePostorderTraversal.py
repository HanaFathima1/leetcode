"""

LC: 145. Binary Tree Postorder Traversal

Solved

Easy

Topics
Stack
Tree
Depth-First Search
Binary Tree

Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,836,287/2.4M
Acceptance Rate
77.2%

"""

from typing import Optional,List

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def postorderTraversal(self,root:Optional[TreeNode])->List[int]:
        res=[]
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                res.append(node.val)
        postorder(root)
        return res
    
root1=TreeNode(1)
root1.left=None
root1.right=None

root2=TreeNode(1)
root2.left=TreeNode(2)
root2.left.left=TreeNode(4)
root2.left.right=TreeNode(5)
root2.left.right.left=TreeNode(6)
root2.left.right.right=TreeNode(7)
root2.right=TreeNode(3)
root2.right.right=TreeNode(8)
root2.right.right.left=TreeNode(9)

sol = Solution()
print(sol.postorderTraversal(root1))
print(sol.postorderTraversal(root2))