"""

LC: 206. Reverse Linked List

Easy

Topics
Linked List
Recursion

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
6,755,888/8.3M
Acceptance Rate
81.1%

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def create_from_list(self, values):
        if not values:
            return None
        self.head = Node(values[0])
        current = self.head
        for val in values[1:]:
            current.next = Node(val)
            current = current.next
    
    def print_list(self, head):
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

        
    def reversell(self,head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
ll = LinkedList()
ll.create_from_list([1,2,3,4,5])
reversed_head = ll.reversell(ll.head)
ll.print_list(reversed_head)
# print(ll.reversell([1,2,3,4,5]))

        
    