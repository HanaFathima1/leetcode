"""

LC: 2130. Maximum Twin Sum of a Linked List

Medium

Topics
Linked List
Two Pointers
Stack
Biweekly Contest 69

Hint
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
467,177/572.6K
Acceptance Rate
81.6%

Hint 1
How can "reversing" a part of the linked list help find the answer?
Hint 2
We know that the nodes of the first half are twins of nodes in the second half, so try dividing the linked list in half and reverse the second half.
Hint 3
How can two pointers be used to find every twin sum optimally?
Hint 4
Use two different pointers pointing to the first nodes of the two halves of the linked list. The second pointer will point to the first node of the reversed half, which is the (n-1-i)th node in the original linked list. By moving both pointers forward at the same time, we find all twin sums.

"""

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    
from typing import Optional

class Solution:
    def pairSum(self,head:Optional[ListNode]) -> int:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        curr=slow
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
            
        ptr1=head
        ptr2=prev
        max_sum=0
        while ptr2:
            twin_sum=ptr1.val+ptr2.val
            max_sum=max(max_sum,twin_sum)
            ptr1=ptr1.next
            ptr2=ptr2.next
        return max_sum
def build_ll(values):
    head=ListNode(values[0])
    current=head
    for val in values[1:]:
        current.next=ListNode(val)
        current=current.next
    return head

def print_ll(head):
    current=head
    while current:
        print(current.val,end="->")
        current=current.next
    print("None")

list1=[5,4,2,1]
head1=build_ll(list1)
print_ll(head1)
sol=Solution()
print(sol.pairSum(head1))

list2=[4,2,2,3]
head2=build_ll(list2)
print_ll(head2)
sol=Solution()
print(sol.pairSum(head2))

list3=[1,100000]
head3=build_ll(list3)
print_ll(head3)
sol=Solution()
print(sol.pairSum(head3))




"""

Idea:

Find middle of the linked list using slow & fast pointers.

Reverse the second half of the list.

Now you have:

First half from head

Second half reversed (from middle to end, reversed)

Walk both halves together, add values, track max sum.

This works because after reversing the second half,
twin nodes become aligned position-wise.

-------------------------------------------------------------------

🧠 Mini Dry Run

Let list = 1 → 2 → 3 → 4

Find middle

slow: 1 → 2 → 3

fast: 1 → 3 → None
→ slow ends at node 3

Reverse second half
Second half: 3 → 4 → None
Reversed: 4 → 3 → None (head = prev)

Pairing

p1 at 1, p2 at 4 → sum = 5

p1 at 2, p2 at 3 → sum = 5
max_sum = 5

Return 5.
"""