"""

LC: 72. Edit Distance

Medium

Topics
String
Dynamic Programming

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,478,514/2.4M
Acceptance Rate
60.7%

"""
#references: https://youtu.be/XYi2-LPrwm4?si=IJ5CGgpv6fJ8n8SS

class Solution:
    def minDistance(self, word1:str, word2:str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for j in range(n+1):
            dp[m][j] = n - j
        for i in range(m+1):
            dp[i][n] = m - i
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:

                    dp[i][j] = 1 + min(
                        dp[i+1][j],      # delete
                        dp[i][j+1],      # insert
                        dp[i+1][j+1]     # replace
                    )
                #or
                # else:
                #     delete_cost = dp[i+1][j]
                #     insert_cost = dp[i][j+1]
                #     replace_cost = dp[i+1][j+1]
                #     dp[i][j] = 1 + min(delete_cost, insert_cost, replace_cost)
        return dp[0][0]
sol = Solution()
print(sol.minDistance(word1 = "horse", word2 = "ros")) 
print(sol.minDistance(word1 = "intention", word2 = "execution")) 
            

#EXPLANATION

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # Length of both strings
        m = len(word1)
        n = len(word2)

        # Create DP table
        #
        # dp[i][j]
        #
        # Meaning:
        # Minimum operations required to convert
        #
        # word1[i:]
        # into
        # word2[j:]
        #
        # Example:
        #
        # word1 = "horse"
        # word2 = "ros"
        #
        # dp[1][1]
        #
        # means:
        #
        # Convert:
        # "orse"
        #
        # into:
        # "os"
        #
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # -----------------------------
        # Base Case 1
        # -----------------------------
        #
        # If word1 is exhausted:
        #
        # ""
        # →
        # remaining part of word2
        #
        # We must INSERT all remaining characters.
        #
        # Example:
        #
        # ""
        # →
        # "ros"
        #
        # Need:
        # insert r
        # insert o
        # insert s
        #
        # Total = 3 operations
        #
        for j in range(n + 1):
            dp[m][j] = n - j

        # -----------------------------
        # Base Case 2
        # -----------------------------
        #
        # If word2 is exhausted:
        #
        # remaining part of word1
        # →
        # ""
        #
        # We must DELETE all remaining characters.
        #
        # Example:
        #
        # "horse"
        # →
        # ""
        #
        # delete h
        # delete o
        # delete r
        # delete s
        # delete e
        #
        # Total = 5 operations
        #
        for i in range(m + 1):
            dp[i][n] = m - i

        # Fill DP table from bottom-right
        #
        # Why?
        #
        # dp[i][j] depends on:
        #
        # dp[i+1][j]
        # dp[i][j+1]
        # dp[i+1][j+1]
        #
        # These states must already be computed.
        """ 
        r   o   s   ""
       -----------------
h     |   ?   ?   ?   5
o     |   ?   ?   ?   4
r     |   ?   ?   ?   3
s     |   ?   ?   ?   2
e     |   ?   ?   ?   1
""    |   3   2   1   0

        """
        #
        for i in range(m - 1, -1, -1):

            for j in range(n - 1, -1, -1):

                # If current characters match
                #
                # Example:
                #
                # o == o
                #
                # No operation needed.
                #
                if word1[i] == word2[j]:

                    # Move both pointers forward
                    dp[i][j] = dp[i + 1][j + 1]

                else:

                    # Characters are different
                    #
                    # Example:
                    #
                    # h != r
                    #
                    # We have 3 choices
                    #

                    # Choice 1: Delete
                    #
                    # Delete current character from word1
                    #
                    # horse
                    # ^
                    #
                    # delete h
                    #
                    delete_cost = dp[i + 1][j]

                    # Choice 2: Insert
                    #
                    # Insert current character of word2
                    #
                    # horse
                    # ros
                    # ^
                    #
                    # insert r
                    #
                    insert_cost = dp[i][j + 1]

                    # Choice 3: Replace
                    #
                    # Replace current character
                    #
                    # h -> r
                    #
                    replace_cost = dp[i + 1][j + 1]

                    # We perform one operation
                    # +
                    # minimum cost among the 3 choices
                    dp[i][j] = 1 + min(
                        delete_cost,
                        insert_cost,
                        replace_cost
                    )

        # dp[0][0]
        #
        # Means:
        #
        # Convert entire word1
        # into
        # entire word2
        #
        # This is exactly what the problem asks.
        #
        return dp[0][0]
    
"""

DP Notebook Summary
State
dp[i][j]

Meaning:

Minimum operations needed to convert

word1[i:]

into

word2[j:]
If Characters Match
dp[i][j] = dp[i+1][j+1]

Reason:

No operation needed
Move both pointers
If Characters Don't Match

Three choices:

Delete
Insert
Replace

Recurrence:

dp[i][j]=1+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])

Base Cases
dp[m][j] = n - j

Need to insert remaining characters.

dp[i][n] = m - i

Need to delete remaining characters.

Fill Direction
Bottom → Top
Right → Left

because:

dp[i][j]

depends on:

dp[i+1][j]
dp[i][j+1]
dp[i+1][j+1]
Answer
dp[0][0]

because it represents converting the entire word1 into the entire word2.

Complexity
Time Complexity  : O(m × n)

Space Complexity : O(m × n)

where:

m = len(word1)
n = len(word2)

"""