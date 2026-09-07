"""

LC:14.LONGEST COMMON PREFIX

EASY

TOPICS:
Array
String
Trie

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

def longestcommonprefix(strs):
    if len(strs) == 0:
        return ""
    
    base = strs[0]
    
    for i in range(len(base)):
        for word in strs[1:]:
            if (i==len(word) or word[i] != base[i]):
                return base[0:i]
    return base
print(longestcommonprefix(strs = ["flower","flow","flight"]))
print(longestcommonprefix(strs = ["dog","racecar","car"]))


"""

DRY RUN
Initial Values
strs = ["flower", "flow", "flight"]

base = "flower"

Remaining words

["flow", "flight"]
Outer Loop (i = 0)

Current character of base

base[0] = 'f'
Compare with "flow"
flow[0] = 'f'

f == f ✅
Compare with "flight"
flight[0] = 'f'

f == f ✅

Both match.

Move to next character.

Outer Loop (i = 1)
base[1] = 'l'
Compare with "flow"
flow[1] = 'l'

Match ✅
Compare with "flight"
flight[1] = 'l'

Match ✅

Continue.

Outer Loop (i = 2)
base[2] = 'o'
Compare with "flow"
flow[2] = 'o'

Match ✅
Compare with "flight"
flight[2] = 'i'

o != i ❌

Condition becomes

word[i] != base[i]

So return

base[:2]

which is

"fl"

Algorithm stops.

Dry Run Table
| i | base[i] | flow | flight | Result        |
| - | ------- | ---- | ------ | ------------- |
| 0 | f       | f✅   | f✅     | Continue      |
| 1 | l       | l✅   | l✅     | Continue      |
| 2 | o       | o✅   | i❌     | Return `"fl"` |


Output

fl
Example 2
strs = ["dog","racecar","car"]

Base

dog
i = 0
base[0]='d'

racecar[0]='r'

Mismatch immediately.

Return

base[:0]

which is

""

Output

""

Complexity:
    TC => O(n * m)
        n = number of strings
        m = length of the shortest string
    SC => O(1)

"""


def longestCommonPrefix(strs):
    # Step 1: Sort the list of strings
    strs.sort()
    
    # Step 2: Take first and last strings
    first = strs[0]
    last = strs[-1]
    
    i = 0
    
    # Step 3: Compare characters
    while i < len(first) and first[i] == last[i]:
        i += 1
    
    # Step 4: Return common prefix
    return first[:i]

"""

DRY RUN
Initial Input
["flower","flow","flight"]
Step 1

Sort the array.

Before sorting

flower
flow
flight

After sorting

flight
flow
flower

So

first = "flight"

last = "flower"
Compare first and last
i = 0
flight[0] = f

flower[0] = f

Match

i = 1
i = 1
flight[1] = l

flower[1] = l

Match

i = 2
i = 2
flight[2] = i

flower[2] = o

Mismatch.

Loop stops.

Return

first[:2]

which is

"fl"
Dry Run Table

Sorted List

flight
flow
flower
| i | first | last | Match |
| - | ----- | ---- | ----- |
| 0 | f     | f    | ✅     |
| 1 | l     | l    | ✅     |
| 2 | i     | o    | ❌     |

Return

fl
Example 2

Input

["dog","racecar","car"]

After sorting

car
dog
racecar

So

first = "car"

last = "racecar"

Compare

c vs r

Mismatch immediately.

Return

""

Complexity:

TC=>
    Sorting → O(n log n)
    Comparison → O(m)
    Total: O(n log n)

SC => O(1)

"""
    
    