"""

LC: 6. Zigzag Conversion

Medium

Topics
String

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
2,243,568/4.1M
Acceptance Rate
54.3%

"""

class Solution:
    def convert(self, s:str, numRows:int) -> str:
        if numRows == 1:
            return s
        i = 0 
        d = 1
        rows = [[] for _ in range(numRows)]
        for char in s:
            rows[i].append(char)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d
        ret =''
        for i in range(numRows):
            ret += ''.join(rows[i])
        return ret
sol = Solution()
print(sol.convert(s = "PAYPALISHIRING", numRows = 3))
print(sol.convert(s = "PAYPALISHIRING", numRows = 4))


#EXPLANATION OF THE CODE
class Solution:
    def convert(self, s:str, numRows:int) -> str:

        # If there is only one row,
        # zigzag conversion is not needed.
        if numRows == 1:
            return s

        # Current row index
        i = 0

        # Direction:
        # 1  -> moving down
        # -1 -> moving up
        d = 1

        # Create empty rows
        # Example for numRows=3:
        # [[], [], []]
        rows = [[] for _ in range(numRows)]

        # Traverse every character in the string
        for char in s:

            # Put character in current row
            rows[i].append(char)

            # If we reach top row,
            # start moving downward
            if i == 0:
                d = 1

            # If we reach bottom row,
            # start moving upward
            elif i == numRows - 1:
                d = -1

            # Move to next row
            i += d

        # Final answer string
        ret = ''

        # Join characters of each row
        for i in range(numRows):
            ret += ''.join(rows[i])

        return ret


"""

==============DRY RUN==============

Input:

s = "PAYPALISHIRING"
numRows = 3

Initially:

i = 0
d = 1

rows = [
 [],
 [],
 []
]
Iteration 1
char = 'P'
rows[0].append('P')

rows:

[
 ['P'],
 [],
 []
]

Since

i == 0
d = 1

Move:

i = i + d
i = 0 + 1
i = 1
Iteration 2
char = 'A'

Put in row 1

rows[1].append('A')

rows:

[
 ['P'],
 ['A'],
 []
]

Not top or bottom.

i = 1 + 1
i = 2
Iteration 3
char = 'Y'

Put in row 2

rows[2].append('Y')

rows:

[
 ['P'],
 ['A'],
 ['Y']
]

Now:

i == numRows-1
i == 2

Bottom reached.

d = -1

Move:

i = 2 + (-1)
i = 1
Iteration 4
char = 'P'

Put in row 1

[
 ['P'],
 ['A','P'],
 ['Y']
]

Move up:

i = 1 + (-1)
i = 0
Iteration 5
char = 'A'

Put in row 0

[
 ['P','A'],
 ['A','P'],
 ['Y']
]

Top reached

d = 1

Move

i = 1

Continue similarly...

Final rows become:

[
 ['P','A','H','N'],
 ['A','P','L','S','I','I','G'],
 ['Y','I','R']
]
Visual Zigzag
Row0: P   A   H   N

Row1: A P L S I I G

Row2: Y   I   R

Equivalent to:

P   A   H   N
A P L S I I G
Y   I   R
Building Answer

Initially

ret = ''
Row 0
''.join(['P','A','H','N'])

gives

"PAHN"
ret = "PAHN"
Row 1
''.join(['A','P','L','S','I','I','G'])

gives

"APLSIIG"
ret = "PAHNAPLSIIG"
Row 2
''.join(['Y','I','R'])

gives

"YIR"
ret = "PAHNAPLSIIGYIR"
Output
PAHNAPLSIIGYIR

"""

"""

===============COMPLEXITY=================

T.C: O(n * numRows)
S.C: O(numRows + n)

"""

"""

Note: the zig-zag pattern is like this y'all

|    /|    /|    /|
|  /  |  /  |  /  |
|/    |/    |/    |

"""