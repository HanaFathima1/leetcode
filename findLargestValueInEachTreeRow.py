"""

LC: 515. Find Largest Value in Each Tree Row

Solved

Medium

Topics
Tree
Depth-First Search
Breadth-First Search
Binary Tree


Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
506,469/764.2K
Acceptance Rate
66.3%

"""

from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque([root])
        level=0
        result=[]
        while q:
            max_val=float('-inf')
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                max_val=max(max_val,node.val)
            result.append(max_val)
        return result

root=TreeNode(1)
root.left=TreeNode(3)
root.left.left=TreeNode(5)
root.left.right=TreeNode(3)
root.right=TreeNode(2)
root.right.right=TreeNode(9)

sol=Solution()
print(sol.largestValues(root))
