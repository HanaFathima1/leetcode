# LC:14.LONGEST COMMON PREFIX

# EASY

# TOPICS:
# Array
# String
# Trie

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestcommonprefix(strs):
    if len(strs) == 0:
        return ""
    
    base = strs[0]
    
    for i in range(len(base)):
        for word in strs[1:]:
            if (i==len(word) or word[i] != base[i]):
                return strs[0:i]
    return base
    
    