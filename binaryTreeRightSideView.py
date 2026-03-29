"""

LC: 199. Binary Tree Right Side View

Medium

Topics
Tree
Depth-First Search
Breadth-First Search
Binary Tree

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,076,372/3M
Acceptance Rate
68.9%

"""

from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
class Solution:
    def rightSideView(self,root:Optional[TreeNode])->List[int]:
        if not root:
            return []
        q=deque([root])
        view=[]
        while q:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if i==size-1:
                    view.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return view

root1=TreeNode(1)
root1.left=TreeNode(2)
root1.right=TreeNode(3)
root1.left.right=TreeNode(5)
root1.right.right=TreeNode(4)

sol = Solution()
print(sol.rightSideView(root1))