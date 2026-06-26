"""

LC: 92. Reverse Linked List II

Medium

Topics
Linked List

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,349,115/2.6M
Acceptance Rate
51.7%

"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # If the list is empty or no reversal is needed, return the head.
        if not head or left == right:
            return head

        # Create a dummy node to simplify handling the case
        # where the reversal starts from the first node.
        dummy = ListNode(0)
        dummy.next = head

        # 'prev' will eventually point to the node just before
        # the start of the reversal.
        prev = dummy

        # Move 'prev' to the node before position 'left'.
        for _ in range(left - 1):
            prev = prev.next

        # 'current' points to the first node that will be reversed.
        current = prev.next

        # Reverse the sublist using the head insertion technique.
        for _ in range(right - left):

            # Node to be moved to the front of the reversed part.
            next_node = current.next

            # Remove next_node from its current position.
            current.next = next_node.next

            # Insert next_node immediately after prev.
            next_node.next = prev.next

            # Update prev to point to the new first node of the reversed part.
            prev.next = next_node

        # Return the new head.
        return dummy.next
    
# ---------------- Helper Functions ----------------

# Create a linked list from a Python list
def createLinkedList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# Print the linked list
def printLinkedList(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()


# ---------------- Driver Code ----------------

head = createLinkedList([1, 2, 3, 4, 5])

print("Original Linked List:")
printLinkedList(head)

sol = Solution()

new_head = sol.reverseBetween(head, 2, 4)

print("\nLinked List after Reversing:")
printLinkedList(new_head)

"""        
Dry Run
Input
head = 1 → 2 → 3 → 4 → 5
left = 2
right = 4

Initially

dummy → 1 → 2 → 3 → 4 → 5
          ^
         prev

Move prev once (left - 1 = 1):

dummy → 1 → 2 → 3 → 4 → 5
          ^
         prev
            ^
         current

current = 2

Iteration 1

next_node = 3

Remove 3:

1 → 2 → 4 → 5

Insert 3 after prev:

1 → 3 → 2 → 4 → 5
Iteration 2

next_node = 4

Remove 4:

1 → 3 → 2 → 5

Insert 4 after prev:

1 → 4 → 3 → 2 → 5

Done!

Why does the loop run right - left times?

Suppose

left = 2
right = 4

Nodes to reverse:

2 → 3 → 4

The first node (2) stays as the tail of the reversed portion. We repeatedly move each following node (3, then 4) to the front of the sublist.

So the number of moves needed is:

(number of nodes) - 1
= (right - left + 1) - 1
= right - left
Time Complexity
Traversing to the left position: O(left)
Reversing the sublist: O(right - left)

Overall:

Time: O(n)
Space: O(1)
"""

#=======================================================

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # If the list is empty or only one node is to be reversed,
        # return the original list.
        if not head or left == right:
            return head

        # Create a dummy node to handle the case when left = 1.
        dummy = ListNode(0)
        dummy.next = head

        # 'prev' will point to the node before the reversal starts.
        prev = dummy

        # Move prev to the (left-1)th node.
        for _ in range(left - 1):
            prev = prev.next

        # 'current' points to the first node of the sublist.
        current = prev.next

        # Store the first node of the sublist.
        # After reversal, this node becomes the last node.
        reverse_start = current

        # Initialize previous pointer for reversing.
        previous = None

        # Reverse exactly (right - left + 1) nodes.
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        # Connect the node before the reversed sublist
        # to the new first node of the reversed sublist.
        prev.next = previous

        # Connect the last node of the reversed sublist
        # to the remaining part of the list.
        reverse_start.next = current

        # Return the new head.
        return dummy.next
    
# ---------------- Helper Function ----------------

def create_linked_list(values):
    """Creates a linked list from a Python list."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def print_linked_list(head):
    """Prints the linked list."""
    while head:
        print(head.val, end="")
        if head.next:
            print(" -> ", end="")
        head = head.next
    print()


# ---------------- Driver Code ----------------

# Input list
values = [1, 2, 3, 4, 5]

# Create linked list
head = create_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

# Input positions
left = 2
right = 4

print(f"\nReverse from position {left} to {right}")

# Call solution
solution = Solution()
new_head = solution.reverseBetween(head, left, right)

print("\nLinked List After Reversal:")
print_linked_list(new_head)


"""
Dry Run
Input
1 → 2 → 3 → 4 → 5
left = 2
right = 4
Before reversing
dummy → 1 → 2 → 3 → 4 → 5
          ↑    ↑
         prev current

reverse_start = 2

Iteration 1

Reverse 2

previous = 2
current = 3

2 → None
Iteration 2

Reverse 3

3 → 2

previous = 3
current = 4
Iteration 3

Reverse 4

4 → 3 → 2

previous = 4
current = 5
Reconnect
prev.next = previous

1 → 4 → 3 → 2
reverse_start.next = current

2 → 5

Final list:

1 → 4 → 3 → 2 → 5
Time Complexity
Time: O(n)
Space: O(1)
"""