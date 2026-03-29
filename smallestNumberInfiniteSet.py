"""

LC: 2336. Smallest Number in Infinite Set

Medium

Topics
Hash Table
Design
Heap (Priority Queue)
Ordered Set
Weekly Contest 301

Hint
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
 

Constraints:

1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
222,486/315.3K
Acceptance Rate
70.6%

Hint 1
Based on the constraints, what is the maximum element that can possibly be popped?
Hint 2
Maintain whether elements are in or not in the set. How many elements do we consider?

"""

import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.curr=1
        self.minHeap=[]
        self.present=set()
    def popSmallest(self)->int:
        if self.minHeap:
            smallest=heapq.heappop(self.minHeap)
            self.present.remove(smallest)
            return smallest
        val=self.curr
        self.curr+=1
        return val
    def addBack(self,num:int)->None:
        if num<self.curr and num not in self.present:
            heapq.heappush(self.minHeap,num)
            self.present.add(num)
obj = SmallestInfiniteSet()

print(obj.popSmallest())  # 1
print(obj.popSmallest())  # 2
obj.addBack(1)
print(obj.popSmallest())  # 1
print(obj.popSmallest())  # 3
print(obj.popSmallest())  # 4
obj.addBack(2)
print(obj.popSmallest())  # 2
