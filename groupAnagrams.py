"""

LC: 49. Group Anagrams

Attempted

Medium

Topics
Array
Hash Table
String
Sorting

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
4,965,693/6.8M
Acceptance Rate
73.0%

"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs:list[str])->list[list[str]]:
        groups=defaultdict(list)
        for word in strs:
            key="".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())
sol=Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams(strs = [""]))
print(sol.groupAnagrams(strs = ["a"]))


"""

DRY RUN

Dry Run 1

Input:

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Initially:

groups = defaultdict(list)

It is empty:

{}
Iteration 1
word = "eat"

Sort it:

sorted("eat") → ['a', 'e', 't']

Join:

"aet"

Therefore:

key = "aet"

Now:

groups["aet"].append("eat")

groups becomes:

{
    "aet": ["eat"]
}
Iteration 2
word = "tea"

Sort:

sorted("tea") → ['a', 'e', 't']

Join:

"aet"

So:

key = "aet"

Then:

groups["aet"].append("tea")

Now:

{
    "aet": ["eat", "tea"]
}

Because "tea" has the same key as "eat", they go into the same group.

Iteration 3
word = "tan"

Sort:

sorted("tan") → ['a', 'n', 't']

Join:

"ant"

So:

key = "ant"

Append:

groups["ant"].append("tan")

Now:

{
    "aet": ["eat", "tea"],
    "ant": ["tan"]
}
Iteration 4
word = "ate"

Sort:

sorted("ate") → ['a', 'e', 't']

Key:

"aet"

Append:

groups["aet"].append("ate")

Now:

{
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan"]
}
Iteration 5
word = "nat"

Sort:

sorted("nat") → ['a', 'n', 't']

Key:

"ant"

Append:

groups["ant"].append("nat")

Now:

{
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"]
}
Iteration 6
word = "bat"

Sort:

sorted("bat") → ['a', 'b', 't']

Key:

"abt"

Append:

groups["abt"].append("bat")

Final dictionary:

{
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
Finally

Your code does:

return list(groups.values())

groups.values() gives:

[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]

So the output is:

[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

The exact ordering of the groups isn't important for the problem.

Dry Run Table

This is the most important table to remember:

| `word`  | `sorted(word)`  | `key`   | `groups` after insertion |
| ------- | --------------- | ------- | ------------------------ |
| `"eat"` | `['a','e','t']` | `"aet"` | `aet → [eat]`            |
| `"tea"` | `['a','e','t']` | `"aet"` | `aet → [eat, tea]`       |
| `"tan"` | `['a','n','t']` | `"ant"` | `ant → [tan]`            |
| `"ate"` | `['a','e','t']` | `"aet"` | `aet → [eat, tea, ate]`  |
| `"nat"` | `['a','n','t']` | `"ant"` | `ant → [tan, nat]`       |
| `"bat"` | `['a','b','t']` | `"abt"` | `abt → [bat]`            |


Final:

aet → [eat, tea, ate]
ant → [tan, nat]
abt → [bat]
Dry Run 2: [""]

Input:

strs = [""]

Initially:

groups = {}
Iteration
word = ""

Sort:

sorted("")

gives:

[]

Then:

"".join([])

gives:

""

Therefore:

key = ""

Then:

groups[""].append("")

Now:

{
    "": [""]
}

Finally:

list(groups.values())

gives:

[[""]]
Output
[[""]]
Dry Run 3: ["a"]

Input:

strs = ["a"]

Initially:

groups = {}
Iteration
word = "a"

Sort:

sorted("a") → ['a']

Join:

"a"

Therefore:

key = "a"

Append:

groups["a"].append("a")

Now:

{
    "a": ["a"]
}

Finally:

list(groups.values())

gives:

[["a"]]
Output
[["a"]]

"""