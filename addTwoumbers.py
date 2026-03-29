"""

LC: 2. Add Two Numbers

Medium

Topics:
Linked List
Math
Recursion

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
6,028,900/12.9M
Acceptance Rate
46.6%

"""

from typing import Optional
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total//10
            current.next = ListNode(total%10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
                
def create_linked_list(digits):
    dummy = ListNode(0)
    current = dummy
    for digit in digits:
        current.next = ListNode(digit)
        current = current.next
    return dummy.next

def print_ll(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)
    
if __name__ == "__main__":
    l1 = create_linked_list([2,4,3])
    l2 = create_linked_list([5,6,4])
    
    sol = Solution()
    result = sol.addTwoNumbers(l1,l2)
    print_ll(result)
                
            
        