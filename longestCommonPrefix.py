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

Complexity:

TC=>
    Sorting → O(n log n)
    Comparison → O(m)
    Total: O(n log n)

SC => O(1)

"""
    
    