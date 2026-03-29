"""

LC: 451. Sort Characters By Frequency

Medium

Topics:
Hash Table
String
Sorting
Heap (Priority Queue)
Bucket Sort
Counting

Given a string s, sort it in decreasing order based on the frequency
of the characters. The frequency of a character is the number of 
times it appears in the string.
Return the sorted string. If there are multiple answers, return 
any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.

"""


import heapq
from collections import Counter
class Solution:
    def freqSort(self, s:str) -> str:
        freq_map = Counter(s)
        max_heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(max_heap)
        result=[]
        while max_heap:
            freq,char = heapq.heappop(max_heap)
            result.append(char*(-freq))
        return ''.join(result)
sol=Solution()
print(sol.freqSort(s = "tree"))
print(sol.freqSort(s = "cccaaa"))
