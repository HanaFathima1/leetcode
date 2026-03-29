"""

LC: 700. Search in a Binary Search Tree

Easy

Topics
Tree
Binary Search Tree
Binary Tree
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,291,169/1.6M
Acceptance Rate
82.3%

"""

from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
class Solution:
    def searchBST(self,root:Optional[TreeNode],val:int)->Optional[TreeNode]:
        if not root:
            return None
        elif val==root.val:
            return root
        elif val>root.val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)
        
def build_tree():
    root=TreeNode(4)
    root.left=TreeNode(2)
    root.left.left=TreeNode(1)
    root.left.right=TreeNode(3)
    root.right=TreeNode(7)
    return root

if __name__=="__main__":
    root=build_tree()
    val=2
    
    sol=Solution()
    result=sol.searchBST(root,val)
    
    if result:
        print("Node found:",result.val)
    else:
        print("Node not found")
        
    