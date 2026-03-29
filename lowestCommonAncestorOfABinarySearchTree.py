"""

LC: 235. Lowest Common Ancestor of a Binary Search Tree

Medium

Topics
Tree
Depth-First Search
Binary Search Tree
Binary Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,126,266/3.1M
Acceptance Rate
69.7%

"""

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
class Solution:
    def lowestCommonAncestor(self,root:'TreeNode',p:'TreeNode',q:'TreeNode')->'TreeNode':
        cur=root
        while cur:
            if p.val<cur.val and q.val<cur.val:
                cur=cur.left
            elif p.val>cur.val and q.val>cur.val:
                cur=cur.right
            else:
                return cur

root1=TreeNode(6)
root1.left=TreeNode(2)
root1.left.left=TreeNode(0)
root1.left.right=TreeNode(4)
root1.left.right.left=TreeNode(3)
root1.left.right.right=TreeNode(5)
root1.right=TreeNode(8)
root1.right.right=TreeNode(9)
root1.right.left=TreeNode(7)

# p and q MUST be TreeNode references
p = root1.left            # node with value 2
q = root1.left.right      # node with value 4

sol=Solution()
print(sol.lowestCommonAncestor(root1,p,q).val)