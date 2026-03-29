"""

LC: 872. Leaf-Similar Trees

Easy

Topics
Tree
Depth-First Search
Binary Tree
Weekly Contest 94

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
653,272/931.1K
Acceptance Rate
70.2%

"""

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def leafSimilar(self,root1,root2):
        def leaves(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return leaves(root.left)+leaves(root.right)
        return leaves(root1)==leaves(root2)
# Tree 1
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.right = TreeNode(9)

# Tree 2
root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(2)
root2.right.right = TreeNode(9)

sol = Solution()
print(sol.leafSimilar(root1, root2))