"""

LC: 1721. Swapping Nodes in a Linked List

Medium

Topics
Linked List
Two Pointers

Hint
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100

Seen this question in a real interview before?
1/5
Yes
No
Accepted
414,743/604.1K
Acceptance Rate
68.7%

Hint 1
We can traverse the linked list and store the elements in an array.
Hint 2
Upon conversion to an array, we can swap the required elements by indexing the array.
Hint 3
We can rebuild the linked list using the order of the elements in the array.

"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

class Solution:
    def swapNodes(self, head:Optional[ListNode], k:int) -> Optional[ListNode]:
        fast = head
        for _ in range(k-1):
            fast = fast.next 
        first_k_node = fast
        
        slow = head 
        while fast.next:
            slow = slow.next 
            fast = fast.next
        second_k_node = slow
        
        first_k_node.val, second_k_node.val = second_k_node.val, first_k_node.val
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
    values = [1,2,3,4,5]
    k = 2
    head = build_linked_list(values)   
    sol = Solution()
    head = sol.swapNodes(head, k)
    print_linked_list(head)
    