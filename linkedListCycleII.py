"""

LC: 142. Linked List Cycle II

Medium

Topics
Hash Table
Linked List
Two Pointers
Floyd's Cycle Finding Algorithm

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
2,216,718/3.7M
Acceptance Rate
59.3%

"""
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if not fast or not fast.next:
            return None
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
def create_from_list(values,pos):
    if not values:
        return []
    node=[]
    for val in values:
        node.append(ListNode(val))
    for i in range(len(values)-1):
        node[i].next=node[i+1]
    if pos!=-1:
        node[-1].next=node[pos]
    return node[0]
values=[3,2,0,-4]
pos=1
head=create_from_list(values,pos)
sol=Solution()
res=sol.detectCycle(head)
if res:
    print("Cycle starts at node:", res.val)
else:
    print("No cycle")

    
#explanation  

from typing import Optional


# A node represents one element of the linked list
class ListNode:

    # Constructor for creating a node
    def __init__(self, x):

        # Store the value inside the node
        self.val = x

        # Initially, the node does not point to anything
        self.next = None


class Solution:

    # This function finds the node where the cycle begins
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # slow moves one node at a time
        slow = head

        # fast moves two nodes at a time
        fast = head

        # Continue as long as fast has a node to move to
        while fast and fast.next:

            # Move slow by ONE step
            slow = slow.next

            # Move fast by TWO steps
            fast = fast.next.next

            # If slow and fast meet,
            # a cycle definitely exists
            if slow == fast:
                break

        # If fast reached the end,
        # there is NO cycle
        if not fast or not fast.next:
            return None

        # We found a cycle.
        # Move slow back to the head
        slow = head

        # Now both slow and fast move ONE step at a time
        while slow != fast:

            # Move slow one step
            slow = slow.next

            # Move fast one step
            fast = fast.next

        # slow and fast meet at the START of the cycle
        return slow


# --------------------------------------------------
# FUNCTION TO CREATE A LINKED LIST FOR TESTING
# --------------------------------------------------

def create_from_list(values, pos):

    # If the values list is empty,
    # there is no linked list
    if not values:
        return []

    # This Python list will store all the ListNode objects
    node = []

    # Create one ListNode for every value
    for val in values:

        # Create a node and store it in node[]
        node.append(ListNode(val))

    # Connect each node to the next node
    for i in range(len(values) - 1):

        # Example:
        # node[0] -> node[1]
        # node[1] -> node[2]
        # node[2] -> node[3]
        node[i].next = node[i + 1]

    # If pos is not -1,
    # create a cycle
    if pos != -1:

        # node[-1] means the LAST node
        #
        # node[pos] means the node where
        # the cycle should start
        #
        # So the last node points back to node[pos]
        node[-1].next = node[pos]

    # Return the first node because it is the head
    return node[0]


# --------------------------------------------------
# TEST INPUT
# --------------------------------------------------

# Values stored in the linked list
values = [3, 2, 0, -4]

# The last node (-4) should connect to index 1
# index 1 contains the value 2
pos = 1


# Create the linked list
head = create_from_list(values, pos)


# Create an object of Solution
sol = Solution()


# Find the beginning of the cycle
res = sol.detectCycle(head)


# If res is not None,
# a cycle was found
if res:

    # Print the value of the cycle's starting node
    print("Cycle starts at node:", res.val)

else:

    # No cycle was found
    print("No cycle")
    
"""
First understand what create_from_list() creates

Your input is:

values = [3, 2, 0, -4]
pos = 1

The indices are:

index:     0    1    2     3
           ↓    ↓    ↓     ↓
value:     3    2    0    -4

First this creates four separate nodes:

node[0] = 3
node[1] = 2
node[2] = 0
node[3] = -4

Then this loop:

for i in range(len(values) - 1):
    node[i].next = node[i + 1]

connects them:

3 → 2 → 0 → -4

Then:

node[-1].next = node[pos]

Since:

node[-1] = node[3] = -4
node[pos] = node[1] = 2

we get:

3 → 2 → 0 → -4
    ↑         |
    └─────────┘

So the cycle begins at node 2.

3. Dry run of detectCycle()

Now:

head = 3

Initially:

slow = head
fast = head

So:

slow
 ↓
3 → 2 → 0 → -4
    ↑         |
    └─────────┘
 ↑
fast
Phase 1 — Detect whether a cycle exists

The code:

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
Iteration 1

Initially:

slow = 3
fast = 3

Move slow one step:

slow = slow.next

So:

slow = 2

Move fast two steps:

fast = fast.next.next

From 3:

3 → 2 → 0

So:

fast = 0

Now:

slow = 2
fast = 0

They are not equal.

Iteration 2

Current:

slow = 2
fast = 0

Move slow one step:

slow = 0

Move fast two steps:

0 → -4 → 2

So:

fast = 2

Now:

slow = 0
fast = 2

Not equal.

Iteration 3

Current:

slow = 0
fast = 2

Move slow:

slow = -4

Move fast two steps:

2 → 0 → -4

So:

fast = -4

Now:

slow = -4
fast = -4

They meet!

Therefore:

if slow == fast:
    break

executes.

Important!

At this point we know:

A cycle exists.

But -4 is not necessarily the beginning of the cycle.

The cycle actually begins at 2.

This is why we need Phase 2.

4. Phase 2 — Find the beginning of the cycle

We execute:

slow = head

So slow goes back to the beginning:

slow = 3
fast = -4

Remember:

3 → 2 → 0 → -4
    ↑         |
    └─────────┘

Now:

while slow != fast:

Both pointers move one step at a time.

Iteration 1

Current:

slow = 3
fast = -4

Move slow:

3 → 2

So:

slow = 2

Move fast:

-4 → 2

So:

fast = 2

Now:

slow == fast

The loop stops.

5. Return the cycle's starting node
return slow

slow points to:

Node(2)

Therefore:

res.val

is:

2

Output:

Cycle starts at node: 2
The most important concept to remember

LeetCode 142 has two phases.

Phase 1 — Detect cycle
slow = slow.next
fast = fast.next.next

If:

slow == fast

then:

Cycle exists.

But don't return slow yet.

Phase 2 — Find cycle beginning
slow = head

while slow != fast:
    slow = slow.next
    fast = fast.next

return slow

When they meet again:

That node is the beginning of the cycle.

So the pattern to memorize is:

PHASE 1
slow → 1 step
fast → 2 steps
       ↓
    meet?
       ↓
   cycle exists

PHASE 2
slow → back to head
fast → stays at meeting point

slow → 1 step
fast → 1 step
       ↓
    meet again
       ↓
cycle starting node

"""
        