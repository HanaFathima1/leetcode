"""

LC: 23. Merge k Sorted Lists

Hard

Topics
Linked List
Divide and Conquer
Heap (Priority Queue)
Merge Sort

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,812,154/4.8M
Acceptance Rate
58.5%

"""

import heapq
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function: build linked list from Python list
def build_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

# Helper function: print linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        return dummy.next

# ------------------ TESTING ------------------

# Create input lists
l1 = build_list([1,4,5])
l2 = build_list([1,3,4])
l3 = build_list([2,6])

lists = [l1, l2, l3]

# Run solution
sol = Solution()
result = sol.mergeKLists(lists)

# Print output
print("Merged list:")
print_list(result)
