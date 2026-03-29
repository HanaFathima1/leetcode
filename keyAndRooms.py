"""

LC: 841. Keys and Rooms

Medium

Topics
Depth-First Search
Breadth-First Search
Graph
Weekly Contest 86

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

 

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
 

Constraints:

n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
634,024/843.2K
Acceptance Rate
75.2%

"""
from collections import deque
class Solution:
    def canVisitAllRooms(self,rooms:list[list[int]]) -> bool:
        visited=set([0])
        queue=deque([0])
        while queue:
            room=queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)
        return len(visited)==len(rooms)
sol = Solution()
print(sol.canVisitAllRooms(rooms = [[1],[2],[3],[]]))
print(sol.canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]]))


#--------------OR(DFS)-------------

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()

        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                dfs(key)

        dfs(0)
        return len(visited) == len(rooms)

                    
