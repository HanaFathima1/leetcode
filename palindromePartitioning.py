"""

LC: 131. Palindrome Partitioning
Medium

Topics
String
Dynamic Programming
Backtracking

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,311,275/1.8M
Acceptance Rate
73.8%

"""

class Solution:
    def partition(self,s:str)->list[list[str]]:
        res=[]
        path=[]
        def isPalindrome(sub):
            return sub==sub[::-1]
        def backtrack(start):
            if start==len(s):
                res.append(path[:])
                return
            for end in range(start,len(s)):
                substring=s[start:end+1]
                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(end+1)
                    path.pop()
        backtrack(0)
        return res
sol=Solution()
print(sol.partition(s = "aab"))
print(sol.partition(s = "a"))




"""

dry run

2️⃣ Initial State
res = []
path = []
start = 0

We call:

backtrack(0)
3️⃣ First Level (start = 0)

Loop:

for end in range(0,3)
end = 0

Substring:

s[0:1] = "a"

Palindrome ✔

path = ["a"]

Call recursion:

backtrack(1)
4️⃣ Second Level (start = 1)

Current state:

path = ["a"]

Loop:

for end in range(1,3)
end = 1

Substring:

s[1:2] = "a"

Palindrome ✔

path = ["a","a"]

Call recursion:

backtrack(2)
5️⃣ Third Level (start = 2)

Current state:

path = ["a","a"]

Loop:

for end in range(2,3)
end = 2

Substring:

s[2:3] = "b"

Palindrome ✔

path = ["a","a","b"]

Call recursion:

backtrack(3)
6️⃣ Base Case
start == len(s)
3 == 3

So we store the path:

res = [["a","a","b"]]

Now backtrack.

Remove last element:

path = ["a","a"]
7️⃣ Continue Second Level

Return to:

path = ["a"]

Now try next substring.

end = 2

Substring:

s[1:3] = "ab"

Check palindrome:

"ab" != "ba"

Not palindrome ❌

Stop this branch.

8️⃣ Back to First Level

Remove last element:

path = []

Continue loop.

end = 1

Substring:

s[0:2] = "aa"

Palindrome ✔

path = ["aa"]

Call recursion:

backtrack(2)
9️⃣ Next Level

Current state:

path = ["aa"]
start = 2

Loop:

end = 2

Substring:

s[2:3] = "b"

Palindrome ✔

path = ["aa","b"]

Call recursion:

backtrack(3)
🔟 Base Case Again
start == 3

Store result:

res = [["a","a","b"], ["aa","b"]]

Backtrack:

path = ["aa"]

Then:

path = []
11️⃣ Last Possibility

Return to first level.

end = 2

Substring:

s[0:3] = "aab"

Check palindrome:

"aab" != "baa"

Not palindrome ❌

12️⃣ Algorithm Ends

Final result:

[
 ["a","a","b"],
 ["aa","b"]
]
13️⃣ Recursion Tree Visualization
               []
             /    \
           "a"     "aa"
          /           \
       "a"             "b"
        |
       "b"

Paths found:

["a","a","b"]
["aa","b"]

"""
                