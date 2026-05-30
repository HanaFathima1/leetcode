"""

LC: 91. Decode Ways

Medium

Topics
Staff
String
Dynamic Programming

You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,669,772/4.4M
Acceptance Rate
38.0%

"""

class Solution:
    def numDecodings(self, s: str) -> int:

        # Length of the string
        n = len(s)

        # DP array of size n+1
        # dp[i] = number of ways to decode the substring starting at index i
        dp = [0] * (n + 1)

        # Base Case:
        # If we have successfully reached beyond the last character,
        # that means we found ONE valid decoding.
        dp[n] = 1

        # Fill the DP array from right to left
        # because dp[i] depends on dp[i+1] and dp[i+2]
        for i in range(n - 1, -1, -1):

            # A substring starting with '0' is invalid
            # Example:
            # "06" -> invalid
            # "0"  -> invalid
            if s[i] == "0":
                dp[i] = 0

            else:

                # -------------------------
                # Choice 1: Take ONE digit
                # -------------------------
                #
                # Example:
                # "226"
                #  ^
                #
                # Take '2'
                #
                # Remaining string:
                # "26"
                #
                # Number of ways from there:
                # dp[i+1]
                #
                dp[i] = dp[i + 1]

                # -------------------------
                # Choice 2: Take TWO digits
                # -------------------------
                #
                # Check whether the two-digit number
                # formed by s[i] and s[i+1]
                # lies between 10 and 26.
                #
                # Examples:
                #
                # "22" -> valid
                # "26" -> valid
                # "27" -> invalid
                # "06" -> invalid
                #
                if (
                    i + 1 < n
                    and
                    10 <= int(s[i:i+2]) <= 26
                ):

                    # Add all decoding ways obtained
                    # after consuming two digits.
                    #
                    # Example:
                    #
                    # "226"
                    #  ^^
                    #
                    # Take "22"
                    #
                    # Remaining:
                    # "6"
                    #
                    # Ways = dp[i+2]
                    #
                    dp[i] += dp[i + 2]

        # dp[0] contains the answer for the entire string
        return dp[0]
sol = Solution()
print(sol.numDecodings(s = "12"))
print(sol.numDecodings(s = "226"))
print(sol.numDecodings(s = "06"))
            

"""

Dry Run on "226"
Initialize
s = "226"
n = 3

dp = [0,0,0,1]
Index
0 1 2 3
2 2 6 X

dp
0 0 0 1
i = 2

Character:

6

Not zero.

Single digit:

dp[2] = dp[3]
dp[2] = 1

Current:

0 0 1 1
i = 1

Character:

2

Single digit:

dp[1] = dp[2]
dp[1] = 1

Two digits:

26

Valid.

Add:

dp[3]
dp[1] = 1 + 1 = 2

Current:

0 2 1 1
i = 0

Character:

2

Single digit:

dp[0] = dp[1]
dp[0] = 2

Two digits:

22

Valid.

Add:

dp[2]
dp[0] = 2 + 1 = 3

Current:

3 2 1 1

Answer:

dp[0] = 3

"""