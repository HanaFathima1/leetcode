"""

LC: 61. Rotate List

Medium

Topics
Linked List
Two Pointers

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,764,344/4.1M
Acceptance Rate
42.8%

"""

from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # If the list is empty, has one node, or no rotation is needed
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the list and the last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Reduce k if it is larger than the length
        k = k % length

        # If k becomes 0, no rotation is needed
        if k == 0:
            return head

        # Step 3: Make the linked list circular
        tail.next = head

        # Step 4: Find the new tail
        newTail = head
        for _ in range(length - k - 1):
            newTail = newTail.next

        # Step 5: The next node becomes the new head
        newHead = newTail.next

        # Step 6: Break the circular list
        newTail.next = None

        return newHead


# -----------------------------
# Create a linked list from a Python list
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
# Print a linked list
# -----------------------------
def printLinkedList(head):
    if not head:
        print("Empty List")
        return

    current = head
    while current:
        print(current.val, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
    print()


# -----------------------------
# Test Cases
# -----------------------------
sol = Solution()

test_cases = [
    ([1, 2, 3, 4, 5], 2),
    ([0, 1, 2], 4),
    ([1], 5),
    ([], 3),
    ([1, 2], 1),
]

for i, (arr, k) in enumerate(test_cases, start=1):
    print(f"\nTest Case {i}")
    print("Input List :", arr)
    print("k =", k)

    head = createLinkedList(arr)

    print("Before Rotation:")
    printLinkedList(head)

    result = sol.rotateRight(head, k)

    print("After Rotation:")
    printLinkedList(result)
    
"""

Dry Run

Input

1 → 2 → 3 → 4 → 5
k = 2

| Step            | Length | Tail | New Tail | New Head | List          |
| --------------- | ------ | ---- | -------- | -------- | ------------- |
| Initial         | 5      | 5    | -        | -        | 1→2→3→4→5     |
| Make Circular   | 5      | 5→1  | -        | -        | Circle        |
| Steps = 5−2−1=2 | 5      | -    | 3        | -        | Circle        |
| New Head        | 5      | -    | 3        | 4        | Circle        |
| Break           | 5      | -    | 3        | 4        | **4→5→1→2→3** |

Complexity
Time: O(n) — one pass to compute the length and one partial pass to find the new tail.
Space: O(1) — only a few pointers are used.

"""
        
        
            
            