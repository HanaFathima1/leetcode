""" 

LC: 24. Swap Nodes in Pairs

Medium

Topics
Linked List
Recursion

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,688,249/2.5M
Acceptance Rate
67.6%

"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next
        
class Solution:
    def swapPairs(self, head:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            first = head
            second = head.next
            
            prev.next = second
            first.next =second.next
            second.next = first
            prev = first
            
            head = first.next
            
        return dummy.next
    
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print("->".join(values))
        
if __name__ == "__main__":
    values = [1,2,3,4]
    head = build_linked_list(values)
    print_linked_list(head)
    sol = Solution()
    swapped_head = sol.swapPairs(head)
    print_linked_list(swapped_head)
    
    
    
"""

ONE-LINE MANTRA (say this in your head)

“Prev jumps to second,
first skips second,
second points to first,
move prev and head.”
------------------------------

Remember the ONE PICTURE

Always visualize only this before writing code:
prev → A → B → C

Your goal is to change it into:
prev → B → A → C


The Golden 4 Steps:
1️⃣ prev.next = B
2️⃣ A.next = C
3️⃣ B.next = A
4️⃣ move prev to A
That’s the entire logic.

--------------------------

Line-by-line explanation

1️⃣ Function definition

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

This defines the function.

head is the first node of the linked list.

It will return the new head of the list after swapping.

2️⃣ Create a dummy node

dummy = ListNode(0)

You create a fake node called dummy with value 0.

This node is placed before the real head.

Reason:
When you swap the first pair, the head of the list changes.
Using dummy makes it easy to handle this change.

3️⃣ Attach dummy to the list

dummy.next = head

Now the list looks like:

dummy → head → ...

Example: if list is

1 → 2 → 3 → 4

then:

dummy → 1 → 2 → 3 → 4

4️⃣ Initialize prev

prev = dummy

prev will always point to the node just before the current pair you are swapping.

At the start:

prev = dummy

current pair will start at head.

5️⃣ Start the loop

while head and head.next:

This means:

Continue only if:

head exists (not None), and

head.next exists (there is a pair).

So you only run the loop when there are at least 2 nodes left to swap.

6️⃣ Identify nodes of the pair

first = head

first is the first node in the pair.

Example (current list):

prev → ? → 1 → 2 → 3 → 4

Here, initially:

head → 1

So first → 1

second = head.next

second is the second node in the pair.

Continuing example:

second → 2

So your current picture is:

prev → dummy → 1 → 2 → 3 → 4
first = 1
second = 2

7️⃣ Step 1 of swapping – connect prev to second

prev.next = second

You are changing the link from prev to point to second instead of first.

Before:

prev.next → first (1)

After:

prev.next → second (2)

Now structure:

dummy → 2 → 1 → 3 → 4 (conceptually; but we’ll fully fix links in the next lines)

8️⃣ Step 2 of swapping – move first.next

first.next = second.next

first currently is node 1.

second.next is 3.

So now:

first.next = 3

Now list effectively becomes:

dummy → 2 → 1 → 3 → 4

(Pair 2 → 1 is almost done.)

9️⃣ Step 3 of swapping – point second to first

second.next = first

second is 2.

You now set:

2.next = 1

So final swapped pair:

2 → 1

And with the rest of the list:

dummy → 2 → 1 → 3 → 4

🎉 First pair successfully swapped.

🔟 Move prev forward

prev = first

After the swap, the pair is:

2 → 1

first is 1 (second node in the swapped pair now).

Setting prev = first means:

prev now points to node 1.

Why?
Because in the next iteration, prev should be the node before the next pair.
And the next pair will start after 1.

So now:

prev → 1

1️⃣1️⃣ Move head to the next pair

head = first.next

first is 1.

first.next is 3.

So:

head now points to 3.

This prepares for the next pair, which will be:

3 and 4.

So current situation:

List: dummy → 2 → 1 → 3 → 4

prev → 1

head → 3

Loop repeats.

Next iteration (for pair 3 and 4)

Now inside the loop again:

head = 3

head.next = 4

So:

first = 3
second = 4

Then again:

prev.next = second
→ 1.next = 4

first.next = second.next
→ 3.next = None (if 4.next is None)

second.next = first
→ 4.next = 3

prev = first
→ prev = 3

head = first.next
→ head = 3.next → None

List is now:

dummy → 2 → 1 → 4 → 3

Loop ends because head is now None.

1️⃣2️⃣ Return the real head

return dummy.next

Remember we started with a fake dummy node.

The real new head of the swapped list is:

dummy.next

So final output is:

2 → 1 → 4 → 3

Mini summary in plain words 🧠

For every pair:

Take first = head, second = head.next.

Connect previous part of list (prev) to second.

Make first skip over second (first.next = second.next).

Point second back to first.

Move prev to first.

Move head to the node after first (next pair).

If you want, next I can:

Do a full dry run with your own example (you choose the list), or

Show a recursive version with the same easy explanation.

You said:
give a dry run
ChatGPT said:

Perfect 👍
Let’s do a clean, slow dry run with only pointer movement, no extra theory.

We’ll use this input:

1 → 2 → 3 → 4

Initial setup
dummy = 0
dummy.next = 1
prev = dummy
head = 1


So the list looks like:

0 → 1 → 2 → 3 → 4
↑
dummy, prev

🔁 WHILE LOOP — 1st iteration

Condition:

head = 1
head.next = 2
✅ true

Step 1: Assign pair nodes
first  = head       → 1
second = head.next  → 2


Current structure:

prev → 0 → 1 → 2 → 3 → 4
            ↑    ↑
          first second

Step 2: Connect prev to second
prev.next = second


Now:

0 → 2 → 1 → 3 → 4   (temporary state)


Pointer view:

prev → 0 → 2
first → 1
second → 2

Step 3: Move first.next
first.next = second.next


Which means:

1.next = 3


Now list:

0 → 2 → 1 → 3 → 4

Step 4: Complete the swap
second.next = first


Which means:

2.next = 1


✅ Pair swapped:

0 → 2 → 1 → 3 → 4

Step 5: Move prev
prev = first


Now:

prev → 1

Step 6: Move head
head = first.next


Which means:

head = 3

✅ End of 1st iteration state
0 → 2 → 1 → 3 → 4
        ↑    ↑
      prev  head

🔁 WHILE LOOP — 2nd iteration

Condition:

head = 3
head.next = 4
✅ true

Step 1: Assign pair nodes
first  = 3
second = 4

0 → 2 → 1 → 3 → 4
              ↑   ↑
           first second

Step 2: Connect prev to second
prev.next = second

0 → 2 → 1 → 4 → 3

Step 3: Move first.next
first.next = second.next

3.next = None

Step 4: Complete the swap
second.next = first


✅ Pair swapped:

0 → 2 → 1 → 4 → 3

Step 5: Move prev
prev = first

prev → 3

Step 6: Move head
head = first.next

head = None

🔚 Loop ends

Condition fails:

head = None
❌ stop

✅ Final return
return dummy.next


Ignoring dummy:

2 → 1 → 4 → 3

🧠 ONE-LINE MEMORY TRICK

For each pair:

prev → A → B → C


Change to:

prev → B → A → C


Then move:

prev = A
head = C
"""