"""

LC:19. Remove Nth Node From End of List

Medium

Topics
Linked List
Two Pointers

Hint
Given the head of a linked list, remove the nth node from the end 
of the list and return its head.

 
Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?

Hint 1
Maintain two pointers and update one with a delay of n steps.

"""

from typing import Optional
class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head:Optional[ListNode], n:int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
    
def create_from_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
        
def print_linked_list(head):
    if not head:
        return None
    while head:
        print(head.data, end=" -> " if head.next else "\n")
        head = head.next

head = create_from_list([1,2,3,4,5])
n=2

print("Original list: ")
print_linked_list(head)

sol = Solution()
new_head = sol.removeNthFromEnd(head, n)
print("After removing",n,"th node from end: ")  
print_linked_list(new_head)      
    
    
    
"""--------------notes---------------

memory trick: FAST → creates gap, SLOW → finds node to delete

Create dummy (for safe deletion).
Move fast n+1 steps (make a gap).
Slide slow & fast until fast reaches end.
Delete the next node of slow.
Return updated head.

----------------------------

🌟 Core Idea of the Two-Pointer Method (LeetCode 19)
👉 Move the fast pointer ahead by n steps to create a fixed gap.
👉 Then move both slow and fast together.
👉 When fast reaches the end, slow will be exactly one node before the node you must delete.

That’s it.
This is the only idea that drives the whole solution.

"""