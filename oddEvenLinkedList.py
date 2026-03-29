"""

LC: 328. Odd Even Linked List

Medium

Topics
Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,380,453/2.2M
Acceptance Rate
62.2%

"""

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def build_ll(values):
    if not values:
        return None
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
    
class Solution:
    def oddEvenList(self,head):
        odd=head
        even=head.next
        even_head=even
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=even_head
        return head

if __name__=="__main__":
    nums1=[1,2,3,4,5]
    head1=build_ll(nums1)
    print_ll(head1)
    sol=Solution()
    new_head1=sol.oddEvenList(head1)
    print("\nAfter Odd-Even rearragement:")
    print_ll(new_head1)
    
    nums2=[2,1,3,5,6,4,7]
    head2=build_ll(nums2)
    print_ll(head2)
    sol=Solution()
    new_head2=sol.oddEvenList(head2)
    print("\nAfter Odd-Even rearragement:")
    print_ll(new_head2)
    