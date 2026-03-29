"""

LC: 79. Word Search
Medium

Topics
Array
String
Backtracking
Depth-First Search
Matrix

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,434,852/5.2M
Acceptance Rate
46.9%

"""

class Solution:
    def exist(self, board:list[list[str]],word:str)->bool:
        rows=len(board)
        cols=len(board[0])
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=cols:
                return False
            if board[r][c]!=word[i]:
                return False
            temp=board[r][c]
            board[r][c]="#"
            
            found=(
                dfs(r+1,c,i+1) or
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1)
            )
            board[r][c]=temp
            return found
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
    
sol=Solution()
print(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
print(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
   
   
   
   
   
"""

dry run:

1️⃣ Example

Grid:

A B C E
S F C S
A D E E

Word to search:

ABCCED

Coordinates (row, col):

(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
2️⃣ Starting the Algorithm

The algorithm checks every cell as a starting point.

Loop:

for r in rows:
    for c in cols:
        dfs(r,c,0)

Start at (0,0).

dfs(0,0,0)

Meaning:

board[0][0] = A
word[0] = A

Match ✅

3️⃣ Mark Cell Visited

We temporarily mark visited:

board[0][0] = "#"

Grid becomes:

# B C E
S F C S
A D E E

Now we search next letter:

word[1] = B
4️⃣ Explore 4 Directions

From (0,0) we try:

down  → (1,0)
up    → (-1,0)
right → (0,1)
left  → (0,-1)
Down
board[1][0] = S

Expected:

B

Mismatch ❌

Up

Out of bounds ❌

Right
board[0][1] = B

Match ✅

Call:

dfs(0,1,1)
5️⃣ Second DFS Call
dfs(0,1,1)
board[0][1] = B
word[1] = B

Match.

Mark visited.

Grid:

# # C E
S F C S
A D E E

Next letter:

word[2] = C
6️⃣ Explore From (0,1)

Check directions.

Right
board[0][2] = C

Match.

Call:

dfs(0,2,2)
7️⃣ Third DFS Call
dfs(0,2,2)
board[0][2] = C
word[2] = C

Match.

Mark visited.

Grid:

# # # E
S F C S
A D E E

Next letter:

word[3] = C
8️⃣ Explore Neighbors

Check directions.

Down
board[1][2] = C

Match.

Call:

dfs(1,2,3)
9️⃣ Fourth DFS Call
dfs(1,2,3)

Grid:

# # # E
S F # S
A D E E

Next letter:

word[4] = E
🔟 Explore Neighbors

Check:

Down
board[2][2] = E

Match.

Call:

dfs(2,2,4)
1️⃣1️⃣ Fifth DFS Call
dfs(2,2,4)

Grid:

# # # E
S F # S
A D # E

Next letter:

word[5] = D
1️⃣2️⃣ Explore Neighbors

Check:

Left
board[2][1] = D

Match.

Call:

dfs(2,1,5)
1️⃣3️⃣ Final DFS
dfs(2,1,5)

Next index:

i = 6

Length of word:

len(word) = 6

Condition:

i == len(word)

True ✅

Word found!


🌳 Recursion Path

The successful path:

(0,0) A
   ↓
(0,1) B
   ↓
(0,2) C
   ↓
(1,2) C
   ↓
(2,2) E
   ↓
(2,1) D

"""             