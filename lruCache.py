"""

LC: 146. LRU Cache

Medium

Topics
Hash Table
Linked List
Design
Doubly-Linked List

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
2,663,715/5.6M
Acceptance Rate
47.6%

"""

class Node:
    def __init__(self, key=0, value=0):
        self.key = key          # Store the key
        self.value = value      # Store the value
        self.prev = None        # Pointer to previous node
        self.next = None        # Pointer to next node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary: key -> node

        # Create dummy head and tail nodes
        self.head = Node()
        self.tail = Node()

        # Connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert a node right after the head
    def insert(self, node):
        first = self.head.next

        node.next = first
        node.prev = self.head

        self.head.next = node
        first.prev = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move the node to the front (most recently used)
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # If key already exists, remove old node
        if key in self.cache:
            self.remove(self.cache[key])

        # Create a new node
        node = Node(key, value)

        # Store it in dictionary
        self.cache[key] = node

        # Insert at front
        self.insert(node)

        # If capacity exceeded, remove least recently used
        if len(self.cache) > self.capacity:

            # LRU node is before tail
            lru = self.tail.prev

            self.remove(lru)

            del self.cache[lru.key]