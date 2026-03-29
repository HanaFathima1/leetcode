"""

LC:83. Remove Duplicates from Sorted List

Easy

Topics
Linked List

Given the head of a sorted linked list, delete all duplicates such 
that each element appears only once. Return the linked list sorted 
as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,029,718/3.7M
Acceptance Rate
55.2%

"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head:Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print("->".join(result))
    
if __name__ == "__main__":
    values = [1,1,2,3,3]
    head = build_linked_list(values)

    sol = Solution()
    updated_head = sol.deleteDuplicates(head)
    print_linked_list(updated_head)
    
    
    