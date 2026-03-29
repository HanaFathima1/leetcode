# LC-876
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slow = head
#         fast = head
#         if not head:
#             return None
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow

# sol=Solution()
# print(sol.middleNode([1,2,3,4,5]))

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
            
    def print_from_node(self,node):
        while node:
            print(node.data, end="->")
            node = node.next
        print("None")
    
    def middleNode(self):
        slow = self.head
        fast = self.head
        if not self.head:
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
ll = LinkedList()
ll.create_from_list([1,2,3,4,5])
middle = ll.middleNode()
ll.print_from_node(middle)