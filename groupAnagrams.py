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
