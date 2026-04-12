"""

LC: 212. Word Search II

Hard

Topics
Array
String
Backtracking
Trie
Matrix

Hint
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
899,863/2.3M
Acceptance Rate
38.3%

Hint 1
You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
Hint 2
If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

"""

# Trie Node class
class TrieNode:
    def __init__(self):
        # Dictionary to store children (character → TrieNode)
        self.children = {}
        
        # Stores complete word at the end node (optimization)
        self.word = None


# Solution class
class Solution:
    def findWords(self, board, words):
        
        # 🔹 STEP 1: BUILD TRIE FROM WORD LIST
        
        # Create root node of Trie
        root = TrieNode()
        
        # Insert each word into Trie
        for word in words:
            node = root
            
            # Traverse each character of the word
            for ch in word:
                
                # If character not present → create new node
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                
                # Move to next node
                node = node.children[ch]
            
            # After inserting full word, store it at last node
            # This helps avoid rebuilding strings during DFS
            node.word = word
        
        
        # 🔹 STEP 2: PREPARE FOR DFS
        
        # Get board dimensions
        rows, cols = len(board), len(board[0])
        
        # List to store final found words
        result = []


        # 🔹 STEP 3: DEFINE DFS FUNCTION
        
        def dfs(r, c, node):
            
            # Get current character from board
            ch = board[r][c]
            
            # ❌ If character not in Trie → stop search early
            # This is the main optimization
            if ch not in node.children:
                return
            
            # Move to next Trie node
            next_node = node.children[ch]
            
            # ✅ If this node represents end of a word
            if next_node.word:
                
                # Add word to result
                result.append(next_node.word)
                
                # Set to None to avoid duplicate results
                next_node.word = None
            
            # 🔹 MARK CURRENT CELL AS VISITED
            # Replace with '#' to avoid revisiting
            board[r][c] = "#"
            
            # 🔹 EXPLORE ALL 4 DIRECTIONS (RIGHT, DOWN, LEFT, UP)
            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                
                # Calculate new row and column
                nr, nc = r + dr, c + dc
                
                # Check boundaries and if cell is not visited
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    
                    # Recursive DFS call
                    dfs(nr, nc, next_node)
            
            # 🔹 BACKTRACK (restore original character)
            board[r][c] = ch


        # 🔹 STEP 4: START DFS FROM EVERY CELL
        
        for i in range(rows):
            for j in range(cols):
                
                # Start DFS from each cell using Trie root
                dfs(i, j, root)


        # 🔹 STEP 5: RETURN RESULT
        
        return result


# 🔥 MAIN FUNCTION (for VS Code execution)
if __name__ == "__main__":
    
    # Input board (2D grid)
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    
    # List of words to search
    words = ["oath","pea","eat","rain"]
    
    # Create solution object
    sol = Solution()
    
    # Call function
    result = sol.findWords(board, words)
    
    # Print result
    print("Words found:", result)