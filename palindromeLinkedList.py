"""

LC: 234. Palindrome Linked List

Easy

Topics:
Linked List
Two Pointers
Stack
Recursion

Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

 
Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?

"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Step 3: Compare first and second halves
        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

# Helper function to create linked list from list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test Cases
test1 = create_linked_list([1, 2, 2, 1])
test2 = create_linked_list([1, 2])
test3 = create_linked_list([1, 2, 3, 2, 1])

sol = Solution()
print("Test1:", sol.isPalindrome(test1))  # Expected: True
print("Test2:", sol.isPalindrome(test2))  # Expected: False
print("Test3:", sol.isPalindrome(test3))  # Expected: True
