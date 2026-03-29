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

        
    