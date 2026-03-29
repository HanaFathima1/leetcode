"""

LC: 109. Convert Sorted List to Binary Search Tree

Medium

Topics
Linked List
Divide and Conquer
Tree
Binary Search Tree
Binary Tree

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
 

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
661,242/1M
Acceptance Rate
65.8%

"""

from typing import Optional,List

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
class TreeNode:
    def __init__(self,val=0,left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
    
class Solution:
    def sortedListToBST(self,head:Optional[ListNode])->Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        prev=None
        slow=fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        root=TreeNode(slow.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(slow.next)
        return root
    
# -------- Helper functions for VS Code testing --------

def build_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next

    return head


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)


# -------- Main (test here) --------

if __name__ == "__main__":
    arr = [-10, -3, 0, 5, 9]
    head = build_linked_list(arr)

    sol = Solution()
    bst_root = sol.sortedListToBST(head)

    print("Inorder traversal of BST:")
    inorder_traversal(bst_root)