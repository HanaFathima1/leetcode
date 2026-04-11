"""

LC: 1268. Search Suggestions System

Medium

Topics
Senior
Array
String
Binary Search
Trie
Sorting
Heap (Priority Queue)
Weekly Contest 164

Hint
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.
 

Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
439,580/674.7K
Acceptance Rate
65.2%

Hint 1
Brute force is a good choice because length of the string is ≤ 1000.
Hint 2
Binary search the answer.
Hint 3
Use Trie data structure to store the best three matching. Traverse the Trie.

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.suggestions.append(word)
            node.suggestions.sort()
            if len(node.suggestions)>3:
                node.suggestions.pop()
                
class Solution:
    def suggestedProducts(self, products:list[str], searchWord:str) -> list[list[str]]:
        products.sort()
        trie=Trie()
        for word in products:
            trie.insert(word)
        result= []
        node=trie.root
        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                result.append(node.suggestions)
            else:
                node=None
                result.append([])
        return result
 
if __name__=="__main__":
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    sol = Solution()
    result = sol.suggestedProducts(products, searchWord)
    print(result)
        