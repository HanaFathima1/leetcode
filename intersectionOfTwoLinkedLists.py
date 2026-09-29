"""

LC: 160. Intersection of Two Linked Lists

Easy

Topics
Hash Table
Linked List
Two Pointers

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
 

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
2,578,417/4M
Acceptance Rate
64.8%

"""

class LinkedList:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def getIntersectionNode(headA,headB):
    p1=headA
    p2=headB
    while p1!=p2:
        p1=p1.next if p1 else headB
        p2=p2.next if p2 else headA
    return p1
def create_from_list(values):
    head=LinkedList(values[0])
    current=head
    for val in values[1:]:
        current.next=LinkedList(val)
        current=current.next
    return head
def print_ll(head):
    while head:
        print(head.val, end="->" if head.next else "\n")
        head=head.next
# ---------------------------------
# Create the COMMON part
# ---------------------------------

common = create_from_list([8, 4, 5])


# ---------------------------------
# Create List A
# ---------------------------------

headA = create_from_list([4, 1])

current = headA

# Go to the end of A
while current.next:
    current = current.next

# Connect A to the COMMON nodes
current.next = common


# ---------------------------------
# Create List B
# ---------------------------------

headB = create_from_list([5, 6, 1])

current = headB

# Go to the end of B
while current.next:
    current = current.next

# Connect B to the SAME common nodes
current.next = common


# ---------------------------------
# Find intersection
# ---------------------------------

intersection = getIntersectionNode(headA, headB)


# ---------------------------------
# Print intersection
# ---------------------------------

if intersection:
    print("Intersection node:", intersection.val)
    print_ll(intersection)
else:
    print("No intersection")
    
    
#==================explanation=======================
# =========================================================
# LEETCODE 160 - INTERSECTION OF TWO LINKED LISTS
# =========================================================


# ---------------------------------------------------------
# 1. Create a Linked List Node
# ---------------------------------------------------------

class LinkedList:

    def __init__(self, val=0, next=None):

        # Store the value of the node
        self.val = val

        # Store the address/reference of the next node
        self.next = next


# ---------------------------------------------------------
# 2. Find the Intersection Node
# ---------------------------------------------------------

def getIntersectionNode(headA, headB):

    # Pointer p1 starts from the beginning of List A
    p1 = headA

    # Pointer p2 starts from the beginning of List B
    p2 = headB

    # Continue until both pointers point to
    # the EXACT SAME NODE
    while p1 != p2:

        # If p1 is not at the end:
        # move p1 to the next node
        #
        # If p1 reaches None:
        # start p1 from the beginning of List B
        p1 = p1.next if p1 else headB

        # If p2 is not at the end:
        # move p2 to the next node
        #
        # If p2 reaches None:
        # start p2 from the beginning of List A
        p2 = p2.next if p2 else headA

    # When the loop ends:
    #
    # p1 == p2
    #
    # They are either:
    # 1. The intersection node
    # 2. None if there is no intersection
    return p1


# ---------------------------------------------------------
# 3. Create a Linked List from a Python List
# ---------------------------------------------------------

def create_from_list(values):

    # Create the first node
    #
    # Example:
    # values = [8, 4, 5]
    #
    # head = 8
    head = LinkedList(values[0])

    # current is used to move through the linked list
    current = head

    # Start creating the remaining nodes
    for val in values[1:]:

        # Create a new node and connect it
        # to the current node
        current.next = LinkedList(val)

        # Move current to the newly created node
        current = current.next

    # Return the first node of the linked list
    return head


# ---------------------------------------------------------
# 4. Print a Linked List
# ---------------------------------------------------------

def print_ll(head):

    # Start from the first node
    while head:

        # Print the current node's value
        #
        # If there is another node:
        # print ->
        #
        # Otherwise print a new line
        print(head.val, end="->" if head.next else "\n")

        # Move to the next node
        head = head.next


# =========================================================
# CREATE THE COMMON PART
# =========================================================

# We first create the part that will be shared
# by BOTH linked lists.
#
# common:
#
#       8 → 4 → 5 → None
#
# IMPORTANT:
# These are actual NODE OBJECTS.
# Both lists will point to these SAME nodes.

common = create_from_list([8, 4, 5])


# =========================================================
# CREATE LIST A
# =========================================================

# Create the unique part of List A:
#
# 4 → 1 → None

headA = create_from_list([4, 1])

# current starts at the beginning of List A
current = headA


# Move current until we reach the LAST node.
#
# Initially:
#
# current
#    ↓
#    4 → 1 → None
#
# After the loop:
#
#         current
#            ↓
#    4 → 1 → None

while current.next:
    current = current.next


# Now current is pointing to node 1.
#
# Connect node 1 to the COMMON part.
#
# Before:
#
# 4 → 1 → None
#
# common:
#
# 8 → 4 → 5
#
# After:
#
# 4 → 1 → 8 → 4 → 5
#          ↑
#       common

current.next = common


# =========================================================
# CREATE LIST B
# =========================================================

# Create the unique part of List B:
#
# 5 → 6 → 1 → None

headB = create_from_list([5, 6, 1])

# Start at the beginning of List B
current = headB


# Move current to the last node.
#
# Initially:
#
# current
#    ↓
#    5 → 6 → 1 → None
#
# After the loop:
#
#              current
#                 ↓
#    5 → 6 → 1 → None

while current.next:
    current = current.next


# Connect the last node of B
# to the SAME common part.
#
# List B becomes:
#
# 5 → 6 → 1 → 8 → 4 → 5
#             ↑
#           common

current.next = common


# =========================================================
# IMPORTANT STRUCTURE
# =========================================================

# Now the actual structure is:
#
#
# List A:
#
# 4 → 1 ──────────┐
#                 ↓
#                 8 → 4 → 5
#                 ↑
#                 │
# List B:         │
# 5 → 6 → 1 ──────┘
#
#
# The nodes 8, 4, 5 are the SAME nodes.
#
# Therefore, this is a REAL intersection.
#
# We are NOT just using the same values.
# We are using the same node objects.


# =========================================================
# FIND THE INTERSECTION
# =========================================================

intersection = getIntersectionNode(headA, headB)


# =========================================================
# PRINT THE RESULT
# =========================================================

if intersection:

    # Print the value of the intersection node
    print("Intersection node:", intersection.val)

    # Print the remaining part of the list
    print_ll(intersection)

else:

    # If there is no intersection
    print("No intersection")
    
    
    
"""
the complete dry run

Our lists are:

List A:

4 → 1 ─────────┐
               ↓
               8 → 4 → 5
               ↑
               │
5 → 6 → 1 ─────┘

List B

So:

A = 4 → 1 → 8 → 4 → 5
B = 5 → 6 → 1 → 8 → 4 → 5

But remember:

A's 8
   ↓
same node
   ↑
B's 8
Step 1: Initialize pointers

Inside:

p1 = headA
p2 = headB

We get:

p1 → 4 → 1 → 8 → 4 → 5

p2 → 5 → 6 → 1 → 8 → 4 → 5

So:

p1 = 4
p2 = 5

They are different.

Iteration 1

Condition:

while p1 != p2:
4 != 5

True.

Move both:

p1 = p1.next
p2 = p2.next

Now:

p1 → 1

p2 → 6

So:

p1 = 1
p2 = 6
Iteration 2
p1 = 1
p2 = 6

Different.

Move:

p1 → 8
p2 → 1

Now:

p1 = 8
p2 = 1
Iteration 3

Move again:

p1 → 4
p2 → 8

So:

p1 = 4
p2 = 8
Iteration 4

Move again:

p1 → 5
p2 → 4

So:

p1 = 5
p2 = 4
Iteration 5

Now p1 is at the last node:

p1 → 5 → None

p2 is at:

p2 → 4

We execute:

p1 = p1.next if p1 else headB

p1.next is None.

So:

p1 = headB

Therefore:

p1 → 5

At the same time:

p2 = p2.next

So:

p2 → 5

Now both point to a node containing 5.

But be careful: these may not be the same node depending on which 5 we mean. In this construction, p1 is now at B's first 5, while p2 is at the common final 5? Let's track precisely: after the previous iteration, p2 was at the common 4, so p2.next is the common 5. Thus they are still different nodes.

So:

p1 → B's first 5

p2 → common 5

Even though:

p1.val == p2.val

they are different nodes.

Therefore:

p1 != p2

is still true.

This is a very important point in LC 160.

Iteration 6

Now:

p1 = B's first 5
p2 = common 5

Move p1:

p1 → 6

Move p2:

p2 → None

So:

p1 = 6
p2 = None
Iteration 7

p2 has reached the end.

Therefore:

p2 = headA

So:

p1 → 6

p2 → 4
Iteration 8

Move:

p1 → 1
p2 → 1

These are still different nodes because one is B's 1 and the other is A's 1.

Iteration 9

Move:

p1 → common 8
p2 → common 8

🎯 NOW THEY ARE THE SAME NODE.

This is the key.

Not just:

p1.val == p2.val

but:

p1 == p2

because both pointers reference the exact same 8 node.

Therefore:

while p1 != p2:

becomes:

while False:

The loop stops.

Step 10: Return
return p1

p1 points to:

8 → 4 → 5

So:

intersection.val

is:

8
Final output
Intersection node: 8
8->4->5
⭐ The most important part to understand

This:

p1 = p1.next if p1 else headB
p2 = p2.next if p2 else headA

means:

If p1 reaches the end of A:
        ↓
    send it to B

If p2 reaches the end of B:
        ↓
    send it to A

So:

p1:  A → B

p2:  B → A

This makes both pointers travel the same total distance.

Eventually:

             SAME NODE
                 ↓
p1 ───────────── 8
                 ↑
p2 ─────────────

and:

p1 == p2

becomes true.

🧠 Remember LC 160 as:

Two pointers → switch heads → meet at intersection.

And the most important distinction:

p1.val == p2.val     # ❌ Not enough

p1 == p2             # ✅ Same node

That distinction is the heart of this problem.
"""
        