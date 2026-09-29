"""

LC: 143. Reorder List

Medium

Topics
Linked List
Two Pointers
Stack
Recursion

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,644,632/2.5M
Acceptance Rate
66.3%

"""

# Definition of a singly linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reorderList(self, head: ListNode | None) -> None:

        # --------------------------------------------------
        # STEP 1: Find the middle of the linked list
        # --------------------------------------------------

        slow = head
        fast = head

        # Slow moves 1 step
        # Fast moves 2 steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # --------------------------------------------------
        # STEP 2: Split the list into two halves
        # --------------------------------------------------

        # Second half starts after slow
        second = slow.next

        # Disconnect the first half from the second half
        slow.next = None

        # --------------------------------------------------
        # STEP 3: Reverse the second half
        # --------------------------------------------------

        prev = None
        current = second

        while current:

            # Save the next node
            next_node = current.next

            # Reverse the pointer
            current.next = prev

            # Move prev forward
            prev = current

            # Move current forward
            current = next_node

        # prev is now the first node of reversed second half
        second = prev

        # --------------------------------------------------
        # STEP 4: Merge the two halves
        # --------------------------------------------------

        first = head

        while second:

            # Save the next nodes
            first_next = first.next
            second_next = second.next

            # Connect first node to second node
            first.next = second

            # Connect second node to next first node
            second.next = first_next

            # Move both pointers forward
            first = first_next
            second = second_next

        # No return needed because we modify the list in-place


# --------------------------------------------------
# FUNCTION TO PRINT THE LINKED LIST
# --------------------------------------------------

def print_list(head):
    current = head

    while current:
        print(current.val, end="")

        if current.next:
            print(" -> ", end="")

        current = current.next

    print()


# --------------------------------------------------
# CREATE TEST LINKED LIST
# --------------------------------------------------

# Creating:
# 1 -> 2 -> 3 -> 4 -> 5

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


# Print before reordering
print("Before:")
print_list(head)


# Reorder the list
solution = Solution()
solution.reorderList(head)


# Print after reordering
print("After:")
print_list(head)



# ========EXPLANATION========
class Solution:

    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything.
        Modify the linked list in-place.
        """

        # --------------------------------------------------
        # STEP 1: Find the middle of the linked list
        # --------------------------------------------------

        slow = head
        fast = head

        # slow moves 1 step
        # fast moves 2 steps
        # When fast reaches the end, slow is at the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # --------------------------------------------------
        # STEP 2: Split the list into two halves
        # --------------------------------------------------

        # second starts from the node after the middle
        second = slow.next

        # Break the connection between the two halves
        slow.next = None


        # --------------------------------------------------
        # STEP 3: Reverse the second half
        # --------------------------------------------------

        prev = None
        current = second

        while current:

            # Save the next node before changing the pointer
            next_node = current.next

            # Reverse the current node's pointer
            current.next = prev

            # Move prev forward
            prev = current

            # Move current forward
            current = next_node

        # prev is now the head of the reversed second half
        second = prev


        # --------------------------------------------------
        # STEP 4: Merge the two halves
        # --------------------------------------------------

        first = head

        while second:

            # Save the next nodes before changing pointers
            first_next = first.next
            second_next = second.next

            # Connect first node to second node
            first.next = second

            # Connect second node to the next first node
            second.next = first_next

            # Move first pointer forward
            first = first_next

            # Move second pointer forward
            second = second_next

        # No return value is required
        return