"""

LC: 1143. Longest Common Subsequence

Medium

Topics
String
Dynamic Programming

Hint
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,852,631/3.1M
Acceptance Rate
59.2%

Hint 1
Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
Hint 2
DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise

"""

#-------------------------------CODE1------------------------------------
class Solution:
    def longestCommonSubsequence(self, text1:str, text2:str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
sol = Solution()
print(sol.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
print(sol.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
print(sol.longestCommonSubsequence(text1 = "abc", text2 = "def"))



#------------------------------CODE2---------------------------------

class Solution:
    def longestCommonSubsequence(self, text1:str, text2:str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
sol = Solution()
print(sol.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
print(sol.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
print(sol.longestCommonSubsequence(text1 = "abc", text2 = "def"))


#-----------------------------------EXPLANATION---------------------------------

#CODE1

class Solution:
    def longestCommonSubsequence(self, text1:str, text2:str) -> int:

        # Length of both strings
        m, n = len(text1), len(text2)

        # Create DP table
        #
        # dp[i][j]
        #
        # Meaning:
        # LCS length between:
        #
        # text1[0:i]
        # and
        # text2[0:j]
        #
        # Extra row and column are added
        # to handle empty strings.
        dp = [[0] * (n+1) for _ in range(m+1)]

        # Traverse row by row
        for i in range(1, m+1):

            # Traverse column by column
            for j in range(1, n+1):

                # Compare current characters
                #
                # i-1 and j-1 are used because
                # DP table has one extra row/column.
                if text1[i-1] == text2[j-1]:

                    # Characters match
                    #
                    # Include this character
                    # in the LCS.
                    #
                    # Move diagonally.
                    dp[i][j] = 1 + dp[i-1][j-1]

                else:

                    # Characters don't match
                    #
                    # Option 1:
                    # Ignore character from text1
                    #
                    # Option 2:
                    # Ignore character from text2
                    #
                    # Take the better answer.
                    dp[i][j] = max(
                        dp[i-1][j],
                        dp[i][j-1]
                    )

        # Bottom-right cell contains answer
        return dp[m][n]

"""
Most Important Thing

In THIS version:

dp[i][j]

means:

LCS length between

first i characters of text1

and

first j characters of text2

Example

text1 = "abcde"
text2 = "ace"
dp[3][2]

means:

LCS of

"abc"

and

"ac"
Dry Run

Input:

text1 = "abcde"
text2 = "ace"

Lengths

m = 5
n = 3

Create table

        ""  a  c  e
     ----------------
"" |  0  0  0  0
a  |  0  0  0  0
b  |  0  0  0  0
c  |  0  0  0  0
d  |  0  0  0  0
e  |  0  0  0  0
Row 1

Current character:

a
j = 1

Compare:

a vs a

Match.

dp[1][1] = 1 + dp[0][0]
dp[1][1] = 1

Table:

        ""  a  c  e
     ----------------
"" |  0  0  0  0
a  |  0  1  0  0
b  |  0  0  0  0
c  |  0  0  0  0
d  |  0  0  0  0
e  |  0  0  0  0
j = 2

Compare:

a vs c

No match.

dp[1][2] =
max(
    dp[0][2],
    dp[1][1]
)
= max(0,1)
= 1
j = 3

Compare:

a vs e

No match.

dp[1][3] = 1

Table:

        ""  a  c  e
     ----------------
"" |  0  0  0  0
a  |  0  1  1  1
b  |  0  0  0  0
c  |  0  0  0  0
d  |  0  0  0  0
e  |  0  0  0  0
Row 2

Character:

b
j = 1

Compare:

b vs a

No match.

dp[2][1]
=
max(
dp[1][1],
dp[2][0]
)
= 1
j = 2

Compare:

b vs c

No match.

dp[2][2]
=
max(1,1)
=1
j = 3

Compare:

b vs e

No match.

dp[2][3]
=1

Table:

        ""  a  c  e
     ----------------
"" |  0  0  0  0
a  |  0  1  1  1
b  |  0  1  1  1
c  |  0  0  0  0
d  |  0  0  0  0
e  |  0  0  0  0
Row 3

Character:

c
j = 1

Compare:

c vs a

No match.

dp[3][1] = 1
j = 2

Compare:

c vs c

Match.

dp[3][2]
=
1 + dp[2][1]
= 2
j = 3

Compare:

c vs e

No match.

dp[3][3]
=
max(1,2)
=2

Table:

        ""  a  c  e
     ----------------
"" |  0  0  0  0
a  |  0  1  1  1
b  |  0  1  1  1
c  |  0  1  2  2
d  |  0  0  0  0
e  |  0  0  0  0
Row 4

Character:

d

No matches.

Row becomes:

0 1 2 2
Row 5

Character:

e

Compare:

e vs e

Match.

dp[5][3]
=
1 + dp[4][2]
= 3

Final table:

        ""  a  c  e
     ----------------
"" |  0  0  0  0
a  |  0  1  1  1
b  |  0  1  1  1
c  |  0  1  2  2
d  |  0  1  2  2
e  |  0  1  2  3
Final Answer
return dp[5][3]

which is:

3

because:

Longest Common Subsequence

ace

Length:

3
"""


#CODE2
class Solution:
    def longestCommonSubsequence(self, text1:str, text2:str) -> int:

        # Length of both strings
        m, n = len(text1), len(text2)

        # Create DP table
        #
        # dp[i][j]
        #
        # Meaning:
        # Length of LCS between:
        #
        # text1[i:]
        # text2[j:]
        #
        # Example:
        #
        # text1 = "abcde"
        # text2 = "ace"
        #
        # dp[1][1]
        #
        # means:
        #
        # LCS of
        # "bcde"
        # and
        # "ce"
        #
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill table from bottom-right
        #
        # Why?
        #
        # dp[i][j] depends on:
        #
        # dp[i+1][j]
        # dp[i][j+1]
        # dp[i+1][j+1]
        #
        # These are future states.
        #
        for i in range(m - 1, -1, -1):

            for j in range(n - 1, -1, -1):

                # If characters match
                if text1[i] == text2[j]:

                    # Include this character
                    #
                    # Move both pointers forward
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                else:

                    # Characters don't match
                    #
                    # Option 1:
                    # Skip character from text1
                    #
                    # Option 2:
                    # Skip character from text2
                    #
                    # Take larger answer
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )

        # dp[0][0]
        #
        # means:
        #
        # LCS of entire text1
        # and
        # entire text2
        #
        return dp[0][0]

"""
Most Important Idea

For:

text1 = "abcde"
text2 = "ace"
dp[0][0]

means:

LCS of

"abcde"

and

"ace"
dp[1][1]

means:

LCS of

"bcde"

and

"ce"
dp[2][2]

means:

LCS of

"cde"

and

"e"
Dry Run

Input:

text1 = "abcde"
text2 = "ace"

Lengths:

m = 5
n = 3

Create table:

         a   c   e   ""
      -----------------
a   |   0   0   0   0
b   |   0   0   0   0
c   |   0   0   0   0
d   |   0   0   0   0
e   |   0   0   0   0
""  |   0   0   0   0

Extra row and column are zeros.

Step 1
i = 4

Character:

e
j = 2

Character:

e

Compare:

e == e

Match.

dp[4][2]
=
1 + dp[5][3]
=
1 + 0
=
1

Table:

         a   c   e   ""
      -----------------
a   |   0   0   0   0
b   |   0   0   0   0
c   |   0   0   0   0
d   |   0   0   0   0
e   |   0   0   1   0
""  |   0   0   0   0
Step 2
i = 4
j = 1

Compare:

e vs c

No match.

dp[4][1]
=
max(
dp[5][1],
dp[4][2]
)
=
max(0,1)
=
1
j = 0

Compare:

e vs a

No match.

dp[4][0]
=
1

Row becomes:

e | 1 1 1 0
Step 3
i = 3

Character:

d

Compare with:

e

No match.

dp[3][2]
=
max(
dp[4][2],
dp[3][3]
)
=
max(1,0)
=
1

Continue.

Row becomes:

d | 1 1 1 0
Step 4
i = 2

Character:

c
j = 1

Character:

c

Match.

dp[2][1]
=
1 + dp[3][2]
=
1 + 1
=
2

This means:

LCS of

"cde"

and

"ce"

has length 2

which is:

ce

Row becomes:

c | 2 2 1 0
Step 5
i = 1

Character:

b

No matches.

Row becomes:

b | 2 2 1 0
Step 6
i = 0

Character:

a
j = 0

Character:

a

Match.

dp[0][0]
=
1 + dp[1][1]
=
1 + 2
=
3

Final table:

         a   c   e   ""
      -----------------
a   |   3   2   1   0
b   |   2   2   1   0
c   |   2   2   1   0
d   |   1   1   1   0
e   |   1   1   1   0
""  |   0   0   0   0
Why Return dp[0][0] ?

Remember:

dp[i][j]

means:

LCS of

text1[i:]

and

text2[j:]

Therefore:

dp[0][0]

means:

LCS of

text1[0:]
=
entire text1

and

text2[0:]
=
entire text2

which is exactly the original problem.
"""
 
"""

Comparison
Approach	State Meaning	               Fill Direction	TC	    SC
Prefix DP	text1[0:i], text2[0:j]	Top-Left → Bottom-Right	O(mn)	O(mn)
Suffix DP	text1[i:], text2[j:]	Bottom-Right → Top-Left	O(mn)	O(mn)

"""            