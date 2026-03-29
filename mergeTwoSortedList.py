"""LC:21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 
 
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to merge two sorted linked lists
def sortedMerge(head1, head2):
    arr = []  

    # Pushing the values of the first linked list
    while head1 is not None:
        arr.append(head1.data)
        head1 = head1.next

    # Pushing the values of the second linked list
    while head2 is not None:
        arr.append(head2.data)
        head2 = head2.next

    # Sorting the list
    arr.sort()

    # Creating a new list with sorted values
    dummy = Node(-1)
    curr = dummy

    for value in arr:
        curr.next = Node(value)
        curr = curr.next

    return dummy.next 

# Function to print the linked list
def printList(curr):
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()
    
if __name__ == "__main__":
  
    # First linked list: 5 -> 10 -> 15
    head1 = Node(5)
    head1.next = Node(10)
    head1.next.next = Node(15)

    # Second linked list: 2 -> 3 -> 20
    head2 = Node(2)
    head2.next = Node(3)
    head2.next.next = Node(20)

    res = sortedMerge(head1, head2)

    printList(res)
    
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def build_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
        
def mergeTwoList(l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next 
            tail = tail.next
        
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        
        return dummy.next
    
def print_linked_list(head):
        while head:
            print(head.val, end="->")
            head = head.next
        print("None")
        
l1 = build_linked_list([1,2,4])
l2 = build_linked_list([1,3,4])
print("list 1")
print_linked_list(l1)
print("list 2")
print_linked_list(l2)
    
merged_head = mergeTwoList(l1, l2)
print("Merged list: ")
print_linked_list(merged_head)
    
    
  
#-----------practice-------------
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val  
        self.next=next
        
def mergeSortedList(l1,l2):
    dummy=ListNode()
    tail=dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next=l1
            l1=l1.next
        else:
            tail.next=l2
            l2=l2.next
        tail=tail.next
    if l1:
        tail.next=l1  
    if l2:
        tail.next=l2
    return dummy.next    
    
def build_ll(values):
    if not values:
        return None  
    head=ListNode(values[0])
    current=head
    for val in values[1:]:
        current.next=ListNode(val)
        current=current.next
    return head
    
def print_ll(current):
    while current:
        print(current.val,end="->")
        current=current.next
    print("None")

l1=build_ll([1,2,4])
l2=build_ll([1,3,4])
print_ll(l1)
print_ll(l2)
merged_head=mergeSortedList(l1,l2)
print_ll(merged_head)

        
              

