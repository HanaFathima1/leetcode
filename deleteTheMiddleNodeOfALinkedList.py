"""

LC: 2095. Delete the Middle Node of a Linked List

Medium

Topics
Linked List
Two Pointers
Weekly Contest 270

Hint
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
 

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
847,266/1.4M
Acceptance Rate
59.5%

Hint 1
If a point with a speed s moves n units in a given time, a point with speed 2 * s will move 2 * n units at the same time. Can you use this to find the middle node of a linked list?
Hint 2
If you are given the middle node, the node before it, and the node after it, how can you modify the linked list?

"""
from typing import Optional,List

class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def build_ll(self,values:List[int]):
        if not values:
            self.head=None
            return
        self.head=ListNode(values[0])
        current=self.head
        for val in values[1:]:
            current.next=ListNode(val)
            current=current.next
    
    def print_ll(self):
        current=self.head
        while current:
            print(current.val,end="->")
            current=current.next
        print("None")        
            
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        prev=None
        slow=head
        fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head

ll1=LinkedList()
ll1.build_ll([1, 3, 4, 7, 1, 2, 6])
ll1.head=ll1.deleteMiddle(ll1.head)
ll1.print_ll()

ll2=LinkedList()
ll2.build_ll([1, 2, 3, 4])
ll2.head=ll2.deleteMiddle(ll2.head)
ll2.print_ll()

ll3=LinkedList()
ll3.build_ll([2, 1])
ll3.head=ll3.deleteMiddle(ll3.head)
ll3.print_ll()