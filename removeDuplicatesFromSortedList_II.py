"""

LC: 82. Remove Duplicates from Sorted List II

Medium

Topics
Linked List
Two Pointers

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,129,002/2.2M
Acceptance Rate
52.0%

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Create a dummy node before the head.
        # This helps handle cases where the first few nodes are duplicates.
        dummy = ListNode(0)
        dummy.next = head

        # prev always points to the last node that is confirmed to be unique.
        prev = dummy

        # curr is used to traverse the linked list.
        curr = head

        # Traverse the list until curr becomes None.
        while curr:

            # Check if the current node is the start of a duplicate group.
            if curr.next and curr.val == curr.next.val:

                # Skip all nodes having the same value.
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                # Remove the entire duplicate group.
                # Connect prev directly to the first non-duplicate node.
                prev.next = curr.next

            else:
                # Current node is unique.
                # Move prev forward.
                prev = prev.next

            # Move curr to the next node.
            curr = curr.next

        # Return the updated linked list.
        return dummy.next


# -----------------------------
# Helper function to create linked list
# -----------------------------
def createLinkedList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# -----------------------------
# Helper function to print linked list
# -----------------------------
def printLinkedList(head):
    if not head:
        print("Empty List")
        return

    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()


# -----------------------------
# Test Cases
# -----------------------------
sol = Solution()

test_cases = [
    [1, 2, 3, 3, 4, 4, 5],
    [1, 1, 1, 2, 3],
    [1, 1],
    [1, 2, 2],
    [1, 2, 3],
    [],
]

for i, arr in enumerate(test_cases, 1):
    print(f"\nTest Case {i}")
    print("Input : ", arr)

    head = createLinkedList(arr)

    print("Linked List Before:")
    printLinkedList(head)

    result = sol.deleteDuplicates(head)

    print("Linked List After:")
    printLinkedList(result)
    
    
"""
Dry Run
Input
1 → 2 → 3 → 3 → 4 → 4 → 5

Initially

dummy → 1 → 2 → 3 → 3 → 4 → 4 → 5
         ↑
        curr

prev = dummy
Iteration 1
curr = 1

No duplicate.

prev = 1
curr = 2
Iteration 2
curr = 2

No duplicate.

prev = 2
curr = 3
Iteration 3
curr = 3
curr.next = 3

Duplicate found.

Skip duplicates

3 → 3

Now

curr = second 3

Connect

prev.next = curr.next

List becomes

dummy → 1 → 2 → 4 → 4 → 5

Move

curr = 4
Iteration 4
curr = 4
curr.next = 4

Duplicate found.

Skip duplicates.

Connect

prev.next = 5

List becomes

dummy → 1 → 2 → 5
Iteration 5
curr = 5

Unique.

prev = 5
curr = None

Stop.

Output

1 → 2 → 5
Why do we need a dummy node?

Consider:

1 → 1 → 2 → 3

The expected output is:

2 → 3

If there were no dummy node, there would be no node before 1 to reconnect the list after removing the duplicate group. By introducing:

dummy → 1 → 1 → 2 → 3

we can simply do:

prev.next = curr.next

to obtain:

dummy → 2 → 3

and finally return:

dummy.next
Time Complexity
Each node is visited at most once.

Time: O(n)

Space Complexity

Only a few pointers (dummy, prev, curr) are used.

Space: O(1)
"""